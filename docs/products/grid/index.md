# faigrid — Sovereign Execution Substrate

**faigrid** is the execution substrate that runs the fusionAIze stack. It manages runner queues, secrets, observability, and recovery patterns — designed from the ground up for sovereign deployment: your hardware, your cloud, your control.

---

## What is Grid?

Every AI workflow needs somewhere to run. Grid provides that substrate — a distributed execution engine that schedules work across runners, manages secrets securely, exposes telemetry, and recovers from failures. Grid runs **anywhere**: your laptop, an on-premise server, a cloud VM, or a multi-node cluster.

```mermaid
graph TB
    subgraph "faigrid"
        Scheduler["Scheduler
        · Queue management
        · Priority dispatch
        · Load balancing"]
        Runner["Runner Pool
        · Isolated execution
        · Resource limits
        · Timeout handling"]
        Secrets["Secrets Vault
        · Encrypted at rest
        · Scoped access
        · Rotation"]
        Observe["Observability
        · Metrics (Prometheus)
        · Traces (OTEL)
        · Logs (structured)"]
        Recovery["Recovery Engine
        · Retry policies
        · Circuit breakers
        · Dead letter queues"]
        API["Control API
        · Submit jobs
        · Query status
        · Manage secrets"]
    end

    Work["Work Sources
    · faigate inference
    · failens processing
    · faifabric ingestion
    · faios workflows
    · Custom tasks"]

    Work --> API --> Scheduler --> Runner
    Secrets --> Runner
    Runner --> Observe
    Runner --> Recovery

    style Grid fill:#2563eb,color:#fff,stroke:#1d4ed8
```

---

## Key Capabilities

### Runner Architecture

Runners are the workers that execute tasks. Each runner is an isolated process or container:

```yaml title="grid.yaml — runner configuration"
runners:
  pool:
    min_size: 2
    max_size: 16
    scale_up_threshold: 0.8    # CPU utilization trigger
    scale_down_cooldown: "300s"

  default_profile:
    cpu_limit: "2"
    memory_limit: "4Gi"
    timeout: "300s"
    max_retries: 3
    isolation: "process"        # process | container | wasm

  profiles:
    - name: "inference"
      cpu_limit: "4"
      memory_limit: "16Gi"
      timeout: "600s"
      isolation: "container"
      gpu: true

    - name: "embedding"
      cpu_limit: "2"
      memory_limit: "8Gi"
      timeout: "120s"

    - name: "ingestion"
      cpu_limit: "1"
      memory_limit: "2Gi"
      timeout: "900s"
      isolation: "process"
```

**Runner lifecycle:**

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Claimed: Job dispatched
    Claimed --> Running: Job started
    Running --> Completed: Success
    Running --> Failed: Error
    Running --> Timeout: Deadline exceeded
    Failed --> Retrying: Retry policy
    Retrying --> Running: Retry attempt
    Failed --> DeadLetter: Max retries exceeded
    Timeout --> DeadLetter: No retry
    Completed --> Idle: Ready for next
    Retrying --> Idle: Max retries exceeded
    DeadLetter --> [*]
```

### Job Queues

Grid manages multiple named queues with independent scheduling:

```yaml
queues:
  - name: "inference"
    priority: 1              # Highest
    concurrency: 8
    preemption: true         # Can take over lower-priority slots

  - name: "embedding"
    priority: 2
    concurrency: 4

  - name: "ingestion"
    priority: 3
    concurrency: 2

  - name: "background"
    priority: 4              # Lowest
    concurrency: 4
    preemption: false
```

**Queue features:**

- **Priority scheduling** — high-priority jobs jump the queue
- **Concurrency limits** — cap parallel executions per queue
- **Preemption** — high-priority work can interrupt lower-priority tasks
- **Affinity** — pin queues to specific runner profiles
- **Dead letter queues** — capture failed jobs for inspection and replay

### Secrets Management

Grid includes a built-in secrets vault — encrypted at rest, scoped by access policy, with rotation support:

```yaml
secrets:
  backend: "vault"      # vault | sops | encrypted-file | kms
  encryption:
    algorithm: "aes-256-gcm"

  # Secrets can be referenced in any Grid configuration
  # via ${secrets.<path>} syntax
```

```bash
# Store a secret
grid secret set PROVIDERS_OPENAI_KEY "sk-..." \
  --scope "inference-runners" \
  --rotation "90d"

# List secrets (names only, never values)
grid secret list --scope "inference-runners"

# Rotate a secret
grid secret rotate PROVIDERS_OPENAI_KEY

# Delete a secret
grid secret delete PROVIDERS_OPENAI_KEY
```

Secrets are injected into runners as environment variables or mounted files — never logged or exposed in task payloads.

### Observability

Grid exposes comprehensive telemetry:

| Signal | Backend | Port |
|--------|---------|------|
| **Metrics** | Prometheus endpoint | `:9090/metrics` |
| **Traces** | OpenTelemetry (OTEL) | Configurable exporter |
| **Logs** | Structured JSON to stdout | Configurable level |
| **Health** | Health check endpoint | `:8082/health` |

```yaml
observability:
  metrics:
    enabled: true
    port: 9090
    path: "/metrics"

  tracing:
    enabled: true
    exporter: "otlp"         # otlp | jaeger | zipkin | none
    endpoint: "http://jaeger:4317"
    sample_rate: 0.1

  logging:
    level: "info"
    format: "json"
    redact_secrets: true
```

**Key metrics exposed:**

```
faigrid_runner_pool_size
faigrid_runners_active
faigrid_jobs_queued{queue="inference"}
faigrid_jobs_completed_total{queue,status}
faigrid_job_duration_seconds{queue,quantile}
faigrid_job_retries_total{queue}
faigrid_secrets_access_total{scope}
faigrid_scheduler_latency_seconds{quantile}
```

### Recovery Patterns

Grid implements production-grade recovery:

```yaml
recovery:
  retry:
    default_policy:
      max_attempts: 3
      backoff: "exponential"
      initial_delay: "1s"
      max_delay: "60s"

    policies:
      - name: "critical"
        max_attempts: 5
        backoff: "exponential"
        jitter: true

      - name: "best-effort"
        max_attempts: 1
        backoff: "none"

  circuit_breaker:
    enabled: true
    failure_threshold: 5       # Open after N failures
    recovery_timeout: "30s"    # Try again after

  dead_letter:
    enabled: true
    retention: "7d"
    replay_enabled: true
```

---

## Deployment Profiles

Grid is designed for four deployment profiles, scaling from a laptop to enterprise clusters:

```mermaid
graph TB
    subgraph Solo["Solo — Laptop"]
        S1["Embedded runner
        SQLite metadata
        Local filesystem
        Zero dependencies"]
    end

    subgraph SmallTeam["Small Team — Single Server"]
        ST1["Process runners
        PostgreSQL
        Shared filesystem
        Docker Compose"]
    end

    subgraph SMB["SMB — Dedicated Infra"]
        SMB1["Container runners
        PostgreSQL + Redis
        S3/MinIO artifacts
        Kubernetes (single cluster)"]
    end

    subgraph Enterprise["Enterprise — Multi-Cluster"]
        E1["Container + WASM runners
        PostgreSQL cluster
        Vault + KMS
        Kubernetes (multi-cluster)
        Federated scheduling"]
    end

    style Solo fill:#22c55e,color:#000
    style SmallTeam fill:#3b82f6,color:#fff
    style SMB fill:#8b5cf6,color:#fff
    style Enterprise fill:#ef4444,color:#fff
```

### Solo

```yaml title="solo.yaml"
deployment:
  profile: "solo"
  storage:
    type: "sqlite"
    path: "./data/grid.db"
  runners:
    pool:
      min_size: 0
      max_size: 4
    profiles:
      - name: "default"
        isolation: "process"
```

Start Grid embedded in your process:

```bash
# Run Grid as part of your app — no separate service
faigrid embedded --config solo.yaml
```

### Small Team

```yaml title="small-team.yaml"
deployment:
  profile: "small-team"
  storage:
    type: "postgres"
    dsn: "postgres://grid:password@localhost:5432/grid"
  runners:
    pool:
      min_size: 1
      max_size: 8
```

```bash
# Docker Compose
docker compose -f grid-small-team.yaml up -d
```

### SMB

```yaml title="smb.yaml"
deployment:
  profile: "smb"
  storage:
    type: "postgres"
    dsn: "${GRID_DSN}"
  runners:
    pool:
      min_size: 2
      max_size: 32
      isolation: "container"
  secrets:
    backend: "vault"
    vault_addr: "${VAULT_ADDR}"
  observability:
    metrics:
      enabled: true
    tracing:
      enabled: true
```

### Enterprise

```yaml title="enterprise.yaml"
deployment:
  profile: "enterprise"
  cluster:
    mode: "federated"
    regions:
      - name: "eu-west"
        scheduler: "grid-scheduler-eu.example.com"
      - name: "us-east"
        scheduler: "grid-scheduler-us.example.com"

  storage:
    type: "postgres"
    primary: "pg-primary.internal"
    replicas: ["pg-replica-1.internal", "pg-replica-2.internal"]

  runners:
    pool:
      min_size: 4
      max_size: 256
      auto_scaling: true
      isolation: "container"

  secrets:
    backend: "vault"
    kms: "aws-kms"

  observability:
    metrics:
      enabled: true
      remote_write: "https://thanos-receive.internal"
    tracing:
      enabled: true
      sample_rate: 1.0
```

---

## On-Premise & Local Deployment

Grid is designed for **sovereign operation**. All data, all execution, all secrets — stay on your infrastructure:

```bash
# Run entirely locally
faigrid serve --profile solo --data-dir ./grid-data

# On-premise server
faigrid serve --profile small-team --config /etc/grid/grid.yaml

# Air-gapped deployment
faigrid serve --profile solo --no-telemetry --offline-mode
```

!!! important "Sovereignty"
    Grid never phones home. No telemetry is sent to fusionAIze or any third party unless you explicitly configure an exporter. Grid is designed for **air-gapped** and **regulated** environments from day one.

**Nexus lineage:** Grid evolved from the Nexus project — a distributed AI execution platform. It inherits Nexus's proven scheduling patterns and recovery semantics, refined for the fusionAIze stack.

---

## Quickstart

### 1. Install

```bash
npm install -g @fusionaize/faigrid

# Docker
docker pull fusionaize/faigrid:latest
```

### 2. Start Grid

```bash
# Minimal — solo profile, everything local
faigrid serve --profile solo

# With config
faigrid serve --config grid.yaml
```

### 3. Submit a Job

```bash
# Submit via CLI
grid submit --queue inference --payload '{
  "type": "chat_completion",
  "provider": "openai",
  "model": "gpt-4o-mini",
  "messages": [{"role": "user", "content": "Hello"}]
}'

# Submit via API
curl -X POST http://localhost:8082/v1/jobs \
  -H "Content-Type: application/json" \
  -d '{
    "queue": "inference",
    "payload": {
      "type": "chat_completion",
      "model": "gpt-4o-mini",
      "messages": [{"role": "user", "content": "Hello"}]
    }
  }'
```

### 4. Check Status

```bash
# Job status
grid status --job-id job_a1b2c3d4

# Queue depth
grid queues

# Runner health
grid runners

# Secrets list
grid secret list
```

### 5. Observe

```bash
# Metrics endpoint
curl http://localhost:9090/metrics

# Health check
curl http://localhost:8082/health
```

```json
{
  "status": "healthy",
  "profile": "solo",
  "uptime_seconds": 12470,
  "runners": {
    "total": 2,
    "active": 0,
    "idle": 2
  },
  "queues": {
    "inference": { "depth": 0, "processed": 847 },
    "embedding": { "depth": 0, "processed": 312 },
    "ingestion": { "depth": 3, "processed": 128 }
  },
  "storage": "sqlite",
  "version": "1.0.0"
}
```

---

## Integration with the Stack

| Product | How Grid serves it |
|---------|--------------------|
| **faigate** | Grid runners execute model inference, especially for local/self-hosted models. Gate delegates embedding and chat tasks to Grid queues. |
| **failens** | Lens compression and filtering tasks run on Grid runners, parallelizing across available capacity. |
| **faifabric** | Fabric ingestion pipelines and embedding generation are scheduled as Grid jobs. Long-running ingestion runs on dedicated queues. |
| **faios** | OS workflow execution — multi-step agent tasks, approval chains, scheduled operations — all run on Grid. |
