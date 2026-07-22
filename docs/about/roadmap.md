# Roadmap

fusionAIze is built in the open. This roadmap reflects our current priorities and planned trajectory — it is a living document that evolves with community input and operational experience.

---

## Current state

The core stack is operational and under active development:

| Component | Status | Notes |
|-----------|--------|-------|
| **Gate** `faigate` | :fontawesome-solid-check:{ style="color: #C4D900" } Stable | Multi-provider routing, cost tracking, access control. In production use. |
| **Lens** `failens` | :fontawesome-solid-check:{ style="color: #C4D900" } Stable | Context compression, relevance filtering, explanation traces. |
| **Fabric** `faifabric` | :fontawesome-solid-check:{ style="color: #C4D900" } Stable | Semantic memory, episodic memory, knowledge graph foundation. |
| **Grid** `faigrid` | :fontawesome-solid-check:{ style="color: #C4D900" } Stable | Containerised execution, resource isolation, audit logging. |
| **faios** `faios` | :fontawesome-solid-gear:{ style="color: #FFAA19" } Evolving | Role definitions, policy engine, handover protocols. |

---

## Near-term — Q3/Q4 2026

### SDK stabilisation

The `faisdk` reaches v1.0 with stable, documented libraries for Python, TypeScript, and Go. This is the highest-priority item because it unlocks every integration scenario — embedding fusionAIze into existing tools, CI/CD pipelines, and custom applications.

```python
# The SDK v1.0 developer experience
from fusionaize import FusionClient

client = FusionClient(gate_url="http://localhost:8120")
result = client.run(
    task="Review pull request #342",
    role="code_reviewer",
    context={"repository": "faigate", "language": "python"}
)
print(result.output)
```

**Key deliverables:**

- Stable Python SDK with full Gate, Fabric, and Lens integration
- TypeScript SDK for web and Node.js environments
- Go SDK for infrastructure and CLI tooling
- Comprehensive documentation with real-world examples
- Backward-compatibility guarantees from v1.0

### Studio alpha

`faistudio` opens to alpha users — a browser-based environment for designing, testing, and refining virtual employee behaviour.

**Alpha scope:**

- Visual workflow designer for virtual employee roles
- Built-in test harness with replay and iteration
- Template library for common fusion team patterns
- Export-to-faios for deployment

### Signal preview

`faisignal` ships a preview release with foundational observability.

**Preview scope:**

- Real-time cost dashboard across Gate-routed providers
- Quality scoring with trend detection
- Basic anomaly alerts for cost and latency
- Integration with existing monitoring stacks (Prometheus, Grafana)

---

## Mid-term — 2027

### Enterprise deployment profiles

Multi-node Grid deployments with advanced orchestration, targeting enterprise production environments.

- High-availability Grid clusters with automatic failover
- Federated Fabric deployments across regions and teams
- Enterprise SSO integration (SAML, OIDC)
- Fine-grained RBAC with audit-compliant logging

### Academy platform

The fusionAIze Academy launches as a standalone product — not just documentation, but a structured enablement platform.

- **Fusion Team Fundamentals** — core certification track
- **Role-based learning paths** — operator, developer, team lead, architect
- **Playbook library** — reusable collaboration patterns for common scenarios
- **Assessment and certification** — validate fusion team readiness
- **Enterprise training instances** — private Academy deployments with custom content

### Signal v1.0

Full operational intelligence platform.

- Collaboration metrics — handover quality, context utilisation, fusion team health
- Predictive analytics — cost forecasting, capacity planning
- Custom dashboard builder
- Advanced alerting with team-aware notification routing

---

## Long-term — 2028+

### Full fusion team operating system

The long-term vision: fusionAIze as the complete operating system for human-AI collaboration.

- **Virtual employee lifecycle management** — hire, onboard, evaluate, promote, retire AI colleagues with the same intentionality as human team members.
- **Cross-organisation fusion teams** — multi-party Fabric for collaboration across organisations with sovereign data boundaries.
- **Fusion team analytics** — measure and optimise the health and productivity of human-AI collaboration at the team level, not just the individual level.
- **Adaptive team composition** — faios recommends optimal fusion team structures based on project characteristics, team history, and capability profiles.

### Ecosystem

- **Plugin marketplace** — community and commercial plugins for Gate, Lens, Fabric, and Grid.
- **Certified partner programme** — agencies and consultancies trained and certified to design and operate fusion teams.
- **Fusion team maturity model** — a structured framework for organisations to assess and improve their human-AI collaboration capability.

---

## How to influence the roadmap

The fusionAIze roadmap is shaped by the community that uses it. Here's how to contribute:

### 1. Open an issue

The primary mechanism for feature requests and priority feedback is the issue tracker on our Forgejo instance.

```bash
# Browse open issues
git.langevc.com/fusionaize/faigate/issues
```

Use the `roadmap` label to signal that your request is about future direction.

### 2. Join the discussion

Roadmap discussions happen in the open:

- **Forgejo issues** — technical feature requests and bug reports
- **GitHub Discussions** (mirror) — broader strategy and use-case conversations
- **Community calls** — periodic open calls where the maintainers share progress and gather input

### 3. Contribute

The fastest way to move something up the roadmap is to help build it. Pull requests — especially for SDK improvements, provider integrations, and documentation — are reviewed promptly.

[:fontawesome-solid-code-pull-request: Contributing guide](../contributing/index.md){ .md-button }

### 4. Commercial partnership

Enterprise customers and commercial partners have a dedicated channel for roadmap input. Commercial relationships directly fund the core development work and naturally influence prioritisation.

[:fontawesome-solid-envelope: Contact us](mailto:hello@fusionaize.com){ .md-button }

---

!!! info "This is a living document"
    Roadmaps change — that's a feature, not a flaw. As we ship, learn from users, and observe how fusion teams actually operate in production, our priorities will evolve. Significant changes to this roadmap will be discussed openly before they're committed.

---

[:fontawesome-solid-arrow-right: Vision & Mission](vision.md){ .md-button }
[:fontawesome-solid-arrow-right: Platform overview](platform.md){ .md-button }
[:fontawesome-solid-arrow-right: Get started](../getting-started/index.md){ .md-button }
