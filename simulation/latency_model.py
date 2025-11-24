import numpy as np
import pandas as pd
from numpy.random import default_rng

from .cache_model import generate_cache_hits
from .error_model import generate_errors

def simulate_feed_pipeline(
    n_requests: int,
    base_latency_ms: float,
    jitter_ms: float,
    cache_hit_rate: float,
    base_error_rate: float,
    latency_reduction_factor: float = 1.0,
    error_reduction_factor: float = 1.0,
    seed: int = 42,
    cohort_name: str = "control",
) -> pd.DataFrame:
    """
    Simulate a content feed backend for a given cohort (control or treatment).

    The model captures:
    - Latency distribution with base latency and jitter
    - Cache hits vs misses (as a function of cache_hit_rate)
    - Errors (as a function of base_error_rate and error_reduction_factor)
    - Latency reduction in treatment cohorts (latency_reduction_factor)

    Parameters
    ----------
    n_requests : int
        Number of feed requests to simulate.
    base_latency_ms : float
        Baseline latency in milliseconds.
    jitter_ms : float
        Standard deviation of latency noise.
    cache_hit_rate : float
        Fraction of requests served from cache.
    base_error_rate : float
        Baseline error rate.
    latency_reduction_factor : float, optional
        Factor applied to latency in the treatment cohort. Values less than 1.0
        represent improvements.
    error_reduction_factor : float, optional
        Factor applied to error rate in the treatment cohort.
    seed : int, optional
        Seed for reproducible randomness.
    cohort_name : str, optional
        Name of the cohort (e.g., "control" or "treatment").

    Returns
    -------
    pandas.DataFrame
        A DataFrame with columns:
        - "cohort"
        - "latency_ms"
        - "cache_hit"
        - "error"
    """
    rng = default_rng(seed)

    cache_hit = generate_cache_hits(n_requests, cache_hit_rate, rng)

    # Draw base latency with noise
    latency = rng.normal(loc=base_latency_ms, scale=jitter_ms, size=n_requests)

    # Cache hits are faster; cache misses are slower
    latency = np.where(cache_hit, latency * 0.7, latency * 1.3)

    # Apply treatment latency factor
    latency = latency * latency_reduction_factor

    # Clip to a minimum latency to avoid unrealistic values
    latency = np.clip(latency, 5.0, None)

    errors = generate_errors(
        n_requests=n_requests,
        base_error_rate=base_error_rate,
        error_reduction_factor=error_reduction_factor,
        rng=rng,
    )

    df = pd.DataFrame(
        {
            "cohort": cohort_name,
            "latency_ms": latency,
            "cache_hit": cache_hit,
            "error": errors,
        }
    )

    return df
