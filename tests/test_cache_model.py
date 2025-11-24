import numpy as np
from numpy.random import default_rng

from simulation.cache_model import generate_cache_hits

def test_generate_cache_hits_length_and_type():
    rng = default_rng(0)
    n_requests = 1000
    hits = generate_cache_hits(n_requests, cache_hit_rate=0.6, rng=rng)

    assert len(hits) == n_requests
    assert hits.dtype == bool

def test_generate_cache_hits_respects_probability():
    rng = default_rng(1)
    n_requests = 10_000
    target_rate = 0.7
    hits = generate_cache_hits(n_requests, cache_hit_rate=target_rate, rng=rng)

    empirical_rate = hits.mean()
    # allows a small tolerance around the target probability
    assert abs(empirical_rate - target_rate) < 0.03
