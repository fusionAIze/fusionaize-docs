# Quickstart

fusionAIze is the operating platform for human-AI fusion teams. This guide gets you from zero to your first AI-powered virtual employee in under five minutes.

You will install **Gate** (`faigate`) — the unified entry point for all AI interactions — configure your first model provider, send a test request, and learn where to go next.

---

## Prerequisites

| Requirement | Version | Notes |
|------------|---------|-------|
| **Python** | 3.10+ | Required for pip installs and CLI tooling |
| **Docker** | 24.0+ | Required for Docker-based deployment (optional) |
| **Docker Compose** | 2.20+ | Required if using the Docker Compose full-stack option |
| **pip** | 23.0+ | Latest version recommended (`pip install --upgrade pip`) |

A model provider account or a locally running model is needed to send requests. Gate supports:

- **Anthropic** (Claude models)
- **OpenAI** (GPT, o-series models)
- **Google** (Gemini models)
- **Local models** via Ollama, vLLM, or any OpenAI-compatible endpoint
- **Custom providers** via the Gate provider plugin interface

---

## Step 1: Install Gate

Gate (`faigate`) is the entry point to the entire fusionAIze stack. It provides a unified, provider-agnostic API surface that every other component plugs into.

=== "pip"

    ```bash
    pip install faigate
    ```

    !!! success "Recommended"
        pip is the fastest way to get started. The `faigate` package includes the Gate server, CLI, and Python client library.

    Verify the installation:

    ```bash
    faigate --version
    ```

=== "Docker"

    ```bash
    docker pull ghcr.io/fusionaize/gate:latest
    docker run -d -p 8120:8120 --name faigate ghcr.io/fusionaize/gate:latest
    ```

=== "Docker Compose"

    ```bash
    git clone https://git.langevc.com/fusionaize/faigate.git
    cd faigate
    docker compose up -d
    ```

    This starts Gate alongside its dependencies (Redis for caching, Postgres for state persistence).

??? question "Which method should I choose?"
    - **pip** — best for development, CLI usage, and embedding Gate into Python applications.
    - **Docker** — best for quick evaluation and isolated testing.
    - **Docker Compose** — best for a production-like setup with persistence and caching out of the box.

Gate starts on `http://localhost:8120`. Check that it's running:

```bash
curl http://localhost:8120/health
# {"status": "ok", "component": "gate", "version": "0.1.0"}
```

---

## Step 2: Configure your first provider

Gate needs at least one model provider configured before it can route requests.

=== "Anthropic"

    Set your API key as an environment variable:

    ```bash
    export ANTHROPIC_API_KEY="sk-ant-..."
    ```

    Then add the provider in Gate's configuration:

    ```yaml title="~/.config/fusionaize/gate.yaml"
    providers:
      - id: anthropic
        type: anthropic
        api_key_env: ANTHROPIC_API_KEY
        default_model: claude-sonnet-4-20250514
    ```

=== "OpenAI"

    ```bash
    export OPENAI_API_KEY="sk-..."
    ```

    ```yaml title="~/.config/fusionaize/gate.yaml"
    providers:
      - id: openai
        type: openai
        api_key_env: OPENAI_API_KEY
        default_model: gpt-4o
    ```

=== "Local (Ollama)"

    Gate connects to a locally running Ollama instance automatically:

    ```bash
    # Start Ollama and pull a model
    ollama pull llama3.2

    # Gate detects Ollama at http://localhost:11434 by default
    ```

    ```yaml title="~/.config/fusionaize/gate.yaml"
    providers:
      - id: ollama-local
        type: openai-compatible
        base_url: http://localhost:11434/v1
        api_key: ollama
        default_model: llama3.2
    ```

=== "Multiple providers (recommended)"

    Configure multiple providers with fallback routing:

    ```yaml title="~/.config/fusionaize/gate.yaml"
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

      - id: ollama-fallback
        type: openai-compatible
        base_url: http://localhost:11434/v1
        api_key: ollama
        default_model: llama3.2
        priority: 3

    routing:
      strategy: priority-failover
      fallback_on:
        - rate_limit
        - provider_error
        - timeout
    ```

    !!! tip "Why multiple providers?"
        A fallback chain means your fusion team keeps working even if a provider is experiencing downtime. Gate handles the failover transparently.

---

## Step 3: Send your first request

With Gate running, send your first request through the unified API:

=== "CLI"

    ```bash
    faigate chat "What is the core idea behind fusionAIze?"
    ```

=== "Python SDK"

    ```python
    from faigate import GateClient

    gate = GateClient()  # defaults to http://localhost:8120

    response = gate.chat.completions.create(
        model="claude-sonnet-4-20250514",
        messages=[
            {"role": "system", "content": "You are a virtual employee of a fusion team."},
            {"role": "user", "content": "Hello! What can you help me build today?"},
        ],
    )

    print(response.choices[0].message.content)
    ```

=== "cURL"

    ```bash
    curl http://localhost:8120/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer ${ANTHROPIC_API_KEY}" \
      -d '{
        "model": "claude-sonnet-4-20250514",
        "messages": [
          {"role": "user", "content": "What is a fusion team?"}
        ]
      }'
    ```

Gate's API is **OpenAI-compatible**. Any client, library, or tool that speaks the OpenAI chat completions format works with Gate — with the added benefit of provider routing, fallback, and governance layered underneath.

!!! success "You're connected"
    If you got a response, Gate is configured correctly and your first provider is active. You now have a unified AI gateway running locally.

---

## Next steps

Gate alone gives you a provider-agnostic API surface with routing and fallback. The real power of fusionAIze comes when you layer the rest of the stack on top.

| Step | What you add | Why |
|------|-------------|-----|
| **1. Add Lens** | Context compression layer | Focuses context so AI colleagues work with exactly the right information — no more, no less. [Lens docs →](../products/lens/index.md) |
| **2. Set up Fabric** | Shared memory fabric | Persistent knowledge across every interaction. No more "as an AI, I don't remember our last conversation." [Fabric docs →](../products/fabric/index.md) |
| **3. Explore the SDK** | Language-native integration | Embed fusionAIze into your existing tools and workflows in Python, TypeScript, or Go. [SDK docs →](../products/sdk/index.md) |
| **4. Deploy with Grid** | Sovereign execution substrate | Run your AI agents in isolated, auditable environments within your own infrastructure. [Grid docs →](../products/grid/index.md) |
| **5. Define faios roles** | Team operating logic | Create roles, policies, and collaboration patterns for your virtual employees. [faios docs →](../products/os/index.md) |

!!! tip "Docker Compose full stack"
    The quickest way to try the entire core stack is with the Docker Compose full-stack deployment:
    ```bash
    git clone https://git.langevc.com/fusionaize/full-stack.git
    cd full-stack
    docker compose up -d
    ```
    This brings up Gate, Lens, Fabric, and Grid together with pre-configured defaults.

---

## Dive deeper

<div class="grid cards" markdown>

-   :fontawesome-solid-download: **Installation Guide**

    ---

    Detailed installation instructions for every component and platform.

    [:octicons-arrow-right-24: Install fusionAIze](install.md)

-   :fontawesome-solid-gear: **Configuration**

    ---

    Complete configuration reference for all components.

    [:octicons-arrow-right-24: Configure the stack](config.md)

-   :fontawesome-solid-cubes: **Platform Overview**

    ---

    Understand how Gate, Lens, Fabric, Grid, and faios work together.

    [:octicons-arrow-right-24: Platform overview](../about/platform.md)

-   :fontawesome-solid-code: **SDK Reference**

    ---

    Integrate fusionAIze into your applications.

    [:octicons-arrow-right-24: SDK documentation](../products/sdk/index.md)

</div>

---

## Need help?

- Report issues on our [Forgejo instance](https://git.langevc.com/fusionaize)
- Star and discuss on [GitHub](https://github.com/fusionAIze)
- Browse the [architecture documentation](../architecture/index.md) for deep dives
