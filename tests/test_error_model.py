import numpy as np
from numpy.random import default_rng

from simulation.error_model import generate_errors


def test_generate_errors_length_and_type():
    rng = default_rng(0)
    n_requests = 500
    errors = generate_errors(
        n_requests=n_requests,
        base_error_rate=0.05,
        error_reduction_factor=1.0,
        rng=rng,
    )

    assert len(errors) == n_requests
    assert errors.dtype == bool


def test_error_reduction_factor_reduces_errors():
    n_requests = 50_000
    base_error_rate = 0.05
    rng1 = default_rng(1)
    rng2 = default_rng(1)  # same seed so underlying randomness is comparable

    errors_control = generate_errors(
        n_requests=n_requests,
        base_error_rate=base_error_rate,
        error_reduction_factor=1.0,
        rng=rng1,
    )

    errors_treatment = generate_errors(
        n_requests=n_requests,
        base_error_rate=base_error_rate,
        error_reduction_factor=0.5,
        rng=rng2,
    )

    control_rate = errors_control.mean()
    treatment_rate = errors_treatment.mean()

    # Treatment should have lower empirical error rate
    assert treatment_rate < control_rate
    # And both should be reasonably close to their theoretical values
    assert abs(control_rate - base_error_rate) < 0.01
    assert abs(treatment_rate - (base_error_rate * 0.5)) < 0.01
