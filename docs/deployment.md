# Deployment

This repository does not deploy a real backend. Instead, it shows how the
simulated concepts could map onto a cloud environment.

A plausible deployment strategy might include:

- CDN or edge layer for static assets and routing.
- Application service running on containers or functions:
  - Container service (for example, ECS or Kubernetes).
  - Or serverless functions (for example, Lambda).
- Redis or ElastiCache as a managed caching layer.
- A storage system for content metadata.

The Streamlit dashboard can be hosted separately as an internal tool for product
and infrastructure teams to explore simulation scenarios.

The `specs/implementation-plan.md` file describes a staged approach to rolling
out reliability improvements in a real system, starting from offline modeling
and moving toward production experiments.
