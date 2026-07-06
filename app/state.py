"""Shared LangGraph state for AutoInsight AI."""

from typing import Any, TypedDict


class FlowState(TypedDict, total=False):
    """Small state container passed through the analysis workflow."""

    dataset_path: str
    metadata: dict[str, Any]
    statistics: dict[str, Any]
    plots: list[dict[str, Any]]
    insights: str
    report: str
    warnings: list[str]
