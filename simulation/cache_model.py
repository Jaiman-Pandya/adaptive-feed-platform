import numpy as np
from numpy.random import Generator


def generate_cache_hits(
    n_requests: int,
    cache_hit_rate: float,
    rng: Generator,
):
    """
    Generates a boolean array indicating which requests are successful cache hits.

    Parameters
    ----------
    n_requests : int
        Number of requests to simulate.
    cache_hit_rate : float
        Probability that a given request is served from cache.
    rng : numpy.random.Generator
        Random number generator for reproducibility.

    Returns
    -------
    numpy.ndarray of bool
        True where the request is a cache hit, False otherwise.
    """
    return rng.random(n_requests) < cache_hit_rate
