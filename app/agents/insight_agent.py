"""Agent that interprets results using the LLM."""

from __future__ import annotations

import logging
import os
from typing import Any

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.llm import get_llm
from app.state import FlowState

logger = logging.getLogger(__name__)

INSIGHT_SYSTEM_PROMPT = """You are the Insight Agent in AutoInsight AI.

Your job is to interpret the dataset using the provided metadata, statistics, and plot summaries.
Do not recalculate statistics.
Do not invent values.
Focus on:
- business-relevant patterns
- anomalies and possible data quality issues
- practical recommendations

Write concise, professional markdown with short sections and clear bullet points."""


def insight_agent(state: FlowState) -> dict[str, Any]:
    """Interpret the analysis results and return concise business insights."""

    logger.info("Insight Agent started")
    warnings = list(state.get("warnings", []))
    metadata = state.get("metadata", {})
    statistics = state.get("statistics", {})
    plots = state.get("plots", [])

    try:
        if not metadata or not statistics:
            warnings.append("Insight Agent skipped because metadata or statistics are missing.")
            insights = _build_fallback_insights(metadata, statistics, plots)
            logger.info("Insight Agent finished")
            return {"insights": insights, "warnings": warnings}

        if not os.getenv("GROQ_API_KEY"):
            warnings.append("GROQ_API_KEY is not set. Using a local fallback insight summary.")
            insights = _build_fallback_insights(metadata, statistics, plots)
            logger.info("Insight Agent finished")
            return {"insights": insights, "warnings": warnings}

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", INSIGHT_SYSTEM_PROMPT),
                ("human", "{context}"),
            ]
        )
        chain = prompt | get_llm() | StrOutputParser()
        context = _build_insight_context(metadata, statistics, _build_plot_summaries(plots))
        insights = chain.invoke({"context": context})

        logger.info("Insight Agent finished")
        return {"insights": insights, "warnings": warnings}
    except Exception as exc:  # pragma: no cover - defensive guard.
        logger.exception("Insight Agent failed")
        warnings.append(f"Insight generation error: {exc}")
        insights = _build_fallback_insights(metadata, statistics, plots)
        return {"insights": insights, "warnings": warnings}


def _build_plot_summaries(plots: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep only the readable parts of each plot for the prompt."""

    return [
        {"title": plot.get("title", "Plot"), "summary": plot.get("summary", "")}
        for plot in plots
    ]


def _build_insight_context(
    metadata: dict[str, Any],
    statistics: dict[str, Any],
    plot_summaries: list[dict[str, Any]],
) -> str:
    """Format the analysis inputs for the LLM."""

    return (
        "Metadata:\n"
        f"{_to_json(metadata)}\n\n"
        "Statistics:\n"
        f"{_to_json(statistics)}\n\n"
        "Visualization summaries:\n"
        f"{_to_json(plot_summaries)}\n\n"
        "Return insights, notable patterns, anomalies, and recommendations."
    )


def _to_json(value: Any) -> str:
    """Render a Python object as pretty JSON for the prompt."""

    import json

    return json.dumps(value, indent=2, default=str)


def _build_fallback_insights(
    metadata: dict[str, Any],
    statistics: dict[str, Any],
    plots: list[dict[str, Any]],
) -> str:
    """Generate a simple local summary when the LLM is unavailable."""

    lines = ["### Insights", "", "- LLM output was unavailable, so this summary is rule-based."]

    duplicate_rows = metadata.get("duplicate_rows", 0)
    if duplicate_rows:
        lines.append(f"- {duplicate_rows} duplicate rows were detected and should be reviewed.")

    missing_percentage = statistics.get("missing_percentage", {})
    high_missing = [
        f"{column} ({float(value):.1f}%)"
        for column, value in missing_percentage.items()
        if float(value) >= 20.0
    ]
    if high_missing:
        lines.append("- Columns with substantial missing data: " + ", ".join(high_missing) + ".")

    correlation = statistics.get("correlation", {})
    strong_pairs = _find_strong_correlations(correlation)
    if strong_pairs:
        lines.append("- Strong correlations detected: " + ", ".join(strong_pairs) + ".")

    if not duplicate_rows and not high_missing and not strong_pairs:
        lines.append("- The dataset looks reasonably clean based on the available summary statistics.")

    if plots:
        lines.append(f"- {len(plots)} visualization(s) were generated successfully.")

    lines.append("- Next step: confirm these patterns against domain knowledge before making decisions.")
    return "\n".join(lines)


def _find_strong_correlations(correlation: dict[str, Any]) -> list[str]:
    """Extract correlation pairs with an absolute value of 0.8 or higher."""

    pairs: list[str] = []
    seen: set[tuple[str, str]] = set()

    for left_column, related_columns in correlation.items():
        if not isinstance(related_columns, dict):
            continue
        for right_column, value in related_columns.items():
            if left_column == right_column:
                continue

            pair = tuple(sorted((left_column, right_column)))
            if pair in seen:
                continue

            try:
                if abs(float(value)) >= 0.8:
                    pairs.append(f"{pair[0]} vs {pair[1]} ({float(value):.2f})")
                    seen.add(pair)
            except (TypeError, ValueError):
                continue

    return pairs[:3]
