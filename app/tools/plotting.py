"""Plot generation helpers for the visualization agent."""

from __future__ import annotations

from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


def create_visualizations(df: pd.DataFrame, metadata: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    """Create the most useful plots for the dataset and skip invalid ones."""

    plots: list[dict[str, Any]] = []
    warnings: list[str] = []

    numerical_columns = metadata.get("column_types", {}).get("numerical_columns", [])
    categorical_columns = metadata.get("column_types", {}).get("categorical_columns", [])

    builders = [
        ("Histogram", lambda: _build_histogram(df, numerical_columns)),
        ("Boxplot", lambda: _build_boxplot(df, numerical_columns)),
        ("Correlation Heatmap", lambda: _build_correlation_heatmap(df, numerical_columns)),
        ("Bar Chart", lambda: _build_bar_chart(df, categorical_columns)),
        ("Scatter Plot", lambda: _build_scatter_plot(df, numerical_columns)),
    ]

    for _, builder in builders:
        try:
            plot = builder()
            if plot is not None:
                plots.append(plot)
        except ValueError as exc:
            warnings.append(str(exc))
        except Exception as exc:  # pragma: no cover - defensive guard for plotting edge cases.
            warnings.append(f"Plot skipped: {exc}")

    return plots, warnings


def _build_histogram(df: pd.DataFrame, numerical_columns: list[str]) -> dict[str, Any]:
    if not numerical_columns:
        raise ValueError("Histogram skipped: no numeric columns found.")

    column_name = numerical_columns[0]
    figure, axis = plt.subplots(figsize=(8, 4))
    axis.hist(df[column_name].dropna(), bins=20, color="#1f77b4", edgecolor="white")
    axis.set_title(f"Histogram of {column_name}")
    axis.set_xlabel(column_name)
    axis.set_ylabel("Frequency")
    figure.tight_layout()

    return {
        "title": f"Histogram: {column_name}",
        "kind": "matplotlib",
        "figure": figure,
        "summary": f"Distribution of {column_name}.",
    }


def _build_boxplot(df: pd.DataFrame, numerical_columns: list[str]) -> dict[str, Any]:
    if not numerical_columns:
        raise ValueError("Boxplot skipped: no numeric columns found.")

    column_name = numerical_columns[0]
    figure, axis = plt.subplots(figsize=(8, 3))
    axis.boxplot(df[column_name].dropna(), vert=False)
    axis.set_title(f"Boxplot of {column_name}")
    axis.set_xlabel(column_name)
    figure.tight_layout()

    return {
        "title": f"Boxplot: {column_name}",
        "kind": "matplotlib",
        "figure": figure,
        "summary": f"Spread and outliers for {column_name}.",
    }


def _build_correlation_heatmap(df: pd.DataFrame, numerical_columns: list[str]) -> dict[str, Any] | None:
    if len(numerical_columns) < 2:
        raise ValueError("Correlation heatmap skipped: need at least two numeric columns.")

    correlation = df[numerical_columns].corr().round(3)
    figure = go.Figure(
        data=go.Heatmap(
            z=correlation.values,
            x=correlation.columns.tolist(),
            y=correlation.index.tolist(),
            colorscale="RdBu",
            zmin=-1,
            zmax=1,
            colorbar=dict(title="Correlation"),
        )
    )
    figure.update_layout(title="Correlation Heatmap", height=500)

    return {
        "title": "Correlation Heatmap",
        "kind": "plotly",
        "figure": figure,
        "summary": "Pairwise correlations across numeric columns.",
    }


def _build_bar_chart(df: pd.DataFrame, categorical_columns: list[str]) -> dict[str, Any]:
    if not categorical_columns:
        raise ValueError("Bar chart skipped: no categorical columns found.")

    column_name = categorical_columns[0]
    counts = df[column_name].astype(str).value_counts().head(10)
    figure = go.Figure(data=go.Bar(x=counts.index.tolist(), y=counts.values.tolist()))
    figure.update_layout(title=f"Bar Chart of {column_name}", xaxis_title=column_name, yaxis_title="Count")

    return {
        "title": f"Bar Chart: {column_name}",
        "kind": "plotly",
        "figure": figure,
        "summary": f"Top categories in {column_name}.",
    }


def _build_scatter_plot(df: pd.DataFrame, numerical_columns: list[str]) -> dict[str, Any]:
    if len(numerical_columns) < 2:
        raise ValueError("Scatter plot skipped: need at least two numeric columns.")

    x_column, y_column = numerical_columns[:2]
    figure = go.Figure(
        data=go.Scatter(
            x=df[x_column],
            y=df[y_column],
            mode="markers",
            marker=dict(color="#2ca02c", opacity=0.7),
        )
    )
    figure.update_layout(title=f"Scatter Plot: {x_column} vs {y_column}", xaxis_title=x_column, yaxis_title=y_column)

    return {
        "title": f"Scatter Plot: {x_column} vs {y_column}",
        "kind": "plotly",
        "figure": figure,
        "summary": f"Relationship between {x_column} and {y_column}.",
    }
