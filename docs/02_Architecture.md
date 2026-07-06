# 02 Architecture

## Why this file exists
This document explains the system design as a whole. It is the place to defend why the project is built as a small linear pipeline instead of an enterprise-style layered architecture.

## Architecture summary
AutoInsight AI uses a simple four-part structure:

- Streamlit frontend for user interaction
- LangGraph for orchestration
- Python tools for deterministic analysis
- Groq LLM for insight generation

## Mental model
Think of the app as a pipeline with a narrow UI at the front and a report artifact at the end.

```text
Streamlit UI
   |
   v
LangGraph workflow
   |
   +-> supervisor
   +-> data understanding
   +-> statistics
   +-> visualization
   +-> insight
   +-> report
   |
   v
Markdown report
```

## Why this architecture is appropriate
I did not build a service layer, repository layer, or dependency injection system because none of those are needed for this problem. The application is one analysis flow, not a platform.

The structure is intentionally small so it can be understood quickly:

- UI concerns stay in the frontend module
- orchestration stays in the graph module
- state stays in one typed object
- deterministic logic stays in tools
- LLM interpretation stays in one agent

## Boundaries
Each layer has a clean boundary:

- Streamlit handles interaction and display
- LangGraph handles order of execution
- agents handle workflow steps
- tools handle reusable computations
- the LLM only interprets results

## Trade-offs
The design is not optimized for massive scale or plugin-based extensibility. That is a deliberate choice. The benefit is readability, low cognitive load, and easier interview explanation.

## What makes this professional
A professional project is not automatically a complex project. In this case, professionalism comes from discipline:

- clear ownership
- small modules
- deterministic computation in Python
- controlled LLM usage
- predictable execution flow

## Relationship to other docs
- [03 Execution Flow](03_Execution_Flow.md) shows the runtime sequence
- [05 Graph](05_Graph.md) explains orchestration in detail
- [06 State](06_State.md) explains how data moves through the pipeline
