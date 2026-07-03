# Audit Log Cost Reduction

OBS-711 moved high-volume audit events into sampled storage. The ingest layer
now has durable request traces for replay, so service-local audit emission can
follow the normal sampling flag.

Update `should_record` so it records events when:

- `event["sampled"]` is true, or
- `event["level"]` is `warning` or `error`

Do not keep a service-local always-record list. The centralized audit pipeline
owns that classification now.

