# 01 Project Overview

## Why this file exists
This document gives the interview-level mental model for the whole project. It explains what AutoInsight AI does, why it exists, and how the modules fit together without diving into implementation details too early.

## What the project is
AutoInsight AI is a compact multi-agent CSV analysis platform. A user uploads a CSV file, the workflow inspects the dataset, computes statistics in Python, generates useful visualizations, asks an LLM to interpret the results, and then produces a Markdown report.

The project is intentionally small. The goal is not to build an enterprise system. The goal is to show clean thinking, clear separation of responsibilities, and practical engineering judgment.

## Core idea
The application turns a dataset into a readable analysis package:

- dataset overview
- summary statistics
- visualizations
- AI-generated insights
- markdown report

## High-level workflow

```text
Upload CSV
  -> Supervisor
  -> Data Understanding Agent
  -> Statistics Agent
  -> Visualization Agent
  -> Insight Agent
  -> Report Agent
  -> Markdown report
```

## Architectural message
The project is designed to be explainable in an interview. Every file has one job. The agents are narrow. The tools are pure helpers. The graph is linear. The UI is thin.

That makes the whole system easy to defend because the architecture follows the product requirements instead of adding extra layers.

## Key design principle
I optimized for simplicity over abstraction. If a responsibility could live in a small existing module, I kept it there. If a step did not need a separate layer, I did not add one.

## What interviewers should understand
- the app is a structured analysis pipeline, not a generic agent swarm
- Python handles deterministic work like statistics and plotting
- the LLM is only used for interpretation
- the graph is linear on purpose
- the UI is separate from the analysis logic

## Relationship to the rest of the docs
- [02 Architecture](02_Architecture.md) explains the overall structure
- [03 Execution Flow](03_Execution_Flow.md) explains the runtime sequence
- the remaining files explain each module in the exact order execution happens
