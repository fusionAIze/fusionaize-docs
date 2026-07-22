# Installation

fusionAIze components are designed to be installed individually or as a unified stack. This guide covers every installation method, platform-specific considerations, and verification steps.

---

## Installation matrix

| Component | pip | Docker | Source |
|-----------|-----|--------|--------|
| **Gate** (`faigate`) | `pip install faigate` | `ghcr.io/fusionaize/gate` | [Repository](https://git.langevc.com/fusionaize/faigate) |
| **Lens** (`failens`) | `pip install failens` | `ghcr.io/fusionaize/lens` | [Repository](https://git.langevc.com/fusionaize/failens) |
| **Fabric** (`faifabric`) | `pip install faifabric` | `ghcr.io/fusionaize/fabric` | [Repository](https://git.langevc.com/fusionaize/faifabric) |
| **Grid** (`faigrid`) | — | `ghcr.io/fusionaize/grid` | [Repository](https://git.langevc.com/fusionaize/faigrid) |
| **faios** | `pip install faios` | `ghcr.io/fusionaize/os` | [Repository](https://git.langevc.com/fusionaize/faios) |
| **SDK** | `pip install faisdk` | — | [Repository](https://git.langevc.com/fusionaize/faisdk) |
| **CLI** | `pip install faicli` | — | [Repository](https://git.langevc.com/fusionaize/faicli) |

---

## Prerequisites

Before installing any component, ensure your system has:

| Dependency | Version | Check command |
|-----------|---------|---------------|
| Python | 3.10+ | `python --version` |
| pip | 23.0+ | `pip --version` |
| Docker (optional) | 24.0+ | `docker --version` |
| Docker Compose (optional) | 2.20+ | `docker compose version` |
| Git (source installs) | 2.40+ | `git --version` |

---

## Installation methods

### Method 1: pip — per-component install

Install individual components as needed. This is the recommended approach for embedding fusionAIze into existing applications.

```bash
# Install only what you need
pip install faigate        # AI Gateway — entry point for all interactions
pip install failens        # Context compression layer
pip install faifabric      # Persistent memory fabric
pip install faios          # Team operating logic
pip install faisdk         # Python SDK for integration
pip install faicli         # Command-line interface
```

!!! tip "Install everything"
    ```bash
    pip install faigate failens faifabric faios faisdk faicli
    ```

**Virtual environment (recommended):**

```bash
python -m venv .venv
source .venv/bin/activate
pip install faigate failens faifabric
```

### Method 2: Docker — per-component containers

Each component is available as a standalone Docker image.

```bash
# Gate — AI Gateway
docker pull ghcr.io/fusionaize/gate:latest
docker run -d -p 8120:8120 \
  -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
  --name faigate \
  ghcr.io/fusionaize/gate:latest

# Lens — Context Layer
docker pull ghcr.io/fusionaize/lens:latest
docker run -d -p 8121:8121 \
  -e GATE_URL=http://faigate:8120 \
  --name failens \
  ghcr.io/fusionaize/lens:latest

# Fabric — Memory Fabric
docker pull ghcr.io/fusionaize/fabric:latest
docker run -d -p 8122:8122 \
  -e FABRIC_STORE_PATH=/data \
  -v fabric-data:/data \
  --name faifabric \
  ghcr.io/fusionaize/fabric:latest

# Grid — Execution Substrate
docker pull ghcr.io/fusionaize/grid:latest
docker run -d -p 8123:8123 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  --name faigrid \
  ghcr.io/fusionaize/grid:latest
```

### Method 3: Docker Compose — full stack

The recommended way to run the entire core stack in a unified, pre-configured deployment.

```bash
# Clone the full-stack repository
git clone https://git.langevc.com/fusionaize/full-stack.git
cd full-stack

# Copy and edit the environment file
cp .env.example .env
# Add your API keys: ANTHROPIC_API_KEY, OPENAI_API_KEY, etc.

# Start everything
docker compose up -d
```

The Docker Compose setup includes:

| Service | Port | Purpose |
|---------|------|---------|
| **gate** | 8120 | AI Gateway — all requests enter here |
| **lens** | 8121 | Context compression and focusing |
| **fabric** | 8122 | Shared memory and knowledge persistence |
| **grid** | 8123 | Isolated execution environment |
| **faios** | 8124 | Team operating logic and policy engine |
| **redis** | 6379 | Caching and ephemeral state |
| **postgres** | 5432 | Persistent storage for Fabric and faios |
| **dashboard** | 8080 | Web UI for monitoring and management |

```yaml title="docker-compose.override.yaml (example customisation)"
services:
  gate:
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - GATE_LOG_LEVEL=debug
    volumes:
      - ./config/gate.yaml:/etc/fusionaize/gate.yaml:ro

  fabric:
    volumes:
      - fabric-data:/data
    environment:
      - FABRIC_BACKEND=postgres

volumes:
  fabric-data:
```

### Method 4: Source — development installs

For contributors and developers who need the latest unreleased code.

```bash
# Gate (example — same pattern for all components)
git clone https://git.langevc.com/fusionaize/faigate.git
cd faigate

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install in development mode with all dependencies
pip install -e ".[dev,test,docs]"

# Verify
pytest
```

Each component repository follows the same structure:

```
faigate/
├── pyproject.toml
├── src/
│   └── faigate/
├── tests/
├── docker/
└── docs/
```

---

## Platform-specific notes

### macOS

Gate and Lens install cleanly via pip. For Docker-based deployments, ensure Docker Desktop is installed.

```bash
# Install via Homebrew (optional)
brew install python@3.12
pip install faigate

# Docker Desktop
brew install --cask docker
```

!!! warning "Apple Silicon (M-series)"
    All components run natively on ARM64. Docker images are multi-arch (`linux/amd64`, `linux/arm64`). If you encounter issues with a specific model provider's Python library, ensure you're using universal2 wheels or install via `pip install --no-binary`.

### Linux

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install python3 python3-pip python3-venv
pip install faigate

# Fedora / RHEL
sudo dnf install python3 python3-pip
pip install faigate
```

For Docker-based deployments:

```bash
# Ubuntu
sudo apt install docker.io docker-compose-v2

# Add your user to the docker group
sudo usermod -aG docker $USER
newgrp docker
```

Grid requires the Docker socket to be accessible for container-based execution sandboxing. Ensure `/var/run/docker.sock` is available.

### Windows (WSL 2)

fusionAIze is developed and tested on Linux. Windows users should install via **WSL 2**.

```powershell
# In PowerShell (Admin)
wsl --install -d Ubuntu
```

Then follow the [Linux instructions](#linux) inside the WSL terminal.

!!! info "Docker on WSL"
    Install Docker Desktop with WSL 2 backend enabled, or install Docker Engine directly inside WSL:
    ```bash
    sudo apt install docker.io docker-compose-v2
    sudo service docker start
    ```

---

## Component-specific configurations

### Gate — provider dependencies

Gate is provider-agnostic but installs client libraries lazily. Install what you need:

```bash
pip install faigate[anthropic]     # Anthropic provider support
pip install faigate[openai]        # OpenAI provider support
pip install faigate[google]        # Google Gemini provider support
pip install faigate[all-providers] # All supported providers
```

### Fabric — storage backends

Fabric supports multiple storage backends:

```bash
pip install faifabric[postgres]    # PostgreSQL backend
pip install faifabric[sqlite]      # SQLite backend (default)
pip install faifabric[chromadb]    # ChromaDB for embeddings
pip install faifabric[qdrant]      # Qdrant for embeddings
pip install faifabric[all]         # All backends
```

### Grid — runner profiles

Grid manages Docker-based execution sandboxes. It requires:

- Docker Engine (24.0+) with the socket accessible
- Sufficient disk space for container images (minimum 2 GB)
- Network access for pulling runner images

---

## Verification

After installation, verify each component is working:

=== "Gate"

    ```bash
    # If installed via pip
    faigate --version
    faigate health

    # If running via Docker
    curl http://localhost:8120/health
    ```

=== "Lens"

    ```bash
    failens --version
    curl http://localhost:8121/health
    ```

=== "Fabric"

    ```bash
    faifabric --version
    curl http://localhost:8122/health
    ```

=== "Grid"

    ```bash
    curl http://localhost:8123/health
    ```

=== "Full stack (Docker Compose)"

    ```bash
    docker compose ps
    # All services should show "healthy" or "running"

    # Test the complete chain
    curl http://localhost:8120/health  # Gate
    curl http://localhost:8121/health  # Lens
    curl http://localhost:8122/health  # Fabric
    curl http://localhost:8123/health  # Grid
    ```

=== "End-to-end test"

    ```bash
    faigate chat "Hello from a verified fusionAIze installation"
    # Should return a response from your configured default provider
    ```

---

## Troubleshooting

!!! failure "Gate fails to start"
    **Symptom:** `faigate: command not found` or Docker container exits immediately.

    **Fix:** Ensure the virtual environment is activated (pip install), or check Docker logs:
    ```bash
    docker logs faigate
    ```

!!! failure "No providers available"
    **Symptom:** Gate returns `{"error": "no_provider_available"}`.

    **Fix:** Check that API keys are set:
    ```bash
    echo $ANTHROPIC_API_KEY  # should not be empty
    ```
    And that your `gate.yaml` configuration references the correct environment variable names.

!!! failure "Docker Compose services won't start"
    **Symptom:** `docker compose up` fails with port conflicts.

    **Fix:** Something is already using ports 8120—8124. Find and free them:
    ```bash
    sudo lsof -i :8120
    # Or use different ports in docker-compose.override.yaml
    ```

!!! failure "Grid fails to create containers"
    **Symptom:** Grid logs show `permission denied` when accessing Docker socket.

    **Fix:** Ensure the user running Grid can access the Docker socket:
    ```bash
    sudo usermod -aG docker $USER
    newgrp docker
    ```

---

## Next steps

- [Configure your first provider](index.md) — set up Gate with API keys
- [Configuration reference](config.md) — deep dive into every configuration option
- [Platform overview](../about/platform.md) — understand how components connect
