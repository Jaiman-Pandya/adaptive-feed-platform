from simulation.latency_model import simulate_feed_pipeline
from simulation.metrics import compute_metrics


def test_treatment_pipeline_improves_latency_and_errors():
    n_requests = 20_000
    base_latency_ms = 220
    jitter_ms = 70
    cache_hit_rate_control = 0.5
    cache_hit_rate_treatment = 0.8
    base_error_rate = 0.03

    control_df = simulate_feed_pipeline(
        n_requests=n_requests,
        base_latency_ms=base_latency_ms,
        jitter_ms=jitter_ms,
        cache_hit_rate=cache_hit_rate_control,
        base_error_rate=base_error_rate,
        latency_reduction_factor=1.0,
        error_reduction_factor=1.0,
        seed=10,
        cohort_name="control",
    )

    treatment_df = simulate_feed_pipeline(
        n_requests=n_requests,
        base_latency_ms=base_latency_ms,
        jitter_ms=jitter_ms,
        cache_hit_rate=cache_hit_rate_treatment,
        base_error_rate=base_error_rate,
        latency_reduction_factor=0.75,
        error_reduction_factor=0.6,
        seed=11,
        cohort_name="treatment",
    )

    control_metrics = compute_metrics(control_df)
    treatment_metrics = compute_metrics(treatment_df)

    # Treatment should have:
    # - higher cache hit ratio
    # - lower mean and p95 latency
    # - lower error rate
    assert treatment_metrics["cache_hit_ratio"] > control_metrics["cache_hit_ratio"]
    assert treatment_metrics["mean_latency_ms"] < control_metrics["mean_latency_ms"]
    assert treatment_metrics["p95_latency_ms"] < control_metrics["p95_latency_ms"]
    assert treatment_metrics["error_rate"] < control_metrics["error_rate"]
