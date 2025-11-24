# Cache Hit and Miss Flow

```mermaid
sequenceDiagram
    participant Client
    participant App
    participant Cache
    participant Storage

    Client->>App: Request feed
    App->>Cache: GET cache entry
    alt Cache hit
        Cache-->>App: Cached content
        App-->>Client: Response with low latency
    else Cache miss
        Cache-->>App: MISS
        App->>Storage: Query content
        Storage-->>App: Content
        App->>Cache: SET cache entry with TTL
        App-->>Client: Response with higher latency
    end