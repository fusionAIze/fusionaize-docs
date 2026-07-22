# Configuration

fusionAIze components are configured through a combination of **YAML configuration files**, **environment variables**, and **runtime API calls**. This reference covers every configuration surface across the stack.

---

## Configuration overview

Every fusionAIze component follows the same configuration pattern:

```
~/.config/fusionaize/
├── gate.yaml          # Gate: provider routing, quotas, access control
├── lens.yaml          # Lens: compression profiles, plugins
├── fabric.yaml        # Fabric: storage backends, vector stores
├── grid.yaml          # Grid: runner profiles, resource limits
├── faios.yaml         # faios: team roles, policies, protocols
└── studio.yaml        # Studio: authoring environment settings
```

Each component also respects a `FUSIONAIZE_CONFIG_DIR` environment variable to override the default config directory.

```bash
export FUSIONAIZE_CONFIG_DIR=/etc/fusionaize
```

---

## Gate configuration

Gate is the unified AI gateway. Its configuration defines which providers are available, how requests are routed, and what governance policies apply.

### Providers

```yaml title="gate.yaml"
providers:
  - id: anthropic
    type: anthropic
    api_key_env: ANTHROPIC_API_KEY
    default_model: claude-sonnet-4-20250514
    priority: 1
    models:
      - claude-sonnet-4-20250514
      - claude-opus-4-20250514
      - claude-haiku-3-5-20241022
    rate_limit:
      requests_per_minute: 50
      tokens_per_minute: 200000

  - id: openai
    type: openai
    api_key_env: OPENAI_API_KEY
    default_model: gpt-4o
    priority: 2
    models:
      - gpt-4o
      - gpt-4o-mini
      - o4-mini
    rate_limit:
      requests_per_minute: 100
      tokens_per_minute: 500000

  - id: local-ollama
    type: openai-compatible
    base_url: http://localhost:11434/v1
    api_key: ollama
    default_model: llama3.2
    priority: 3
    models:
      - llama3.2
      - mistral
      - codellama
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique identifier for this provider |
| `type` | string | yes | Provider type: `anthropic`, `openai`, `google`, `openai-compatible` |
| `api_key_env` | string | yes | Environment variable containing the API key |
| `api_key` | string | no | Direct API key value (not recommended — use `api_key_env`) |
| `base_url` | string | no | Override the API base URL |
| `default_model` | string | no | Default model when none is specified in requests |
| `priority` | int | no | Routing priority (lower = higher preference) |
| `models` | list | no | Allow-listed models for this provider |
| `rate_limit` | object | no | Per-provider rate limiting |

### Routing

```yaml title="gate.yaml (routing)"
routing:
  strategy: priority-failover     # priority-failover | round-robin | least-latency | model-aware
  fallback_on:
    - rate_limit
    - provider_error
    - timeout
    - model_unavailable
  timeout_ms: 30000               # Per-request timeout
  retry:
    max_attempts: 3
    backoff: exponential
    initial_delay_ms: 500
```

| Strategy | Behaviour |
|----------|-----------|
| `priority-failover` | Try providers in priority order. On failure, try the next. |
| `round-robin` | Distribute requests evenly across available providers. |
| `least-latency` | Route to the provider with the lowest recent latency. |
| `model-aware` | Match the requested model to the provider that hosts it. |

### Access control

```yaml title="gate.yaml (access control)"
access:
  api_keys:
    - key_env: FUSIONAIZE_API_KEY_1
      scopes:
        - chat:read
        - chat:write
      rate_limit:
        requests_per_hour: 1000

    - key_env: FUSIONAIZE_API_KEY_2
      scopes:
        - chat:read
        - admin:read
      rate_limit:
        requests_per_hour: 10000

  oidc:
    enabled: false
    issuer: https://auth.example.com
    client_id: fusionaize-gate
    client_secret_env: OIDC_CLIENT_SECRET
```

### Cost governance

```yaml title="gate.yaml (cost governance)"
cost:
  enabled: true
  currency: USD
  budgets:
    - scope: team
      id: engineering
      monthly_limit: 5000.00
      alert_thresholds:
        - 50   # Alert at 50% of budget
        - 80   # Alert at 80% of budget
        - 95   # Alert at 95% of budget
      action_on_exhaustion: block     # block | warn | fallback-to-cheapest

    - scope: project
      id: pr-review-bot
      daily_limit: 50.00
      action_on_exhaustion: warn
```

### Audit logging

```yaml title="gate.yaml (audit)"
audit:
  enabled: true
  storage: file                    # file | postgres | elastic
  file_path: /var/log/fusionaize/gate-audit.log
  log_bodies: false                # Log request/response bodies (off by default for privacy)
  retention_days: 90
```

---

## Lens configuration

Lens manages context — compressing, focusing, and translating information before it reaches the AI model.

### Compression profiles

```yaml title="lens.yaml"
compression:
  default_profile: balanced

  profiles:
    minimal:
      strategy: extractive
      max_tokens: 4000
      preserve:
        - instructions
        - recent_messages

    balanced:
      strategy: hybrid
      max_tokens: 8000
      preserve:
        - instructions
        - recent_messages
        - key_facts
        - decisions
      summarise:
        - conversation_history

    complete:
      strategy: none               # No compression — send everything
      max_tokens: 0                # 0 = no limit (bounded by model context window)

    code_review:
      strategy: extractive
      max_tokens: 16000
      preserve:
        - code_diffs
        - review_standards
        - related_files
      summarise:
        - file_history
        - prior_reviews
```

### Relevance filtering

```yaml title="lens.yaml (relevance)"
relevance:
  enabled: true
  threshold: 0.6                   # Minimum relevance score (0.0—1.0)
  max_context_items: 20            # Maximum number of Fabric items to include
  ranking:
    strategy: hybrid               # semantic | recency | hybrid
    recency_weight: 0.3
    semantic_weight: 0.7
```

### Plugins

```yaml title="lens.yaml (plugins)"
plugins:
  - id: code-review-lens
    type: builtin
    config:
      include_tests: true
      max_files: 10

  - id: customer-support-lens
    type: builtin
    config:
      include_ticket_history: true
      include_knowledge_base: true

  - id: custom-privacy-filter
    type: external
    path: /etc/fusionaize/plugins/privacy_filter.py
    config:
      pii_patterns: true
      strip_emails: true
      strip_phone_numbers: true
```

---

## Fabric configuration

Fabric provides persistent, shared memory across all fusion team interactions.

### Storage backends

```yaml title="fabric.yaml"
storage:
  backend: postgres                # postgres | sqlite

  postgres:
    host: localhost
    port: 5432
    database: fusionaize_fabric
    user_env: FABRIC_PG_USER
    password_env: FABRIC_PG_PASSWORD
    pool_size: 20

  sqlite:
    path: /var/lib/fusionaize/fabric.db
```

### Vector store (embeddings)

```yaml title="fabric.yaml (embeddings)"
embeddings:
  provider: openai                # openai | local | huggingface
  model: text-embedding-3-small

  store:
    backend: chromadb             # chromadb | qdrant | pgvector

    chromadb:
      path: /var/lib/fusionaize/chroma
      collection: fusionaize_memory

    qdrant:
      url: http://localhost:6333
      collection: fusionaize_memory
      vector_size: 1536

    pgvector:
      host: localhost
      port: 5432
      database: fusionaize_fabric
      table: embeddings
      dimension: 1536
```

### Knowledge graph

```yaml title="fabric.yaml (knowledge graph)"
knowledge_graph:
  enabled: true
  entity_extraction:
    model: gpt-4o-mini            # Used for entity extraction from new content
    batch_size: 10
  relation_types:
    - depends_on
    - authored_by
    - references
    - implements
    - supersedes
  max_entities_per_namespace: 100000
```

### Retention

```yaml title="fabric.yaml (retention)"
retention:
  episodic_memory_days: 90        # Session histories and decision logs
  semantic_memory: permanent      # permanent | days:N
  prune_interval_hours: 24
  archive_enabled: true
  archive_backend: postgres
```

---

## Grid configuration

Grid provides the sovereign execution environment for AI agents.

### Runner profiles

```yaml title="grid.yaml"
runners:
  profiles:
    default:
      image: ghcr.io/fusionaize/runner:latest
      cpu_limit: "2"
      memory_limit: "4Gi"
      timeout_seconds: 300
      network: isolated              # isolated | host | custom
      readonly_rootfs: true
      volumes:
        - name: shared-workspace
          path: /workspace
          size: "10Gi"

    code-review:
      extends: default
      cpu_limit: "4"
      memory_limit: "8Gi"
      timeout_seconds: 600
      network: host                   # Needs to access git repositories
      environment:
        - GIT_AUTHOR_NAME=fusionAIze Code Review Agent
        - GIT_AUTHOR_EMAIL=code-review@fusionaize.local

    data-analysis:
      extends: default
      cpu_limit: "8"
      memory_limit: "16Gi"
      timeout_seconds: 1200
      volumes:
        - name: data-volume
          path: /data
          size: "50Gi"
```

### Resource pools

```yaml title="grid.yaml (resources)"
resources:
  max_concurrent_runners: 10
  max_runners_per_user: 5
  idle_timeout_seconds: 600        # Stop idle runners after 10 minutes
  image_pull_policy: IfNotPresent  # Always | IfNotPresent | Never
  registry:
    url: ghcr.io/fusionaize
    auth_env: GRID_REGISTRY_TOKEN
```

### Security boundaries

```yaml title="grid.yaml (security)"
security:
  seccomp_profile: default
  apparmor_profile: fusionaize-grid
  no_new_privileges: true
  allowed_syscalls: []              # Empty = use default seccomp profile
  network:
    egress:
      default: deny
      allow:
        - cidr: 0.0.0.0/0
          ports: [443]
          protocol: tcp
    ingress:
      default: deny
```

### Audit

```yaml title="grid.yaml (audit)"
audit:
  enabled: true
  capture_stdout: true
  capture_stderr: true
  record_filesystem_changes: true
  storage:
    backend: postgres
    retention_days: 90
```

---

## faios configuration

faios defines roles, policies, and collaboration protocols for fusion teams.

### Team roles

```yaml title="faios.yaml"
team:
  id: engineering-core
  name: Engineering Core Team

  roles:
    - id: code-reviewer
      name: Code Reviewer
      description: Reviews pull requests against team standards
      capabilities:
        - read:repository
        - read:pull_requests
        - write:review_comments
        - read:team_standards
        - read:fabric:code_patterns

    - id: documentation-writer
      name: Documentation Writer
      description: Keeps documentation synchronised with code changes
      capabilities:
        - read:repository
        - read:pull_requests
        - write:documentation
        - read:fabric:architecture_decisions

    - id: on-call-assistant
      name: On-Call Assistant
      description: Triages incidents and suggests remediation
      capabilities:
        - read:monitoring
        - read:runbooks
        - read:fabric:incident_history
        - write:incident_notes
```

### Collaboration policies

```yaml title="faios.yaml (policies)"
policies:
  - id: require-human-approval
    description: Code changes must be approved by a human before merging
    applies_to: [code-reviewer]
    rule:
      type: approval-gate
      requires: human.reviewer
      auto_approve_conditions:
        - change_type: documentation
        - change_size: trivial        # < 10 lines

  - id: incident-escalation
    description: Critical incidents must be escalated to on-call human
    applies_to: [on-call-assistant]
    rule:
      type: escalation
      conditions:
        - severity: critical
        - confidence: below-0.8
      action: notify-oncall-channel

  - id: knowledge-sharing
    description: All decisions and architectural trade-offs must be recorded in Fabric
    applies_to: [code-reviewer, documentation-writer]
    rule:
      type: fabric-writeback
      on_event: decision_made
      store_in: architecture_decisions
```

### Handover protocols

```yaml title="faios.yaml (handover)"
handover:
  on_session_end:
    summary_generation: true
    summary_format: structured
    sections:
      - decisions_made
      - open_questions
      - context_for_next_session
      - suggested_next_actions
  on_role_change:
    brief_new_role: true
    transfer_context: true
```

---

## Environment variables reference

Every configuration value that references `*_env` in the YAML can be set via environment variables. Additional global variables:

| Variable | Component | Description | Default |
|----------|-----------|-------------|---------|
| `FUSIONAIZE_CONFIG_DIR` | all | Configuration directory | `~/.config/fusionaize` |
| `FUSIONAIZE_LOG_LEVEL` | all | Logging level | `info` |
| `FUSIONAIZE_DATA_DIR` | Fabric, Grid | Persistent data directory | `~/.local/share/fusionaize` |
| `ANTHROPIC_API_KEY` | Gate | Anthropic API key | — |
| `OPENAI_API_KEY` | Gate | OpenAI API key | — |
| `GOOGLE_API_KEY` | Gate | Google Gemini API key | — |
| `GATE_LISTEN_HOST` | Gate | Bind address | `0.0.0.0` |
| `GATE_LISTEN_PORT` | Gate | Bind port | `8120` |
| `LENS_LISTEN_PORT` | Lens | Bind port | `8121` |
| `FABRIC_LISTEN_PORT` | Fabric | Bind port | `8122` |
| `GRID_LISTEN_PORT` | Grid | Bind port | `8123` |
| `FAIOS_LISTEN_PORT` | faios | Bind port | `8124` |
| `FABRIC_PG_USER` | Fabric | Postgres user | — |
| `FABRIC_PG_PASSWORD` | Fabric | Postgres password | — |
| `FABRIC_PG_HOST` | Fabric | Postgres host | `localhost` |
| `FABRIC_PG_PORT` | Fabric | Postgres port | `5432` |
| `GRID_REGISTRY_TOKEN` | Grid | Container registry auth token | — |

---

## Configuration file format

All fusionAIze configuration files use **YAML 1.2**. Key conventions:

### Environment variable references

Suffix `_env` on any configuration field tells the system to read the value from the named environment variable:

```yaml
# Resolves to the value of $ANTHROPIC_API_KEY at runtime
api_key_env: ANTHROPIC_API_KEY

# Direct value — use only for non-sensitive configuration
api_key: sk-ant-example   # Not recommended
```

### Configuration merging

When multiple configuration sources exist, they merge with this precedence:

1. Environment variables (highest)
2. `~/.config/fusionaize/<component>.yaml`
3. Component defaults (lowest)

```bash
# Override the config directory
export FUSIONAIZE_CONFIG_DIR=/etc/fusionaize

# Override a specific value
export GATE_LISTEN_PORT=9000
```

### Validation

Run configuration validation before starting any component:

```bash
# Validate a specific component's config
faigate config validate
failens config validate
faifabric config validate

# Validate the entire stack
faigate config validate --all

# Validate with verbose output
faigate config validate --verbose
```

!!! warning "Invalid configuration"
    Components will refuse to start if their configuration fails validation. Error messages include the exact YAML path of the problem and suggestions for fixing it.

---

## Example: complete minimal configuration

```yaml title="~/.config/fusionaize/gate.yaml (minimal working example)"
providers:
  - id: anthropic
    type: anthropic
    api_key_env: ANTHROPIC_API_KEY
    default_model: claude-sonnet-4-20250514
    priority: 1

  - id: openai
    type: openai
    api_key_env: OPENAI_API_KEY
    default_model: gpt-4o
    priority: 2

routing:
  strategy: priority-failover

access:
  api_keys:
    - key_env: FUSIONAIZE_API_KEY
      scopes:
        - chat:read
        - chat:write
```

This is enough to run Gate with two providers, automatic failover, and basic API key authentication. Every other configuration option is optional and defaults to sensible values.

---

## Next steps

- [Quickstart guide](index.md) — from zero to first request
- [Installation guide](install.md) — detailed per-platform installation
- [Gate documentation](../products/gate/index.md) — deep dive into the gateway
- [Platform overview](../about/platform.md) — understand the full architecture
