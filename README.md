# fusionAIze Docs

[![CI](https://github.com/fusionAIze/faiops-browser/actions/workflows/ci.yml/badge.svg)](https://github.com/fusionAIze/faiops-browser/actions/workflows/ci.yml)
[![CodeQL](https://github.com/fusionAIze/faiops-browser/actions/workflows/codeql.yml/badge.svg)](https://github.com/fusionAIze/faiops-browser/actions/workflows/codeql.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](./LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-2496ED?logo=docker&logoColor=white)](./Dockerfile)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](./pyproject.toml)

**The browser‑based operator dashboard for the fusionAIze stack.**

fusionAIze Docs provides a unified, real‑time dashboard for monitoring health, cost, quality, and collaboration signals across the fusionAIze ecosystem. It gives operators, founders, and small teams the visibility they need without drowning in raw telemetry.

It focuses on four first‑class responsibilities:

1. **Real‑time monitoring** – live metrics from Gate, Grid, Lens, Fabric, and fusionAIzeOS.
2. **Cross‑layer correlation** – connecting signals across components to show what matters.
3. **Actionable insights** – highlighting what needs attention, where cost is rising, and where collaboration is breaking down.
4. **Operator‑friendly interface** – intuitive browser UI designed for solo operators and small teams.

Ops Browser is a **standalone, composable product** that works in heterogeneous environments and becomes even more powerful when embedded in the broader fusionAIze ecosystem.

## Quick Navigation

- [Why fusionAIze Docs](#why-fusionaize-signal)
- [MVP Scope](#mvp-scope)
- [Quickstart](#quickstart)
- [Architecture](#architecture)
- [Integration with the fusionAIze Stack](#integration-with-the-fusionaize-stack)
- [Development](#development)
- [Community and Security](#community-and-security)

## Why fusionAIze Docs

Modern AI‑native systems suffer from fragmented observability:

- **Too many silos** – each component (Gate, Fabric, Lens, Grid) emits its own logs, metrics, and traces without a unified view.
- **Too much noise** – raw telemetry is voluminous, unstructured, and hard to correlate.
- **Poor alerting** – missing deterministic rule‑based detection, leading to delayed incident response.
- **Lack of role‑aware visualization** – operators, developers, and learners need different views of the same signals.
- **Missing cross‑component correlation** – incidents often span multiple layers, but tracing across them is manual.

The result is operational blindness, slow debugging, missed anomalies, and poor team alignment.

Signal solves these problems by being **deterministic‑first, plugin‑friendly, and dashboard‑built‑in**.

## MVP Scope

Signal v1 focuses on three concrete outcomes:

### 1. Metrics collection and aggregation
Collect Prometheus‑style metrics from Gate, Fabric, Lens, Grid, and OS via lightweight exporters. Aggregate, downsample, and store them for querying.

### 2. Log ingestion and filtering
Ingest structured logs (JSON lines, syslog, application logs) from across the stack. Filter, parse, and index them for fast search and alerting.

### 3. Alert rule engine
Evaluate deterministic rules (thresholds, absence, rate‑of‑change) against metrics and logs. Send notifications via webhook, email, or chat platforms.

Every signal yields **contextual metadata** that answers:
- what changed
- where it changed
- why it matters
- who should be alerted
- how to investigate

## Quickstart

```bash
# Clone the repository
git clone https://github.com/fusionAIze/faiops-browser.git
cd faiops-browser

# Set up a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Signal with development dependencies
pip install -e .[dev]

# Install pre‑commit hooks
pre‑commit install

# Run the test suite
pytest tests/
```

### Basic CLI usage (conceptual – commands will evolve)

```bash
# Query metrics
faiops-browser metrics --source gateway --interval 1h

# Tail logs from a component
faiops-browser logs --component gate --tail 50

# List active alerts
faiops-browser alerts --list

# Check health of monitored services
faiops-browser health --service faigate
```

### Local HTTP API (planned)

```bash
# Start the Signal service
faiops-browser serve --port 8122

# Query metrics via API
curl -X GET http://127.0.0.1:8122/api/v1/metrics?query=gate_requests_total

# Submit a log entry
curl -X POST http://127.0.0.1:8122/api/v1/logs \
  -H "Content-Type: application/json" \
  -d '{
    "component": "gate",
    "level": "info",
    "message": "Request routed successfully",
    "timestamp": "2025-03-23T10:00:00Z"
  }'
```

## Architecture

Signal is built around a **plugin‑based pipeline architecture**:

- **Core orchestration** (`signal‑core`) – ingestion contracts, pipeline routing, storage abstraction.
- **Collector plugins** (`signal‑collector`) – Prometheus scrapers, log tailers, event listeners, trace receivers.
- **Processor plugins** (`signal‑processor`) – aggregation, filtering, enrichment, compression.
- **Alerting plugins** (`signal‑alert`) – rule evaluation, notification dispatch, suppression.
- **Storage plugins** (`signal‑storage`) – time‑series databases, log indexes, trace stores.
- **Visualization plugins** (`signal‑viz`) – operator dashboards, developer debug views, academy teaching views.
- **Adapters** (`signal‑adapters`) – CLI, HTTP API, file/stdin/stdout, MCP shim, Gate/Fabric/Grid hooks.

### Plugin families

- **Collector plugins** – `prometheus_scraper`, `log_ingestor`, `event_receiver`, `trace_span_collector`
- **Processor plugins** – `metric_aggregator`, `log_parser`, `anomaly_detector`, `correlation_engine`
- **Alert plugins** – `threshold_alert`, `absence_alert`, `rate_alert`, `composite_alert`
- **Storage plugins** – `tsdb_prometheus`, `logs_loki`, `traces_jaeger`
- **Visualization plugins** – `operator_dashboard`, `developer_debug`, `academy_teaching`

## Integration with the fusionAIze Stack

### Signal + Gate
Signal can collect **gateway metrics** (request rate, latency, error rate, provider health) and **gateway logs** for real‑time routing visibility.

### Signal + Fabric
Signal can monitor **memory usage, recall latency, and cache hit rates** from Fabric, providing insights into context‑retrieval performance.

### Signal + Lens
Signal can track **compression ratios, token savings, and explanation quality** from Lens, helping optimize context‑window usage.

### Signal + Grid
Signal can observe **execution substrate health, runner queue depth, and isolation violations** across Grid nodes.

### Signal + fusionAIzeOS
Signal can adopt **role‑, policy‑, and identity‑aware alerting** based on team structures, responsibilities, and escalation paths defined in fusionAIzeOS.

### Signal + Academy
Signal’s **visualization and explanation surfaces** become live teaching tools for operational literacy, incident response, and system‑understanding.

## Development

### Prerequisites

- Python 3.10+
- `pip` and `virtualenv` (or equivalent)
- Git

### Setup

```bash
git clone https://github.com/fusionAIze/faiops-browser.git
cd faiops-browser
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pre‑commit install
```

### Running tests

```bash
pytest tests/                      # unit and integration tests
pytest tests/benchmarks/           # performance benchmarks (requires pytest‑benchmark)
ruff check .                       # linting
ruff format --check .              # formatting check
```

### Pre‑commit hooks

The repository includes pre‑commit hooks for:

- trailing‑whitespace removal
- end‑of‑file fixer
- YAML validation
- private‑key detection
- Ruff linting and formatting
- Bandit security scanning
- conventional‑commit validation

Hooks run automatically on `git commit`.

### DevContainer

A VS Code DevContainer configuration is provided in `.devcontainer/devcontainer.json`. It includes:

- Python 3.12
- GitHub CLI
- Docker‑in‑Docker
- VS Code extensions for Python, Ruff, YAML, Docker, and GitHub Actions

## Community and Security

- [Contributing](./CONTRIBUTING.md)
- [Security policy](./SECURITY.md)
- [Code of conduct](./CODE_OF_CONDUCT.md)
- [Repo safety and CI](./.github/workflows)

Signal follows the same repo‑safety, CodeQL, Dependabot, and secret‑scanning practices as the rest of the fusionAIze stack.

## License

Apache‑2.0. See [LICENSE](./LICENSE).

---

**fusionAIze Docs** is part of the fusionAIze product stack:

- **fusionAIze Gate** – connects models, providers, tools, and clients.
- **fusionAIze Lens** – filters, compresses, translates, and focuses context.
- **fusionAIze Fabric** – stores and serves shared context, memory, and knowledge.
- **fusionAIze Grid** – runs the sovereign execution environment.
- **fusionAIze Docs** – observes, monitors, and alerts across the stack.
- **fusionAIzeOS** – orchestrates roles, policies, identities, and collaboration.