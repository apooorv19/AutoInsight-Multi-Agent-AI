"""Supervisor agent that only coordinates the workflow."""

from __future__ import annotations

import logging
from typing import Any

from app.state import FlowState

logger = logging.getLogger(__name__)


def supervisor_agent(state: FlowState) -> dict[str, Any]:
    """Log the start of the workflow and pass state through unchanged."""

    logger.info("Supervisor Agent started")
    try:
        if not state.get("dataset_path"):
            warnings = list(state.get("warnings", []))
            warnings.append("No dataset path was provided.")
            logger.info("Supervisor Agent finished")
            return {"warnings": warnings}

        logger.info("Supervisor Agent finished")
        return {}
    except Exception as exc:  # pragma: no cover - defensive guard.
        logger.exception("Supervisor Agent failed")
        warnings = list(state.get("warnings", []))
        warnings.append(f"Supervisor error: {exc}")
        return {"warnings": warnings}
