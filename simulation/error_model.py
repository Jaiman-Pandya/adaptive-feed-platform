import numpy as np
from numpy.random import Generator


def generate_errors(
    n_requests: int,
    base_error_rate: float,
    error_reduction_factor: float,
    rng: Generator,
):
    """
    Generate a boolean array indicating which requests result in errors.

    Parameters
    ----------
    n_requests : int
        Number of requests to simulate.
    base_error_rate : float
        Baseline error rate in the control pipeline.
    error_reduction_factor : float
        Factor applied to the error rate in the treatment pipeline.
        Values less than 1.0 represent improvements.
    rng : numpy.random.Generator
        Random number generator for reproducibility.

    Returns
    -------
    numpy.ndarray of bool
        True where the request results in an error, False otherwise.
    """
    effective_error_rate = base_error_rate * error_reduction_factor
    return rng.random(n_requests) < effective_error_rate
