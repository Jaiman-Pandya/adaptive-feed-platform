# Control Versus Treatment Comparison
```mermaid
flowchart LR
    A[Incoming requests] --> C1[Control pipeline]
    A --> T1[Treatment pipeline]

    C1 --> C2[Baseline caching and error behavior]
    T1 --> T2[Improved caching and error handling]

    C2 --> CM[Control metrics]
    T2 --> TM[Treatment metrics]
