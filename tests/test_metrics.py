import pandas as pd
from simulation.metrics import compute_metrics

def test_compute_metrics_shapes():
    df = pd.DataFrame(
        {
            "latency_ms": [100, 200, 300],
            "cache_hit": [True, False, True],
            "error": [False, False, True],
        }
    )
    metrics = compute_metrics(df)
    expected_keys = {
        "mean_latency_ms",
        "p50_latency_ms",
        "p95_latency_ms",
        "p99_latency_ms",
        "error_rate",
        "cache_hit_ratio",
    }
    assert expected_keys == set(metrics.keys())
