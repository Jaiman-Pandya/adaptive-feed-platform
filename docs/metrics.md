# Metrics

The simulator focuses on a small set of reliability metrics:

- Mean latency
- p50 latency
- p95 latency
- p99 latency
- Error rate
- Cache hit ratio

These are computed per cohort (control and treatment) to support direct comparison.

High-percentile latency (p95 and p99) is important, because it captures the tail
of the distribution. Even if the mean latency looks acceptable, occasional slow
responses can harm user perception of performance.

Error rate is modeled as a probability that a request fails. In reality, this
could correspond to timeouts, internal server errors, or dependency failures.

Cache hit ratio helps explain why latency may improve or degrade between
pipelines. Improvements in caching strategy should often be reflected in higher
cache hit ratios and reduced high-percentile latency.
