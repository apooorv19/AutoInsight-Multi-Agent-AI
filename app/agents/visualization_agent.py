"""Agent that creates the most useful visualizations."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from app.state import FlowState
from app.tools.dataframe import build_dataset_metadata, load_csv
from app.tools.plotting import create_visualizations

logger = logging.getLogger(__name__)


def visualization_agent(state: FlowState) -> dict[str, Any]:
    """Create plots and skip invalid ones without crashing."""

    logger.info("Visualization Agent started")
    warnings = list(state.get("warnings", []))
    dataset_path = state.get("dataset_path")

    try:
        if not dataset_path:
            warnings.append("Visualization Agent skipped because no dataset path was provided.")
            logger.info("Visualization Agent finished")
            return {"plots": [], "warnings": warnings}

        if not Path(dataset_path).exists():
            warnings.append(f"Dataset not found: {dataset_path}")
            logger.info("Visualization Agent finished")
            return {"plots": [], "warnings": warnings}

        dataframe = load_csv(dataset_path)
        metadata = state.get("metadata") or build_dataset_metadata(dataframe, dataset_path)
        plots, plot_warnings = create_visualizations(dataframe, metadata)
        warnings.extend(plot_warnings)
        logger.info("Visualization Agent finished")
        return {"plots": plots, "warnings": warnings}
    except Exception as exc:  # pragma: no cover - defensive guard.
        logger.exception("Visualization Agent failed")
        warnings.append(f"Visualization error: {exc}")
        return {"plots": [], "warnings": warnings}
