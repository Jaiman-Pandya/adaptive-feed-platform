# Risks and Limitations

1. Simplified model
   - The simulator uses a simplified statistical model for latency, cache
     behavior, and errors. It does not capture all edge cases of real systems.

2. No live production traffic
   - The platform operates entirely on synthetic data. Real-world validation
     would still require controlled experiments in a live environment.

3. Assumed independence
   - Requests are modeled as independent events, while real systems may
     exhibit correlated failures or congestion.

4. Deployment assumptions
   - The AWS-aligned architecture is conceptual. Actual deployment details
     may differ depending on the infrastructure stack, scale, and team
     preferences.

Despite these limitations, the platform is useful for building intuition
around how caching and backend decisions influence reliability metrics in
a feed-oriented system.
