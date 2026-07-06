# 04 Streamlit

## Why this file exists
This document explains the Streamlit frontend as the user-facing boundary of the application. It is the place to defend why the UI is thin and what responsibilities it owns.

## File responsibility
`frontend/streamlit_app.py` owns:

- file upload
- run button handling
- session state
- display of overview, statistics, plots, insights, and report
- download of the generated Markdown file

## Why the UI is separate
The frontend should not contain the analysis logic. If the analysis lived inside Streamlit callbacks, the project would become harder to test and harder to explain. The current design keeps the UI focused on presentation and user interaction.

## Interview explanation
I would explain this file by saying that I intentionally kept the Streamlit layer thin. The UI handles upload and display, while the graph handles analysis. That separation lets me keep the workflow easy to reason about and prevents the frontend from becoming a second orchestration layer.

## Key design choices
- Session state is used because Streamlit reruns the script often.
- The uploaded CSV is saved to disk because the rest of the pipeline expects a file path.
- The analysis runs only when the button is pressed.
- Results are stored in session state so the page can re-render without recomputing immediately.

## What the user sees
The UI renders the final output in a clear sequence:

- dataset overview metrics
- data preview
- missing values
- summary statistics
- generated plots
- AI insights
- markdown report download

## Why this is interview-friendly
This file shows product thinking. It proves I understand the difference between a backend workflow and a frontend experience. It also shows I know how to keep a Streamlit app from becoming chaotic.

## Trade-offs
The only real trade-off is that the UI repeats some display logic for readability. That is acceptable because the app is small and the code is easier to explain that way.

## Related files
- [03 Execution Flow](03_Execution_Flow.md)
- [05 Graph](05_Graph.md)
- [06 State](06_State.md)
- [17 Report Agent](17_Report_Agent.md)
