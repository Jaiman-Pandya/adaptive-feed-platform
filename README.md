# Adaptive Feed Reliability Platform

The Adaptive Feed Reliability Platform is a simulation toolkit for modeling how caching behavior, latency variance, and backend error rates affect the performance of a large-scale content feed. It provides a reproducible, metrics-driven environment for evaluating control versus treatment pipelines and understanding how reliability strategies influence p50, p95, and p99 latency.

This repository is structured like an infrastructure product engineering project, including simulation modules, documentation, diagrams, specifications, and a full test suite.

---

## Objectives

- Model realistic feed-request behavior with controllable latency, jitter, caching, and error probabilities  
- Compare control and treatment configurations under identical traffic profiles  
- Quantify reliability metrics such as mean latency, percentiles, cache-hit ratio, and error rate  
- Provide distribution-level analysis instead of relying only on averages  
- Maintain documentation that follows infrastructure product conventions  

---

## Repository Structure

```
adaptive-feed-platform/
│
├── diagrams/
│   ├── cache-hit-flow.md
│   ├── control-vs-treatment.md
│   └── high-level-architecture.md
│
├── docs/
│   ├── architecture.md
│   ├── cache-design.md
│   ├── deployment.md
│   ├── experiments.md
│   ├── metrics.md
│   └── overview.md
│
├── simulation/
│   ├── __init__.py
│   ├── cache_model.py
│   ├── error_model.py
│   ├── latency_model.py
│   └── metrics.py
│
├── specs/
│   ├── implementation-plan.md
│   ├── requirements.md
│   └── risks.md
│
├── tests/
│   ├── test_cache_model.py
│   ├── test_error_model.py
│   ├── test_integration_control_versus_treatment.py
│   └── test_metrics.py
│
├── .gitignore
├── LICENSE
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<username>/adaptive-feed-platform.git
cd adaptive-feed-platform
```

### Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Simulation

The entrypoint is `main.py`. It constructs control and treatment cohorts using the simulation modules and computes performance metrics.

### Run with default settings

```bash
python main.py
```

### View available command-line arguments

```bash
python main.py --help
```

### Example: Custom configuration

```bash
python main.py \
  --requests 20000 \
  --control-cache-hit 0.65 \
  --treatment-cache-hit 0.82 \
  --control-error-rate 0.03 \
  --treatment-error-rate 0.01 \
  --latency-mean 120 \
  --latency-jitter 40 \
  --seed 42
```

---

## Program Usage

```python
from simulation.latency_model import generate_latency
from simulation.cache_model import generate_cache_hits
from simulation.error_model import generate_errors
from simulation.metrics import compute_metrics

lat = generate_latency(n_requests=10000, base_mean_ms=120, jitter_ms=30, seed=1)
hits = generate_cache_hits(n_requests=10000, hit_ratio=0.75, seed=1)
errs = generate_errors(n_requests=10000, error_rate=0.02, seed=1)

summary = compute_metrics(lat, hits, errs)
print(summary)
```

---

## Documentation

Documentation is located in the `docs/` directory. Recommended reading order:

1. `docs/overview.md`  
2. `docs/architecture.md`  
3. `docs/metrics.md`  
4. `docs/cache-design.md`  
5. `docs/experiments.md`  
6. `docs/deployment.md`

These documents cover architecture, caching strategy, experiment structures, metric definitions, and deployment considerations.

---

## Diagrams

The `diagrams/` directory contains Mermaid-based diagrams for:

- Cache hit and miss flow  
- Control versus treatment pipelines  
- High-level architecture  

These can be embedded into GitHub or external documentation.

---

## Specifications

The `specs/` directory contains:

- `requirements.md`  
- `implementation-plan.md`  
- `risks.md`  

These files mirror product and infrastructure planning documents.

---

## Tests

Run all tests:

```bash
pytest tests/
```

The test suite validates:

- Cache model behavior  
- Error model behavior  
- Latency generation  
- Metric calculations  
- Control vs. treatment integration  

---

## Example Use Cases

- Evaluating effects of increased cache-hit ratio on tail latency  
- Measuring error-rate reductions  
- Studying sensitivity to latency jitter  
- Simulating traffic scaling impacts  
- Prototyping reliability improvements before live A/B testing  

---

## Extending the Platform

To extend functionality:

1. Add or modify modules in `simulation/`  
2. Add corresponding tests in `tests/`  
3. Update documentation in `docs/`  
4. Update diagrams as needed in `diagrams/`  
5. Update specifications in `specs/` if design assumptions change  

---

Made with ❤️ by Jaiman Pandya

