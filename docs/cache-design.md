# Cache Design

The platform treats caching as a key driver of reliability and latency. Instead
of implementing a full cache, it models cache hits and misses using a probability:

- `cache_hit_rate` in the control pipeline.
- Higher `cache_hit_rate` in the treatment pipeline.

Conceptually, this corresponds to a Redis or ElastiCache layer that stores
materialized feed responses or feed metadata.

Key points:

- Cache hits have lower latency (requests can be served faster).
- Cache misses incur higher latency and require calls to storage.
- Better cache key design, prefetching, and time-to-live (TTL) tuning can
  increase the cache hit rate.
- There is a trade-off between freshness and hit rate.

This simplified model is enough to see how changes in caching strategy affect
end-to-end latency distributions.
