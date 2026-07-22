# SDK — Integration Layer

**Build on fusionAIze with shared clients, contracts, and tooling.**

---

## What is the SDK?

The fusionAIze SDK (`fusionaize-sdk`) is the **shared client, contract,
and integration layer** for the entire fusionAIze stack. It provides
typed clients, interface definitions, and development tooling that let
you integrate with Gate, Lens, Fabric, Grid, OS, Signal, and Studio
from any TypeScript or Python application.

The SDK is a **monorepo** following the `@fusionaize/*` package
convention for TypeScript and a mirrored `fusionaize.*` module
structure for Python.

---

## Why a Shared SDK?

Without a unified SDK, every integration with the stack reinvents:

- **Authentication** — token management, refresh logic, scope handling.
- **Serialization** — request/response formats, error types, pagination.
- **Typing** — TypeScript interfaces and Python type stubs drift apart.
- **Contracts** — breaking API changes are discovered in production.

The SDK solves this by providing a **single source of truth** for client
interfaces, maintained alongside the services themselves.

---

## Package Structure

### TypeScript (`packages/`)

```
fusionaize-sdk/
├── packages/
│   ├── core/              # @fusionaize/core — shared types, auth, errors
│   ├── gate/              # @fusionaize/gate — AI Gateway client
│   ├── lens/              # @fusionaize/lens — Context Layer client
│   ├── fabric/            # @fusionaize/fabric — Memory Fabric client
│   ├── grid/              # @fusionaize/grid — Execution Substrate client
│   ├── os/                # @fusionaize/os — Team Logic client
│   ├── signal/            # @fusionaize/signal — Operational Intelligence client
│   ├── studio/            # @fusionaize/studio — Blueprint Authoring client
│   └── cli/               # @fusionaize/cli — Unified CLI tool
├── contracts/             # Shared interface definitions (OpenAPI, gRPC protos)
├── examples/              # End-to-end examples
└── docs/                  # SDK-specific documentation
```

### Python (`fusionaize/`)

```
fusionaize/
├── fusionaize/
│   ├── core/              # fusionaize.core — shared types, auth, errors
│   ├── gate/              # fusionaize.gate
│   ├── lens/              # fusionaize.lens
│   ├── fabric/            # fusionaize.fabric
│   ├── grid/              # fusionaize.grid
│   ├── os/                # fusionaize.os
│   ├── signal/            # fusionaize.signal
│   └── studio/            # fusionaize.studio
├── contracts/             # Mirrored from TypeScript contracts/
└── examples/
```

!!! note
    Each TypeScript package is published independently to npm under
    `@fusionaize/*`. Python packages are published to PyPI under
    `fusionaize-*`. Dependencies between packages are declared
    explicitly and versioned together.

---

## Installation

=== "TypeScript"

    ```bash
    # Install individual packages
    npm install @fusionaize/gate @fusionaize/fabric

    # Or install the full SDK meta-package
    npm install @fusionaize/sdk

    # CLI tool
    npm install -g @fusionaize/cli
    ```

=== "Python"

    ```bash
    # Install individual packages
    pip install fusionaize-gate fusionaize-fabric

    # Or install the full SDK meta-package
    pip install fusionaize-sdk

    # CLI tool
    pip install fusionaize-cli
    ```

---

## Quickstart

### Connecting to Gate

=== "TypeScript"

    ```typescript
    import { GateClient } from "@fusionaize/gate";

    const gate = new GateClient({
      baseUrl: "https://gate.fusionaize.example.com",
      apiKey: process.env.FUSIONAIZE_API_KEY,
    });

    const response = await gate.chat.completions.create({
      model: "primary",
      messages: [{ role: "user", content: "Summarize Q3 metrics." }],
      maxTokens: 500,
    });

    console.log(response.choices[0].message.content);
    ```

=== "Python"

    ```python
    from fusionaize.gate import GateClient

    gate = GateClient(
        base_url="https://gate.fusionaize.example.com",
        api_key=os.environ["FUSIONAIZE_API_KEY"],
    )

    response = gate.chat.completions.create(
        model="primary",
        messages=[{"role": "user", "content": "Summarize Q3 metrics."}],
        max_tokens=500,
    )

    print(response.choices[0].message.content)
    ```

### Storing and Retrieving Memory via Fabric

=== "TypeScript"

    ```typescript
    import { FabricClient } from "@fusionaize/fabric";

    const fabric = new FabricClient({
      baseUrl: "https://fabric.fusionaize.example.com",
      apiKey: process.env.FUSIONAIZE_API_KEY,
    });

    // Store a memory
    await fabric.memories.store({
      content: "API rate limits reset at midnight UTC.",
      metadata: {
        source: "ops-playbook",
        tags: ["rate-limit", "production"],
      },
    });

    // Retrieve relevant memories
    const memories = await fabric.memories.search({
      query: "What are the API rate limits?",
      topK: 5,
    });

    for (const mem of memories) {
      console.log(`[${mem.score.toFixed(2)}] ${mem.content}`);
    }
    ```

=== "Python"

    ```python
    from fusionaize.fabric import FabricClient

    fabric = FabricClient(
        base_url="https://fabric.fusionaize.example.com",
        api_key=os.environ["FUSIONAIZE_API_KEY"],
    )

    # Store a memory
    fabric.memories.store(
        content="API rate limits reset at midnight UTC.",
        metadata={
            "source": "ops-playbook",
            "tags": ["rate-limit", "production"],
        },
    )

    # Retrieve relevant memories
    memories = fabric.memories.search(
        query="What are the API rate limits?",
        top_k=5,
    )

    for mem in memories:
        print(f"[{mem.score:.2f}] {mem.content}")
    ```

### Querying Signal Metrics

=== "TypeScript"

    ```typescript
    import { SignalClient } from "@fusionaize/signal";

    const signal = new SignalClient({
      baseUrl: "https://signal.fusionaize.example.com",
    });

    const latency = await signal.metrics.query({
      metric: "gate_request_duration_seconds",
      quantile: 0.95,
      window: "1h",
    });

    console.log(`P95 latency: ${latency.current}ms (baseline: ${latency.baseline}ms)`);
    ```

=== "Python"

    ```python
    from fusionaize.signal import SignalClient

    signal = SignalClient(
        base_url="https://signal.fusionaize.example.com",
    )

    latency = signal.metrics.query(
        metric="gate_request_duration_seconds",
        quantile=0.95,
        window="1h",
    )

    print(f"P95 latency: {latency.current}ms (baseline: {latency.baseline}ms)")
    ```

### Defining a Role via Studio

=== "TypeScript"

    ```typescript
    import { StudioClient } from "@fusionaize/studio";

    const studio = new StudioClient({
      baseUrl: "https://studio.fusionaize.example.com",
      apiKey: process.env.FUSIONAIZE_API_KEY,
    });

    const role = await studio.roles.create({
      name: "Customer Success Agent",
      domain: "post-purchase support",
      authority: "autonomous_with_escalation",
      constraints: {
        neverAccess: ["billing_api", "refund_api"],
        requireApproval: ["email_to_customer"],
        rateLimit: "10_rpm",
      },
      persona: {
        tone: "empathetic",
        formality: "semi-formal",
      },
    });

    // Run a simulation
    const sim = await studio.simulations.run(role.id, {
      scenario: "angry_customer_return",
      iterations: 10,
    });

    console.log(`Realism score: ${sim.realismScore}`);
    console.log(`Constraint violations: ${sim.violations}`);
    ```

=== "Python"

    ```python
    from fusionaize.studio import StudioClient

    studio = StudioClient(
        base_url="https://studio.fusionaize.example.com",
        api_key=os.environ["FUSIONAIZE_API_KEY"],
    )

    role = studio.roles.create(
        name="Customer Success Agent",
        domain="post-purchase support",
        authority="autonomous_with_escalation",
        constraints={
            "never_access": ["billing_api", "refund_api"],
            "require_approval": ["email_to_customer"],
            "rate_limit": "10_rpm",
        },
        persona={
            "tone": "empathetic",
            "formality": "semi-formal",
        },
    )

    sim = studio.simulations.run(role.id, {
        "scenario": "angry_customer_return",
        "iterations": 10,
    })

    print(f"Realism score: {sim.realism_score}")
    print(f"Constraint violations: {sim.violations}")
    ```

---

## Contracts and Interfaces

The SDK is contract-first. Shared interface definitions live in the
`contracts/` directory and drive both TypeScript type generation and
Python type stubs.

### Contract Sources

```
contracts/
├── openapi/
│   ├── gate.yaml           # Gate REST API specification
│   ├── fabric.yaml         # Fabric REST API specification
│   ├── signal.yaml         # Signal REST API specification
│   └── studio.yaml         # Studio REST API specification
├── proto/
│   ├── gate/
│   │   └── v1/
│   │       └── routing.proto
│   ├── grid/
│   │   └── v1/
│   │       └── execution.proto
│   └── os/
│       └── v1/
│           ├── roles.proto
│           └── policies.proto
└── shared/
    ├── auth.proto           # Common auth types
    ├── common.proto         # Shared primitives (Pagination, Error, etc.)
    └── telemetry.proto      # Metrics and tracing contracts
```

### Code Generation

```bash
# Generate TypeScript types from OpenAPI specs
pnpm --filter @fusionaize/gate generate:types
pnpm --filter @fusionaize/fabric generate:types

# Generate Python stubs from the same specs
cd contracts && make generate-python

# Generate gRPC clients from protobufs
cd contracts && make generate-grpc
```

The generation pipeline ensures that TypeScript and Python clients stay
synchronized with the service contracts. A CI check fails if codegen
output differs from the committed client code.

### Versioning

The SDK follows **semantic versioning with a shared epoch**:

- **Major** — breaking changes to any package's public API. All packages
  bump in lockstep.
- **Minor** — new features, non-breaking additions.
- **Patch** — bug fixes, documentation updates.

```json
{
  "name": "@fusionaize/sdk",
  "version": "1.4.2",
  "packages": {
    "@fusionaize/core": "1.4.2",
    "@fusionaize/gate": "1.4.2",
    "@fusionaize/fabric": "1.4.2",
    "@fusionaize/lens": "1.4.2",
    "@fusionaize/grid": "1.4.2",
    "@fusionaize/os": "1.4.2",
    "@fusionaize/signal": "1.4.2",
    "@fusionaize/studio": "1.4.2"
  }
}
```

---

## Authentication

All SDK clients support a common authentication interface:

=== "TypeScript"

    ```typescript
    import { FusionAIzeClient } from "@fusionaize/core";

    const client = new FusionAIzeClient({
      // API key for server-to-server communication
      apiKey: process.env.FUSIONAIZE_API_KEY,

      // OAuth2 client credentials for user-delegated access
      clientId: process.env.FUSIONAIZE_CLIENT_ID,
      clientSecret: process.env.FUSIONAIZE_CLIENT_SECRET,

      // Automatic token refresh
      autoRefresh: true,

      // Connection pooling and retry
      maxRetries: 3,
      timeout: 30_000,
    });

    // Same client works across all service packages
    const gate = client.gate();
    const fabric = client.fabric();
    const signal = client.signal();
    ```

=== "Python"

    ```python
    from fusionaize.core import FusionAIzeClient

    client = FusionAIzeClient(
        api_key=os.environ["FUSIONAIZE_API_KEY"],
        client_id=os.environ["FUSIONAIZE_CLIENT_ID"],
        client_secret=os.environ["FUSIONAIZE_CLIENT_SECRET"],
        auto_refresh=True,
        max_retries=3,
        timeout=30,
    )

    gate = client.gate()
    fabric = client.fabric()
    signal = client.signal()
    ```

---

## CLI Tool

The SDK includes a unified CLI (`fai`) for common operations:

```bash
# Health check
fai health --component gate

# Chat completion via Gate
fai gate chat --prompt "Summarize Q3 metrics" --model primary

# Search memory via Fabric
fai fabric search --query "API rate limits" --top-k 5

# Query metrics via Signal
fai signal metrics --metric gate_request_duration_seconds

# Run a role simulation via Studio
fai studio simulate --role-id "cs-agent-01" --scenario angry_customer

# List active OS roles
fai os roles --status active
```

---

## Error Handling

All SDK clients use a consistent error model:

=== "TypeScript"

    ```typescript
    import { FusionAIzeError, RateLimitError, AuthError } from "@fusionaize/core";

    try {
      const result = await gate.chat.completions.create({ /* ... */ });
    } catch (err) {
      if (err instanceof RateLimitError) {
        console.log(`Rate limited. Retry after ${err.retryAfter}s`);
      } else if (err instanceof AuthError) {
        console.log("Authentication failed. Refresh your API key.");
      } else if (err instanceof FusionAIzeError) {
        console.log(`${err.status} ${err.code}: ${err.message}`);
      }
    }
    ```

=== "Python"

    ```python
    from fusionaize.core import FusionAIzeError, RateLimitError, AuthError

    try:
        result = gate.chat.completions.create(...)
    except RateLimitError as e:
        print(f"Rate limited. Retry after {e.retry_after}s")
    except AuthError:
        print("Authentication failed. Refresh your API key.")
    except FusionAIzeError as e:
        print(f"{e.status} {e.code}: {e.message}")
    ```

---

## Development

```bash
# Clone the SDK monorepo
git clone https://git.langevc.com/fusionaize/fusionaize-sdk.git
cd fusionaize-sdk

# TypeScript packages
pnpm install
pnpm build
pnpm test

# Python packages
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/

# Regenerate contracts
make generate-all
```
