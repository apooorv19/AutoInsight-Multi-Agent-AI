"""Streamlit interface for AutoInsight AI."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pandas as pd
import streamlit as st

from app.graph import run_analysis
from app.tools.dataframe import load_csv

st.set_page_config(page_title="AutoInsight AI", page_icon="📊", layout="wide")


def main() -> None:
    """Render the dashboard and run the analysis workflow."""

    st.title("AutoInsight AI")
    st.caption("Multi-Agent Data Analysis Platform")

    if "analysis_result" not in st.session_state:
        st.session_state.analysis_result = None
    if "dataset_path" not in st.session_state:
        st.session_state.dataset_path = None

    with st.sidebar:
        st.header("Run Analysis")
        uploaded_file = st.file_uploader("Upload a CSV dataset", type=["csv"])
        run_button = st.button("Run Analysis", type="primary", use_container_width=True)
        st.markdown("---")
        st.write("Upload any CSV file, then click Run Analysis.")

    if run_button:
        if uploaded_file is None:
            st.sidebar.error("Please upload a CSV file first.")
        else:
            dataset_path = _save_uploaded_file(uploaded_file)
            st.session_state.dataset_path = dataset_path
            st.session_state.analysis_result = run_analysis(dataset_path)
            st.sidebar.success("Analysis complete.")

    result = st.session_state.analysis_result
    dataset_path = st.session_state.dataset_path

    if not result or not dataset_path:
        st.info("Upload a CSV file and run the analysis to see the report.")
        return

    dataframe = load_csv(dataset_path)
    metadata = result.get("metadata", {})
    statistics = result.get("statistics", {})
    plots = result.get("plots", [])
    report = result.get("report", "")
    insights = result.get("insights", "")
    warnings = result.get("warnings", [])

    if warnings:
        for warning in warnings:
            st.warning(warning)

    st.subheader("Dataset Overview")
    overview_columns = st.columns(3)
    overview_columns[0].metric("Rows", metadata.get("rows", dataframe.shape[0]))
    overview_columns[1].metric("Columns", metadata.get("columns", dataframe.shape[1]))
    overview_columns[2].metric("Duplicate Rows", metadata.get("duplicate_rows", 0))

    detail_columns = st.columns(3)
    detail_columns[0].write("**Numerical Columns**")
    detail_columns[0].write(", ".join(metadata.get("column_types", {}).get("numerical_columns", [])) or "None")
    detail_columns[1].write("**Categorical Columns**")
    detail_columns[1].write(", ".join(metadata.get("column_types", {}).get("categorical_columns", [])) or "None")
    detail_columns[2].write("**Datetime Columns**")
    detail_columns[2].write(", ".join(metadata.get("column_types", {}).get("datetime_columns", [])) or "None")

    st.write("**Preview**")
    st.dataframe(dataframe.head(10), use_container_width=True)

    st.write("**Missing Values**")
    missing_frame = pd.DataFrame(
        list(metadata.get("missing_values", {}).items()),
        columns=["Column", "Missing Count"],
    )
    st.dataframe(missing_frame, use_container_width=True, hide_index=True)

    st.subheader("Statistics")
    summary_statistics = statistics.get("summary_statistics", {})
    if summary_statistics:
        st.dataframe(pd.DataFrame.from_dict(summary_statistics, orient="index"), use_container_width=True)
    else:
        st.info("No numeric columns were available for summary statistics.")

    stats_columns = st.columns(2)
    stats_columns[0].json(
        {
            "mean": statistics.get("mean", {}),
            "median": statistics.get("median", {}),
            "standard_deviation": statistics.get("standard_deviation", {}),
        }
    )
    stats_columns[1].json(
        {
            "skewness": statistics.get("skewness", {}),
            "correlation": statistics.get("correlation", {}),
            "missing_percentage": statistics.get("missing_percentage", {}),
        }
    )

    categorical_summary = statistics.get("categorical_summary")
    if categorical_summary:
        st.write("**Categorical Summary**")
        st.dataframe(pd.DataFrame.from_dict(categorical_summary, orient="index"), use_container_width=True)

    st.subheader("Visualizations")
    if plots:
        for plot in plots:
            st.markdown(f"**{plot.get('title', 'Plot')}**")
            figure = plot.get("figure")
            if plot.get("kind") == "plotly":
                st.plotly_chart(figure, use_container_width=True)
            else:
                st.pyplot(figure, clear_figure=False, use_container_width=True)
            if plot.get("summary"):
                st.caption(plot["summary"])
    else:
        st.info("No plots were generated.")

    st.subheader("Insights")
    st.markdown(insights or "No insights were generated.")

    st.subheader("Markdown Report")
    st.download_button(
        label="Download Markdown Report",
        data=report,
        file_name="autoinsight_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
    st.text_area("Report Preview", value=report, height=500)


def _save_uploaded_file(uploaded_file: st.runtime.uploaded_file_manager.UploadedFile) -> str:
    """Persist the uploaded CSV to a temporary file."""

    outputs_dir = Path("outputs")
    outputs_dir.mkdir(exist_ok=True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv", dir=outputs_dir) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        return temp_file.name


if __name__ == "__main__":
    main()

# streamlit run frontend/streamlit_app.py