"""Agent that understands the dataset structure and quality."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from app.state import FlowState
from app.tools.dataframe import build_dataset_metadata, load_csv

logger = logging.getLogger(__name__)


def data_understanding_agent(state: FlowState) -> dict[str, Any]:
    """Load the CSV and return structured metadata."""

    logger.info("Data Understanding Agent started")
    warnings = list(state.get("warnings", []))
    dataset_path = state.get("dataset_path")

    try:
        if not dataset_path:
            warnings.append("Data Understanding Agent skipped because no dataset path was provided.")
            logger.info("Data Understanding Agent finished")
            return {"metadata": {}, "warnings": warnings}

        if not Path(dataset_path).exists():
            warnings.append(f"Dataset not found: {dataset_path}")
            logger.info("Data Understanding Agent finished")
            return {"metadata": {}, "warnings": warnings}

        dataframe = load_csv(dataset_path)
        metadata = build_dataset_metadata(dataframe, dataset_path)
        logger.info("Data Understanding Agent finished")
        return {"metadata": metadata, "warnings": warnings}
    except Exception as exc:  # pragma: no cover - defensive guard.
        logger.exception("Data Understanding Agent failed")
        warnings.append(f"Data understanding error: {exc}")
        return {"metadata": {}, "warnings": warnings}
