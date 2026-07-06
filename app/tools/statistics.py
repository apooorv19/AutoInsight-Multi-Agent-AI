"""Pure Python statistics helpers for CSV analysis."""

from __future__ import annotations

from typing import Any

import pandas as pd


def calculate_statistics(df: pd.DataFrame) -> dict[str, Any]:
    """Calculate the numeric statistics required by the project."""

    numeric_df = df.select_dtypes(include="number")
    categorical_df = df.select_dtypes(exclude="number")

    statistics: dict[str, Any] = {
        "summary_statistics": numeric_df.describe().round(3).to_dict() if not numeric_df.empty else {},
        "mean": numeric_df.mean().round(3).to_dict() if not numeric_df.empty else {},
        "median": numeric_df.median().round(3).to_dict() if not numeric_df.empty else {},
        "standard_deviation": numeric_df.std().round(3).to_dict() if not numeric_df.empty else {},
        "skewness": numeric_df.skew().round(3).to_dict() if not numeric_df.empty else {},
        "correlation": numeric_df.corr().round(3).to_dict() if numeric_df.shape[1] > 1 else {},
        "missing_percentage": (df.isna().mean().mul(100).round(2)).to_dict(),
    }

    if not categorical_df.empty:
        statistics["categorical_summary"] = categorical_df.describe(include="all").fillna("").to_dict()

    return statistics
