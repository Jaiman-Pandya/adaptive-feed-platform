import numpy as np
import pandas as pd


def compute_metrics(df: pd.DataFrame) -> dict:
    """
    Compute reliability metrics for a simulated cohort.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame with columns "latency_ms", "cache_hit", and "error".

    Returns
    -------
    dict
        Dictionary containing mean, p50, p95, p99 latency, error_rate, and cache_hit_ratio.
    """
    lat = df["latency_ms"]
    err = df["error"]
    hit = df["cache_hit"]

    return {
        "mean_latency_ms": float(lat.mean()),
        "p50_latency_ms": float(np.percentile(lat, 50)),
        "p95_latency_ms": float(np.percentile(lat, 95)),
        "p99_latency_ms": float(np.percentile(lat, 99)),
        "error_rate": float(err.mean()),
        "cache_hit_ratio": float(hit.mean()),
    }
