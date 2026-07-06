"""Agent that turns the workflow output into a Markdown report."""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

from app.state import FlowState

logger = logging.getLogger(__name__)


def report_agent(state: FlowState) -> dict[str, Any]:
    """Combine metadata, statistics, plots, and insights into a Markdown report."""

    logger.info("Report Agent started")
    try:
        report = _build_report(
            metadata=state.get("metadata", {}),
            statistics=state.get("statistics", {}),
            plots=state.get("plots", []),
            insights=state.get("insights", "No insights were generated."),
            warnings=state.get("warnings", []),
        )
        _save_report(report, state.get("metadata", {}))
        logger.info("Report Agent finished")
        return {"report": report}
    except Exception as exc:  # pragma: no cover - defensive guard.
        logger.exception("Report Agent failed")
        fallback_report = f"# AutoInsight AI Report\n\nReport generation failed: {exc}"
        return {"report": fallback_report}


def _build_report(
    metadata: dict[str, Any],
    statistics: dict[str, Any],
    plots: list[dict[str, Any]],
    insights: str,
    warnings: list[str],
) -> str:
    """Render a compact Markdown report."""

    sections = [
        "# AutoInsight AI Report",
        "",
        "## Dataset Overview",
        f"- Dataset: {metadata.get('dataset_name', 'Unknown')}",
        f"- Dimensions: {metadata.get('rows', 0)} rows x {metadata.get('columns', 0)} columns",
        f"- Duplicate rows: {metadata.get('duplicate_rows', 0)}",
        f"- Numerical columns: {', '.join(metadata.get('column_types', {}).get('numerical_columns', [])) or 'None'}",
        f"- Categorical columns: {', '.join(metadata.get('column_types', {}).get('categorical_columns', [])) or 'None'}",
        f"- Datetime columns: {', '.join(metadata.get('column_types', {}).get('datetime_columns', [])) or 'None'}",
        "",
        "## Summary Statistics",
        _render_table("Summary Statistics", statistics.get("summary_statistics", {})),
        _render_table("Mean", statistics.get("mean", {})),
        _render_table("Median", statistics.get("median", {})),
        _render_table("Standard Deviation", statistics.get("standard_deviation", {})),
        _render_table("Skewness", statistics.get("skewness", {})),
        _render_table("Correlation", statistics.get("correlation", {})),
    ]

    categorical_summary = statistics.get("categorical_summary")
    if categorical_summary:
        sections.extend([
            _render_table("Categorical Summary", categorical_summary),
        ])

    sections.extend([
        "## Visualizations",
        _render_plot_summaries(plots),
        "## AI Insights",
        insights,
    ])

    if warnings:
        sections.extend([
            "## Warnings",
            _render_bullets(warnings),
        ])

    return "\n".join(section for section in sections if section)


def _render_table(title: str, data: dict[str, Any]) -> str:
    """Render a nested mapping as a plain text table inside a Markdown fence."""

    if not data:
        return f"### {title}\n\nNo data available."

    frame = pd.DataFrame.from_dict(data, orient="index")
    return f"### {title}\n\n```text\n{frame.round(3).to_string()}\n```"


def _render_plot_summaries(plots: list[dict[str, Any]]) -> str:
    """Render a short summary of the generated plots."""

    if not plots:
        return "No plots were generated."

    return _render_bullets([f"{plot.get('title', 'Plot')}: {plot.get('summary', '')}" for plot in plots])


def _render_bullets(items: list[str]) -> str:
    """Convert a list of strings into Markdown bullets."""

    return "\n".join(f"- {item}" for item in items)


def _save_report(report: str, metadata: dict[str, Any]) -> None:
    """Persist the generated report in the reports folder."""

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    dataset_name = metadata.get("dataset_name", "dataset").replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = reports_dir / f"{dataset_name}_{timestamp}.md"
    report_path.write_text(report, encoding="utf-8")
