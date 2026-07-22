# Stack Integration

**How the fusionAIze components form a coherent pipeline — from request to execution to insight.**

---

## The Core Pipeline

The fusionAIze stack processes every interaction through a four-stage
pipeline: **Gate → Lens → Fabric → Grid**. Each stage adds a specific
capability, and the output of one feeds the input of the next.

```mermaid
flowchart LR
    subgraph "Gate"
        direction TB
        AUTH[Authentication]
        ROUTE[Routing]
        POLICY[Policy Enforcement]
    end

    subgraph "Lens"
        direction TB
        COMPRESS[Compress]
        TRANSLATE[Translate]
        FOCUS[Focus]
    end

    subgraph "Fabric"
        direction TB
        RETRIEVE[Retrieve]
        RANK[Rank]
        STORE[Store]
    end

    subgraph "Grid"
        direction TB
        ISOLATE[Isolate]
        EXECUTE[Execute]
        TOOLS[Tool Access]
    end

    Request --> Gate --> Lens --> Fabric --> Grid --> Response

    Gate -.-> OS
    Grid -.-> OS
    Gate -.-> Signal
    Grid -.-> Signal
```

While the pipeline is sequential, OS and Signal operate **orthogonally**
— OS provides the identity and policy fabric, and Signal observes
everything.

---

## Stage 1: Gate — The Entry Point

Gate is the **single entry point** for all external interactions with the
fusionAIze stack. Every request — whether from a human user, an API client,
or another service — passes through Gate.

### Gate's Responsibilities in the Pipeline

1. **Authenticate** the caller against OS identity providers.
2. **Authorize** the request against role-based policies.
3. **Route** the request to the appropriate AI provider (cloud or local).
4. **Enforce** rate limits, quotas, and cost caps.
5. **Transform** the response into a standard format.

```yaml
# Example Gate routing configuration
routes:
  primary:
    providers:
      - name: anthropic-claude
        weight: 70
        models: [claude-3-opus, claude-3-sonnet]
      - name: openai-gpt4
        weight: 30
        models: [gpt-4o]
    failover:
      - name: local-llama
        models: [llama-3-70b]
    constraints:
      max_latency_ms: 5000
      max_cost_per_1k_tokens: 0.03
```

### What Gate Passes Forward

After processing, Gate forwards a **normalized request** downstream:

```json
{
  "caller": {
    "identity": "role:customer-support-agent-01",
    "scopes": ["chat:invoke", "memory:read", "tool:email:draft"]
  },
  "request": {
    "prompt": "Customer asks about refund policy for order #1234...",
    "max_tokens": 500,
    "temperature": 0.7
  },
  "context": {
    "conversation_id": "conv_abc123",
    "thread_history": []
  }
}
```

---

## Stage 2: Lens — Context Optimization

Lens receives the normalized request from Gate and optimizes the context
window. Its goal is to **maximize useful information per token**.

### Lens Processing Steps

```mermaid
flowchart TB
    IN[Raw Request + History] --> COMPRESS[Compress Thread History]
    COMPRESS --> RETRIEVE[Query Fabric for Relevant Memory]
    RETRIEVE --> FOCUS[Focus on Task-Relevant Context]
    FOCUS --> ASSEMBLE[Assemble Optimized Prompt]
    ASSEMBLE --> OUT[Optimized Prompt to Gate]
```

1. **Compress** — reduce thread history by summarizing or truncating
   older messages while preserving key facts and decisions.
2. **Retrieve** — query Fabric for stored memories, knowledge, and facts
   relevant to the current task.
3. **Focus** — prioritize context based on relevance, recency, and task
   requirements. Deprioritize or drop irrelevant context.
4. **Assemble** — build the final prompt struct with system instructions,
   retrieved memory, compressed history, and the current query — all
   within the token budget.

### What Lens Produces

```json
{
  "token_budget": {
    "total": 8000,
    "system_instructions": 500,
    "retrieved_memory": 1200,
    "compressed_history": 800,
    "current_query": 150,
    "reserved_for_response": 1000,
    "remaining": 4350
  },
  "retrieved_chunks": [
    {
      "content": "Refund policy: 30-day return window...",
      "source": "knowledge_base/refund_policy",
      "score": 0.94
    }
  ]
}
```

---

## Stage 3: Fabric — Memory Retrieval and Storage

Fabric is Lens's **memory backend**. It stores, indexes, and retrieves
structured memories, knowledge, and facts.

### Fabric's Role in the Pipeline

During context assembly, Lens calls Fabric with:

```json
{
  "query": "refund policy order shipping damage",
  "top_k": 5,
  "filters": {
    "source_type": ["knowledge_base", "policy_doc"],
    "recency": "90d"
  }
}
```

Fabric returns ranked results with relevance scores:

```json
{
  "results": [
    {
      "id": "mem_789",
      "content": "Returns accepted within 30 days. Shipping damage...",
      "metadata": {
        "source": "refund_policy_v3",
        "last_updated": "2024-11-15"
      },
      "score": 0.94
    }
  ],
  "query_time_ms": 12
}
```

### Post-Execution Memory Storage

After Grid finishes execution, new memories flow back to Fabric:

```mermaid
flowchart LR
    GR[Grid Execution Complete] --> MEM[Memory Extraction]
    MEM --> EMB[Embedding]
    EMB --> DEDUP[Deduplication Check]
    DEDUP --> INDEX[Index Update]
    INDEX --> STORE[(Vector Store)]
```

---

## Stage 4: Grid — Execution Foundation

Grid is the **execution substrate** where virtual employees run. It
provides isolated sandboxes, tool access, and lifecycle management.

### Grid's Responsibilities

1. **Isolation** — each execution runs in its own sandbox (container,
   microVM, or namespace).
2. **Tool access** — a controlled bridge between the sandbox and
   external tools (email, Slack, APIs, databases).
3. **Lifecycle** — start, pause, resume, and terminate execution sessions.
4. **Constraints** — enforce the role's constraint policies during
   execution.

```mermaid
flowchart TB
    subgraph "Grid Node"
        S1[Sandbox 1<br>CS Agent]
        S2[Sandbox 2<br>Data Analyst]
        S3[Sandbox 3<br>Code Reviewer]

        TB[Tool Bridge]
        LB[Lifecycle Manager]
        CB[Constraint Enforcer]
    end

    subgraph "External Tools"
        EMAIL[Email API]
        SLACK[Slack API]
        CRM[CRM System]
        DB[Database]
    end

    S1 --> CB
    S2 --> CB
    S3 --> CB
    CB --> TB
    TB --> EMAIL
    TB --> SLACK
    TB --> CRM
    TB --> DB

    LB --> S1
    LB --> S2
    LB --> S3
```

### Execution Lifecycle

```
Request arrives → Grid allocates sandbox → loads role blueprint
→ binds tool permissions → executes → emits telemetry → stores memory → responds
```

??? example "Grid Execution Example"
    ```json
    {
      "execution_id": "exec_456",
      "role": "customer-support-agent-01",
      "sandbox": {
        "type": "container",
        "image": "fusionaize/grid-runner:latest",
        "isolation": "process+network"
      },
      "tool_grants": [
        {
          "tool": "email:send_draft",
          "constraint": "require_approval",
          "scope": ["support@example.com"]
        },
        {
          "tool": "knowledge_base:search",
          "constraint": "read_only",
          "scope": ["product_docs", "refund_policies"]
        }
      ],
      "status": "running"
    }
    ```

---

## OS — Team Orchestration Layer

OS operates transversely across the pipeline, providing **identity,
policy, and collaboration** services:

```mermaid
flowchart TB
    subgraph OS
        ID[Identity Service]
        RB[Role Bindings]
        POL[Policy Engine]
        COL[Collaboration Events]
    end

    subgraph "fusionAIze Stack"
        G[Gate]
        GR[Grid]
    end

    ID --> G
    ID --> GR
    RB --> G
    RB --> GR
    POL --> G
    POL --> GR
    COL --> G
```

### OS Integration Points

| Integration | What OS Provides | Used By |
|-------------|-----------------|---------|
| Authentication | Token validation, identity resolution | Gate |
| Authorization | Role-based access control, scope validation | Gate, Grid |
| Role definitions | Virtual employee identity and constraints | Grid |
| Policy enforcement | Rate limits, quotas, access policies | Gate, Grid |
| Collaboration | Handoff events, escalation paths, approvals | Grid |

---

## Integration Patterns

### Pattern 1: Direct HTTP (REST)

Used between components in the same network (low latency, strong typing):

```
Client → Gate → Lens → Fabric
                  Gate → Grid
```

OpenAPI specs in the SDK's `contracts/` directory define these interfaces.

### Pattern 2: gRPC Streaming

Used for high-throughput, streaming communication:

```
Grid ← → Fabric (memory streaming)
Gate ← → Lens (context streaming)
Signal ← → All (metrics streaming)
```

Protobuf definitions in `contracts/proto/` define these interfaces.

### Pattern 3: Message Queue (Async)

Used for fire-and-forget, event-driven communication:

```
Grid → [MQ] → Fabric (memory ingestion)
All → [MQ] → Signal (telemetry collection)
```

The message queue is the **event backbone** of the stack. Every component
emits structured events to a shared topic. Signal consumes all topics.
Fabric consumes memory-related topics. Other components subscribe as
needed.

### Pattern 4: Sidecar Proxy

For deployments where co-location matters:

```yaml
# docker-compose fragment
services:
  grid-runner:
    image: fusionaize/grid-runner:latest
    depends_on:
      - signal-collector  # sidecar

  signal-collector:
    image: fusionaize/signal-collector:latest
    network_mode: "service:grid-runner"
    volumes:
      - ./config/signal-collector.yml:/etc/signal/config.yml
```

The Signal collector runs as a sidecar on the same network namespace,
capturing local metrics without exposing endpoints externally.

---

## Complete Integration Example

A virtual employee answering a customer query end-to-end:

```mermaid
sequenceDiagram
    participant C as Customer
    participant G as Gate
    participant L as Lens
    participant F as Fabric
    participant GR as Grid
    participant E as Email API

    C->>G: "Where is my order #1234?"
    G->>G: Auth (OS Identity)
    G->>G: Policy check (rate limit, quota)
    G->>L: Optimize context
    L->>F: Retrieve order + shipping policies
    F-->>L: Relevant memories
    L-->>G: Optimized prompt
    G->>G: Route to provider
    G-->>C: "Your order shipped yesterday. Tracking: ..."
    G->>GR: Post-execution: log memory, update tracking
    GR->>F: Store conversation memory
    GR->>E: Send tracking email (if role policy allows)
    G->>G: Emit telemetry to Signal
```

---

## Key Design Constraints

1. **Every request goes through Gate.** No component is externally
   accessible except through Gate. This ensures consistent authentication,
   authorization, and auditing.

2. **Memory flows through Fabric.** No component stores persistent state
   independently. Fabric is the single source of truth for knowledge and
   memory.

3. **Execution happens on Grid.** Virtual employees never run in-process
   inside Gate or any other component. Grid provides the isolation
   boundary.

4. **Telemetry goes to Signal.** Every component emits structured
   telemetry to Signal's collectors. There are no side-channels for
   observability.

5. **OS governs identity and policy.** No component makes authorization
   decisions independently. OS is the authoritative source for who can
   do what.

6. **Contracts are the boundaries.** Components communicate only through
   typed, versioned contracts. There is no shared database, no direct
   filesystem access between components, and no implicit coupling.
