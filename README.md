# Adaptive Feed Reliability Platform

The Adaptive Feed Reliability Platform is a simulator and dashboard for studying how
caching, prefetching, and error-handling strategies affect reliability in a content
feed backend.

The project is split into the following:

- `simulation/` – Python modules for latency, cache, error, and metrics modeling.
- `dashboard/` – A Streamlit app that exposes interactive controls and visualizations.
- `docs/` – Conceptual documentation on architecture, caching design, experiments, metrics, and deployment.
- `diagrams/` – Mermaid-based diagrams for architecture and data flow.
- `specs/` – Requirements, implementation plan, and risk analysis.

## Quick Start

```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
