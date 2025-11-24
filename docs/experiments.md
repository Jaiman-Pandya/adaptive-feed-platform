# Experiments

The platform is built around the idea of control and treatment pipelines.

- The control pipeline represents the current or baseline configuration.
- The treatment pipeline represents a proposed improvement, such as better
  caching, prefetching, or error-handling.

For each configuration, the simulator generates a synthetic dataset of requests,
then computes and visualizes metrics.

Example experiments:

- Increase the cache hit rate in the treatment group and measure:
  - Change in mean latency.
  - Change in p95 and p99 latency.
- Reduce the error rate in the treatment group and measure:
  - Reduction in simulated error frequency.
- Combine improved caching and error handling to see the combined impact
  relative to the control pipeline.

This experimentation style is similar to how we would validate infrastructure
changes with an A/B experiment in a real system, but without requiring a live
environment.
