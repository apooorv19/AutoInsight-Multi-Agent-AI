"""Agent that computes statistics in Python only."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from app.state import FlowState
from app.tools.dataframe import load_csv
from app.tools.statistics import calculate_statistics

logger = logging.getLogger(__name__)


def statistics_agent(state: FlowState) -> dict[str, Any]:
    """Load the CSV and calculate numerical statistics."""

    logger.info("Statistics Agent started")
    warnings = list(state.get("warnings", []))
    dataset_path = state.get("dataset_path")

    try:
        if not dataset_path:
            warnings.append("Statistics Agent skipped because no dataset path was provided.")
            logger.info("Statistics Agent finished")
            return {"statistics": {}, "warnings": warnings}

        if not Path(dataset_path).exists():
            warnings.append(f"Dataset not found: {dataset_path}")
            logger.info("Statistics Agent finished")
            return {"statistics": {}, "warnings": warnings}

        dataframe = load_csv(dataset_path)
        statistics = calculate_statistics(dataframe)
        logger.info("Statistics Agent finished")
        return {"statistics": statistics, "warnings": warnings}
    except Exception as exc:  # pragma: no cover - defensive guard.
        logger.exception("Statistics Agent failed")
        warnings.append(f"Statistics error: {exc}")
        return {"statistics": {}, "warnings": warnings}
