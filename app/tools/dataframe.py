"""DataFrame helpers for loading and understanding CSV files."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype, is_numeric_dtype


def load_csv(dataset_path: str) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""

    return pd.read_csv(dataset_path)


def detect_column_types(df: pd.DataFrame) -> dict[str, list[str]]:
    """Detect numeric, categorical, and datetime columns."""

    numerical_columns: list[str] = []
    categorical_columns: list[str] = []
    datetime_columns: list[str] = []

    for column_name in df.columns:
        series = df[column_name]
        if is_numeric_dtype(series):
            numerical_columns.append(column_name)
        elif _looks_like_datetime(series):
            datetime_columns.append(column_name)
        else:
            categorical_columns.append(column_name)

    return {
        "numerical_columns": numerical_columns,
        "categorical_columns": categorical_columns,
        "datetime_columns": datetime_columns,
    }


def build_dataset_metadata(df: pd.DataFrame, dataset_path: str) -> dict[str, Any]:
    """Build the structured metadata used by the agents and UI."""

    column_types = detect_column_types(df)
    missing_values = df.isna().sum().to_dict()

    return {
        "dataset_name": Path(dataset_path).name,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "dimensions": [int(df.shape[0]), int(df.shape[1])],
        "column_types": column_types,
        "missing_values": {column: int(count) for column, count in missing_values.items()},
        "duplicate_rows": int(df.duplicated().sum()),
    }


def _looks_like_datetime(series: pd.Series) -> bool:
    """Return True when a column appears to contain datetime values."""

    if is_datetime64_any_dtype(series):
        return True

    sample = series.dropna().astype(str).head(20)
    if sample.empty:
        return False

    parsed_values = pd.to_datetime(sample, errors="coerce")
    return float(parsed_values.notna().mean()) >= 0.8
