"""Single LangGraph workflow for AutoInsight AI."""

from __future__ import annotations

import logging
from typing import Any

from langgraph.graph import END, StateGraph

from app.agents.data_agent import data_understanding_agent
from app.agents.insight_agent import insight_agent
from app.agents.report_agent import report_agent
from app.agents.statistics_agent import statistics_agent
from app.agents.supervisor import supervisor_agent
from app.agents.visualization_agent import visualization_agent
from app.state import FlowState


def _configure_logging() -> None:
    """Configure root logging once for the whole project."""

    root_logger = logging.getLogger()
    if not root_logger.handlers:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )


_configure_logging()


def build_graph() -> Any:
    """Create the linear workflow used by the app."""

    workflow = StateGraph(FlowState)
    workflow.add_node("supervisor", supervisor_agent)
    workflow.add_node("data_understanding", data_understanding_agent)
    workflow.add_node("statistics", statistics_agent)
    workflow.add_node("visualization", visualization_agent)
    workflow.add_node("insight", insight_agent)
    workflow.add_node("report", report_agent)

    workflow.set_entry_point("supervisor")
    workflow.add_edge("supervisor", "data_understanding")
    workflow.add_edge("data_understanding", "statistics")
    workflow.add_edge("statistics", "visualization")
    workflow.add_edge("visualization", "insight")
    workflow.add_edge("insight", "report")
    workflow.add_edge("report", END)

    return workflow.compile()


analysis_graph = build_graph()


def run_analysis(dataset_path: str) -> FlowState:
    """Execute the graph for a single uploaded CSV file."""

    return analysis_graph.invoke({"dataset_path": dataset_path, "warnings": []})
