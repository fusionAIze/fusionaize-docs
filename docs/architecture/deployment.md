# Deployment Profiles

**Run fusionAIze anywhere — from a laptop to a data center.**

---

## Overview

fusionAIze is designed to run on **your infrastructure**. Every component
is packaged as a Docker container with no hard dependency on any cloud
provider. You choose where to run it, how to scale it, and which providers
to route to.

The stack can run on a single machine for development and testing, or scale
across a Kubernetes cluster for production.

---

## Deployment Profiles

### Profile Comparison

| Profile | Uses | Team Size | Typical Setup |
|---------|------|-----------|---------------|
| **Solo** | Development, personal projects, evaluation | 1 | Docker Compose on a single machine |
| **Small Team** | Internal tools, proof-of-concept | 2–10 | Docker Compose or lightweight orchestration |
| **SMB** | Production workloads, client projects | 10–100 | Docker Swarm or small Kubernetes cluster |
| **Enterprise** | Mission-critical, multi-tenant | 100+ | Kubernetes with HA, dedicated nodes |

---

## Solo — Single Machine

For developers and solo operators evaluating the stack or running personal
projects.

### Resource Requirements

| Component | CPU | RAM | Disk | Notes |
|-----------|-----|-----|------|-------|
| Gate | 0.5 core | 256 MB | 1 GB | Stateless, no disk growth |
| Lens | 0.5 core | 256 MB | 1 GB | Stateless |
| Fabric | 1 core | 1 GB | 10 GB+ | Grows with memory volume |
| Grid | 2 cores | 2 GB | 5 GB | Per-sandbox overhead |
| OS | 0.5 core | 256 MB | 1 GB | Stateless |
| Signal | 1 core | 512 MB | 20 GB+ | Grows with telemetry retention |
| **Total** | **~5.5 cores** | **~4.5 GB** | **~38 GB** | Minimum viable |

!!! tip "Local Model Recommendation"
    For the Solo profile, we recommend using cloud providers (OpenAI,
    Anthropic) for inference. If you want local models, budget an
    additional 8+ GB VRAM for a quantized 7B-parameter model via
    Ollama.

### Docker Compose

```yaml
# docker-compose.solo.yml
version: "3.9"

services:
  gate:
    image: fusionaize/gate:latest
    ports:
      - "8080:8080"
    environment:
      GATE_PROVIDERS_CONFIG: /etc/gate/providers.yml
      GATE_AUTH_MODE: api_key
      GATE_OS_ENDPOINT: http://os:8100
    volumes:
      - ./config/providers.yml:/etc/gate/providers.yml
    depends_on:
      - os

  lens:
    image: fusionaize/lens:latest
    ports:
      - "8081:8081"
    environment:
      LENS_FABRIC_ENDPOINT: http://fabric:8090
      LENS_COMPRESSION_STRATEGY: adaptive
      LENS_MAX_CONTEXT_TOKENS: 8000

  fabric:
    image: fusionaize/fabric:latest
    ports:
      - "8090:8090"
    environment:
      FABRIC_BACKEND: chromadb
      FABRIC_CHROMA_PATH: /data/chroma
    volumes:
      - fabric_data:/data
    depends_on:
      - chromadb

  chromadb:
    image: chromadb/chroma:latest
    volumes:
      - chroma_data:/chroma/chroma

  grid:
    image: fusionaize/grid:latest
    ports:
      - "8091:8091"
    environment:
      GRID_RUNTIME: docker
      GRID_OS_ENDPOINT: http://os:8100
      GRID_TOOL_BRIDGE_ENABLED: "true"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - grid_data:/var/lib/grid

  os:
    image: fusionaize/os:latest
    ports:
      - "8100:8100"
    environment:
      OS_DB_PATH: /data/os.db
      OS_AUTH_PROVIDER: local
    volumes:
      - os_data:/data

  signal:
    image: fusionaize/signal:latest
    ports:
      - "8122:8122"
    environment:
      SIGNAL_COLLECTORS: |
        - type: prometheus_scraper
          targets:
            - http://gate:8080/metrics
            - http://fabric:8090/metrics
            - http://grid:8091/metrics
    volumes:
      - signal_data:/var/lib/signal

volumes:
  fabric_data:
  chroma_data:
  grid_data:
  os_data:
  signal_data:
```

### Startup

```bash
docker compose -f docker-compose.solo.yml up -d
docker compose -f docker-compose.solo.yml logs -f
```

---

## Small Team — 2–10 Users

For internal tools, agency projects, and proof-of-concept deployments.

### Resource Requirements

| Component | CPU | RAM | Disk | Instances |
|-----------|-----|-----|------|-----------|
| Gate | 1 core | 512 MB | 5 GB | 2 |
| Lens | 1 core | 512 MB | 5 GB | 2 |
| Fabric | 2 cores | 2 GB | 50 GB | 1 |
| Grid | 4 cores | 4 GB | 20 GB | 2 |
| OS | 1 core | 512 MB | 5 GB | 1 |
| Signal | 2 cores | 1 GB | 50 GB | 1 |
| **Total** | **~12 cores** | **~10 GB** | **~140 GB** | |

### Key Adjustments from Solo

- **Gate replication** — two instances behind a load balancer for HA.
- **Grid pool** — two Grid nodes to handle concurrent sandboxes.
- **Fabric backend** — upgrade from ChromaDB to Qdrant for filtered search
  and better performance at scale.
- **Separate Signal storage** — use external Loki (logs) and Mimir
  (metrics) instead of embedded storage.

```yaml
# docker-compose.small-team.yml (fragment)
services:
  gate:
    image: fusionaize/gate:latest
    deploy:
      replicas: 2
    environment:
      GATE_PROVIDERS_CONFIG: /etc/gate/providers.yml
      GATE_FABRIC_BACKEND: qdrant
      GATE_QDRANT_ENDPOINT: http://qdrant:6333

  fabric:
    image: fusionaize/fabric:latest
    environment:
      FABRIC_BACKEND: qdrant
      FABRIC_QDRANT_ENDPOINT: http://qdrant:6333

  qdrant:
    image: qdrant/qdrant:latest
    volumes:
      - qdrant_data:/qdrant/storage

  grid:
    image: fusionaize/grid:latest
    deploy:
      replicas: 2

  signal:
    image: fusionaize/signal:latest
    environment:
      SIGNAL_LOGS_BACKEND: loki
      SIGNAL_METRICS_BACKEND: mimir
      SIGNAL_LOKI_ENDPOINT: http://loki:3100
      SIGNAL_MIMIR_ENDPOINT: http://mimir:9009
```

---

## SMB — 10–100 Users

For production workloads, client-facing deployments, and growing
organizations.

### Resource Requirements

| Component | CPU | RAM | Disk | Instances |
|-----------|-----|-----|------|-----------|
| Gate | 2 cores | 1 GB | 10 GB | 3 |
| Lens | 2 cores | 1 GB | 10 GB | 3 |
| Fabric | 4 cores | 4 GB | 200 GB | 1 (with replicas) |
| Grid | 8 cores | 8 GB | 50 GB | 4 |
| OS | 2 cores | 1 GB | 10 GB | 2 (HA) |
| Signal | 4 cores | 2 GB | 200 GB | 1 |
| Load Balancer | 1 core | 512 MB | — | 1 |
| **Total** | **~37 cores** | **~33 GB** | **~480 GB** | |

### Infrastructure Addition

```mermaid
flowchart TB
    LB[Nginx / Traefik<br>Load Balancer]

    subgraph "Gate Pool (3)"
        G1[Gate 1]
        G2[Gate 2]
        G3[Gate 3]
    end

    subgraph "Lens Pool (3)"
        L1[Lens 1]
        L2[Lens 2]
        L3[Lens 3]
    end

    subgraph "Grid Pool (4)"
        GR1[Grid 1]
        GR2[Grid 2]
        GR3[Grid 3]
        GR4[Grid 4]
    end

    subgraph "Data Layer"
        Q[Qdrant<br>Vector Store]
        PG[(PostgreSQL<br>OS State)]
        LK[Loki + Mimir<br>Telemetry]
    end

    subgraph "Core Services"
        F[Fabric]
        OS[OS (HA)]
        SIG[Signal]
    end

    LB --> G1 & G2 & G3
    G1 & G2 & G3 --> L1 & L2 & L3
    L1 & L2 & L3 --> F
    G1 & G2 & G3 --> GR1 & GR2 & GR3 & GR4

    F --> Q
    OS --> PG
    SIG --> LK
```

### Docker Swarm Example

```yaml
# stack.smb.yml (fragment)
services:
  gate:
    image: fusionaize/gate:latest
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: "2"
          memory: 1G
      restart_policy:
        condition: on-failure
      update_config:
        parallelism: 1
        delay: 10s

  grid:
    image: fusionaize/grid:latest
    deploy:
      replicas: 4
      resources:
        limits:
          cpus: "8"
          memory: 8G
```

---

## Enterprise — 100+ Users

For mission-critical, multi-tenant deployments with strict SLAs.

### Resource Requirements

| Component | CPU | RAM | Disk | Instances |
|-----------|-----|-----|------|-----------|
| Gate | 4 cores | 2 GB | 20 GB | 5+ |
| Lens | 4 cores | 2 GB | 20 GB | 5+ |
| Fabric | 8 cores | 16 GB | 1 TB+ | 3 (HA) |
| Grid | 16 cores | 16 GB | 100 GB | 10+ |
| OS | 4 cores | 2 GB | 20 GB | 3 (HA) |
| Signal | 8 cores | 8 GB | 1 TB+ | 2 (HA) |
| **Total** | **~104+ cores** | **~90+ GB** | **~3 TB+** | |

### Enterprise Architecture

```mermaid
flowchart TB
    subgraph "Edge Layer"
        WAF[WAF / DDoS Protection]
        LB[Global Load Balancer]
        CDN[CDN]
    end

    subgraph "Application Layer — Kubernetes"
        subgraph "Gate Service"
            G1[Gate Pod × 5]
        end
        subgraph "Lens Service"
            L1[Lens Pod × 5]
        end
        subgraph "Grid Service"
            GR1[Grid Pod × 10]
        end
    end

    subgraph "Data Layer — StatefulSets"
        F1[Fabric Primary]
        F2[Fabric Replica]
        F3[Fabric Replica]
        OS1[OS Primary]
        OS2[OS Replica]
    end

    subgraph "Observability"
        SIG1[Signal Primary]
        SIG2[Signal Replica]
        PROMS[Mimir — Metrics<br>(HA)]
        LOGS[Loki — Logs<br>(HA)]
        TRACES[Tempo — Traces<br>(HA)]
    end

    WAF --> LB
    LB --> G1
    G1 --> L1
    L1 --> F1
    G1 --> GR1
    F1 --> F2 & F3
    OS1 --> OS2
    SIG1 --> PROMS & LOGS & TRACES
```

### Kubernetes Deployment

```yaml
# gate-deployment.yaml (fragment)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gate
  namespace: fusionaize
spec:
  replicas: 5
  selector:
    matchLabels:
      app: gate
  template:
    metadata:
      labels:
        app: gate
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values: [gate]
              topologyKey: kubernetes.io/hostname
      containers:
        - name: gate
          image: fusionaize/gate:latest
          resources:
            requests:
              cpu: "2"
              memory: "1Gi"
            limits:
              cpu: "4"
              memory: "2Gi"
          env:
            - name: GATE_OS_ENDPOINT
              value: http://os-service:8100
            - name: GATE_AUTH_MODE
              value: oauth2
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 15
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: gate-service
  namespace: fusionaize
spec:
  selector:
    app: gate
  ports:
    - port: 8080
      targetPort: 8080
  type: ClusterIP
```

---

## On-Premise Options

### Bare Metal / VM

All components run directly on bare metal or virtual machines via Docker.
No Kubernetes required.

```bash
# Install Docker on each node
curl -fsSL https://get.docker.com | sh

# Run components directly
docker run -d --name gate --restart unless-stopped \
  -p 8080:8080 \
  -v /etc/fusionaize/providers.yml:/etc/gate/providers.yml \
  fusionaize/gate:latest

docker run -d --name fabric --restart unless-stopped \
  -p 8090:8090 \
  -v /data/fabric:/data \
  fusionaize/fabric:latest
```

### Air-Gapped Deployment

For environments without internet access:

1. Build or pull images on an internet-connected machine.
2. Export images as tarballs.
3. Transfer to the air-gapped environment.
4. Load and run.

```bash
# On internet-connected machine
docker pull fusionaize/gate:latest
docker save fusionaize/gate:latest | gzip > gate.tar.gz

# On air-gapped machine
docker load < gate.tar.gz
docker run -d fusionaize/gate:latest
```

### Local Model Support

Every component can route to locally-hosted models:

```yaml
# providers.yml — local-only configuration
providers:
  ollama-local:
    type: ollama
    endpoint: http://localhost:11434
    models:
      - llama3.1:8b
      - mistral:7b
      - qwen2.5:14b

  vllm-local:
    type: vllm
    endpoint: http://localhost:8000
    models:
      - llama-3-70b
```

!!! warning "Local Model Performance"
    Local models require significant GPU memory. Budget:
    - 7B model quantized: ~6 GB VRAM
    - 7B model full: ~14 GB VRAM
    - 70B model quantized: ~40 GB VRAM
    - 70B model full: ~140 GB VRAM
    
    For acceptable latency in production, plan for one GPU per active
    concurrent request.

---

## Resource Calculator

Use these formulas to estimate resource needs from your workload:

```
Gate CPU = (requests_per_second / 50) × 0.5 cores
Gate RAM = (requests_per_second / 50) × 256 MB

Grid CPU = concurrent_sandboxes × 1 core
Grid RAM = concurrent_sandboxes × 512 MB

Fabric RAM = (total_memories / 1000000) × 2 GB
Fabric Disk = total_memories × 2 KB × embedding_dim / 1024

Signal Disk = telemetry_retention_days × events_per_day × 250 bytes
```

---

## Environment Variables Reference

### Common (all components)

| Variable | Description | Default |
|----------|-------------|---------|
| `FUSIONAIZE_LOG_LEVEL` | Log verbosity (debug, info, warn, error) | `info` |
| `FUSIONAIZE_LOG_FORMAT` | Log output format (json, text) | `json` |
| `FUSIONAIZE_METRICS_ENABLED` | Enable Prometheus metrics endpoint | `true` |
| `FUSIONAIZE_TRACING_ENABLED` | Enable distributed tracing | `false` |
| `FUSIONAIZE_TRACING_ENDPOINT` | OTLP collector endpoint | — |

### Gate

| Variable | Description | Default |
|----------|-------------|---------|
| `GATE_PORT` | HTTP listen port | `8080` |
| `GATE_PROVIDERS_CONFIG` | Path to providers configuration YAML | `/etc/gate/providers.yml` |
| `GATE_AUTH_MODE` | Authentication mode (api_key, oauth2, mTLS) | `api_key` |
| `GATE_OS_ENDPOINT` | OS service endpoint | — |
| `GATE_MAX_CONCURRENT` | Maximum concurrent requests | `1000` |
| `GATE_REQUEST_TIMEOUT_S` | Request timeout in seconds | `120` |

### Fabric

| Variable | Description | Default |
|----------|-------------|---------|
| `FABRIC_PORT` | HTTP listen port | `8090` |
| `FABRIC_BACKEND` | Storage backend (chromadb, qdrant, pgvector) | `chromadb` |
| `FABRIC_CHROMA_PATH` | ChromaDB data directory | `/data/chroma` |
| `FABRIC_QDRANT_ENDPOINT` | Qdrant service endpoint | — |
| `FABRIC_EMBEDDING_MODEL` | Model used for embeddings | `all-MiniLM-L6-v2` |

### Grid

| Variable | Description | Default |
|----------|-------------|---------|
| `GRID_PORT` | HTTP listen port | `8091` |
| `GRID_RUNTIME` | Sandbox runtime (docker, firecracker, native) | `docker` |
| `GRID_OS_ENDPOINT` | OS service endpoint | — |
| `GRID_MAX_SANDBOXES` | Concurrent sandbox limit | `50` |
| `GRID_SANDBOX_TIMEOUT_S` | Max sandbox lifetime in seconds | `600` |
