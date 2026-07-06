# 03 Execution Flow

## Why this file exists
This document explains how the application actually runs. It is useful when you need to describe the runtime sequence in an interview without getting lost in implementation details.

## Execution order
The workflow is strictly linear:

```text
Upload CSV
  -> Streamlit saves file
  -> run_analysis(dataset_path)
  -> Supervisor Agent
  -> Data Understanding Agent
  -> Statistics Agent
  -> Visualization Agent
  -> Insight Agent
  -> Report Agent
  -> return final state
```

## Step-by-step narrative
1. The user uploads a CSV in Streamlit.
2. The UI writes the file to the outputs folder and gets a path.
3. The graph receives that path inside the shared state.
4. The supervisor confirms the workflow can proceed.
5. The data agent loads the file and builds metadata.
6. The statistics agent calculates numeric summaries in Python.
7. The visualization agent builds the most useful charts and skips invalid ones.
8. The insight agent interprets the results with the LLM or a fallback summary.
9. The report agent combines everything into Markdown and saves it.
10. Streamlit renders the results and offers the report for download.

## Why this order matters
The order is deliberate. The later steps depend on the earlier steps:

- insights need metadata, statistics, and plot summaries
- the report needs everything collected earlier
- the UI should not orchestrate steps manually

That keeps the system predictable and easy to explain.

## Error behavior
The workflow is designed to continue whenever possible.

- missing dataset path -> warning
- invalid dataset path -> warning
- plot failure -> warning and skip
- missing Groq key -> fallback insight summary
- report failure -> fallback Markdown output

The main principle is simple: do not crash the analysis pipeline for recoverable issues.

## Interview framing
In an interview, I would describe this as a deterministic pipeline with one LLM-assisted interpretation stage. The important point is that the LLM is not controlling the workflow; it is only enriching the analysis at the right point.

## Related files
- [04 Streamlit](04_Streamlit.md)
- [05 Graph](05_Graph.md)
- [08 Supervisor Agent](08_Supervisor_Agent.md)
- [09 Data Agent](09_Data_Agent.md)
- [11 Statistics Agent](11_Statistics_Agent.md)
- [13 Visualization Agent](13_Visualization_Agent.md)
- [15 Insight Agent](15_Insight_Agent.md)
- [17 Report Agent](17_Report_Agent.md)
