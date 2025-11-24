import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd
import streamlit as st

from simulation import simulate_feed_pipeline, compute_metrics

def format_percent(x: float) -> str:
    return f"{x * 100:.2f}%"


st.set_page_config(
    page_title="Adaptive Feed Reliability Platform",
    layout="wide",
)

st.title("Adaptive Feed Reliability Platform")

st.markdown(
    """
This dashboard simulates how a content feed backend behaves under different caching,
prefetching, and error-handling strategies. It compares a baseline pipeline
(control) with an improved pipeline (treatment) and shows how reliability metrics
change between the two.
"""
)

with st.sidebar:
    st.header("Simulation configuration")

    n_requests = st.slider(
        "Requests per cohort",
        min_value=1000,
        max_value=50000,
        value=10000,
        step=1000,
    )

    st.subheader("Baseline pipeline (control)")
    base_latency_ms = st.slider(
        "Base latency (ms)",
        min_value=50,
        max_value=400,
        value=200,
        step=10,
    )
    jitter_ms = st.slider(
        "Latency jitter (ms)",
        min_value=5,
        max_value=200,
        value=60,
        step=5,
    )
    cache_hit_rate_control = st.slider(
        "Cache hit rate (control)",
        min_value=0.0,
        max_value=1.0,
        value=0.55,
        step=0.05,
    )
    error_rate_control = st.slider(
        "Error rate (control)",
        min_value=0.0,
        max_value=0.1,
        value=0.02,
        step=0.005,
    )

    st.subheader("Improved pipeline (treatment)")
    latency_reduction_factor = st.slider(
        "Latency reduction factor",
        min_value=0.4,
        max_value=1.0,
        value=0.75,
        step=0.05,
        help="Factor applied to latency in the treatment pipeline "
             "(values below 1.0 indicate lower latency).",
    )
    cache_hit_rate_treatment = st.slider(
        "Cache hit rate (treatment)",
        min_value=0.0,
        max_value=1.0,
        value=0.80,
        step=0.05,
    )
    error_reduction_factor = st.slider(
        "Error reduction factor",
        min_value=0.2,
        max_value=1.0,
        value=0.7,
        step=0.05,
        help="Factor applied to error rate in the treatment pipeline "
             "(values below 1.0 indicate fewer errors).",
    )

    seed = st.number_input(
        "Random seed",
        min_value=0,
        max_value=10_000_000,
        value=42,
        step=1,
    )

# Simulate control and treatment cohorts
control_df = simulate_feed_pipeline(
    n_requests=n_requests,
    base_latency_ms=base_latency_ms,
    jitter_ms=jitter_ms,
    cache_hit_rate=cache_hit_rate_control,
    base_error_rate=error_rate_control,
    latency_reduction_factor=1.0,
    error_reduction_factor=1.0,
    seed=seed,
    cohort_name="control",
)

treatment_df = simulate_feed_pipeline(
    n_requests=n_requests,
    base_latency_ms=base_latency_ms,
    jitter_ms=jitter_ms,
    cache_hit_rate=cache_hit_rate_treatment,
    base_error_rate=error_rate_control,
    latency_reduction_factor=latency_reduction_factor,
    error_reduction_factor=error_reduction_factor,
    seed=seed + 1,
    cohort_name="treatment",
)

control_metrics = compute_metrics(control_df)
treatment_metrics = compute_metrics(treatment_df)

st.subheader("Summary metrics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Control")
    st.write(
        {
            "mean_latency_ms": round(control_metrics["mean_latency_ms"], 2),
            "p50_latency_ms": round(control_metrics["p50_latency_ms"], 2),
            "p95_latency_ms": round(control_metrics["p95_latency_ms"], 2),
            "p99_latency_ms": round(control_metrics["p99_latency_ms"], 2),
            "error_rate": format_percent(control_metrics["error_rate"]),
            "cache_hit_ratio": format_percent(control_metrics["cache_hit_ratio"]),
        }
    )

with col2:
    st.markdown("#### Treatment")
    st.write(
        {
            "mean_latency_ms": round(treatment_metrics["mean_latency_ms"], 2),
            "p50_latency_ms": round(treatment_metrics["p50_latency_ms"], 2),
            "p95_latency_ms": round(treatment_metrics["p95_latency_ms"], 2),
            "p99_latency_ms": round(treatment_metrics["p99_latency_ms"], 2),
            "error_rate": format_percent(treatment_metrics["error_rate"]),
            "cache_hit_ratio": format_percent(treatment_metrics["cache_hit_ratio"]),
        }
    )

st.markdown("---")

st.subheader("Latency distributions")

lat_col1, lat_col2 = st.columns(2)

with lat_col1:
    st.markdown("#### Control latency (ms)")
    st.bar_chart(control_df["latency_ms"])

with lat_col2:
    st.markdown("#### Treatment latency (ms)")
    st.bar_chart(treatment_df["latency_ms"])

st.markdown("---")

st.subheader("Error rate and cache behavior")

summary = pd.DataFrame(
    {
        "cohort": ["control", "treatment"],
        "error_rate": [
            control_metrics["error_rate"],
            treatment_metrics["error_rate"],
        ],
        "cache_hit_ratio": [
            control_metrics["cache_hit_ratio"],
            treatment_metrics["cache_hit_ratio"],
        ],
    }
).set_index("cohort")

err_col, cache_col = st.columns(2)

with err_col:
    st.markdown("#### Error rate")
    st.bar_chart(summary[["error_rate"]])

with cache_col:
    st.markdown("#### Cache hit ratio")
    st.bar_chart(summary[["cache_hit_ratio"]])
