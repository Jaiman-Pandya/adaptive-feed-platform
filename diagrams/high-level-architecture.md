# High Level Architecture

```mermaid
flowchart LR
    Client[Client application] --> CDN[CDN / edge layer]
    CDN --> LB[Load balancer]
    LB --> App[Application service]
    App --> Cache[(Redis / ElastiCache)]
    App --> Storage[(Content metadata storage)]
