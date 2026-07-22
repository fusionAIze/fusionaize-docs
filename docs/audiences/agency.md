# Agencies & Consultancies

Your clients hire you for outcomes. They don't want to think about the infrastructure that delivers those outcomes. fusionAIze gives you a platform to build, deploy, and manage AI agents for your clients — under your brand, on your infrastructure, with the operational controls your contracts demand.

## Why agencies choose fusionAIze

Agencies face three structural challenges when adopting AI:

1. **Client data isolation.** You can't run Client A's proprietary data through the same shared SaaS environment as Client B's.
2. **Margin pressure.** Per-seat and per-token SaaS pricing erodes project profitability at scale.
3. **Knowledge retention.** Client context lives in people's heads. When a team member leaves, so does the institutional knowledge.

fusionAIze addresses all three at the infrastructure level:

| Challenge | fusionAIze's approach |
|-----------|----------------------|
| Data isolation | Multi-tenant deployment with physical or logical separation per client |
| Margin protection | Local model support, open-source core, no per-agent platform fees |
| Knowledge retention | Fabric memory layer persists client context across team changes |

## Multi-tenant deployment

The **Agency** deployment profile supports running isolated environments for each client. Each tenant gets its own Gate namespace, Fabric memory partition, and OS role hierarchy — all managed from a single operator dashboard.

=== "Single-server multi-tenant"

    ```bash
    # Deploy one fusionAIze instance with tenant isolation
    faios deploy --profile agency

    # Create a tenant for each client
    faios tenant create --name client-alpha
    faios tenant create --name client-beta
    faios tenant create --name client-gamma
    ```

    Each tenant is a fully isolated workspace. Agents under `client-alpha` cannot access data, memory, or models assigned to `client-beta`.

=== "Per-client dedicated instances"

    ```bash
    # For clients requiring physical separation
    faios deploy --profile agency --mode dedicated \
      --config ./clients/client-alpha/deploy.yml
    ```

    Dedicated instances run on separate hardware or VMs. Recommended for regulated industries (legal, finance, healthcare) where contractual isolation is required.

### Tenant isolation model

```
fusionAIze Agency Instance
│
├── Tenant: client-alpha
│   ├── Gate namespace: alpha-gate
│   ├── Fabric partition: alpha-memory
│   ├── OS roles: alpha-*
│   └── Models: dedicated or shared pool
│
├── Tenant: client-beta
│   ├── Gate namespace: beta-gate
│   ├── Fabric partition: beta-memory
│   ├── OS roles: beta-*
│   └── Models: dedicated or shared pool
│
└── Agency operator dashboard (cross-tenant visibility)
```

!!! warning "Shared versus dedicated models"
    Local models can be safely shared across tenants because they run inference only — they don't store data. Cloud provider API keys should be configured per tenant to maintain cost isolation and audit trails.

## White-label and brand ownership

fusionAIze is designed for white-label deployment. Your clients interact with AI agents that carry your brand, not ours.

- **No fusionAIze watermark.** Agent responses, dashboards, and client-facing interfaces are brand-clean.
- **Custom agent names.** Deploy "AcmeCorp Content Assistant" — not "fusionAIze Agent #4."
- **Your domain, your URLs.** The operator dashboard and any client-facing interfaces run on your infrastructure under your domain.
- **Configurable terminology.** Rename components to match your service language. Call agents "Digital Team Members" or "AI Associates" — whatever fits your brand.

## Use cases

### Client project automation

Deploy pre-built agent blueprints for common client deliverables:

- **Content agency:** Research → Draft → Edit → SEO-optimize pipeline per client
- **Dev agency:** Code review agent, documentation generator, test writer per project
- **Marketing agency:** Campaign analysis agent, A/B test evaluator, competitor monitor
- **Design agency:** Design system validator, accessibility checker, brand consistency auditor

Each blueprint is a reusable workflow template in [Studio](../products/studio/index.md). Create it once, deploy it for every client who needs it.

```
Studio Blueprint: "Content Pipeline"
    │
    ├── Deploy to client-alpha → alpha-content-pipeline
    ├── Deploy to client-beta  → beta-content-pipeline
    └── Deploy to client-gamma → gamma-content-pipeline
        │
        └── Same blueprint, three isolated tenants, zero duplication
```

### Internal agency operations

Your own agency runs on fusionAIze too:

- **Proposal generator** — drafts SOWs and proposals from past project data
- **Resource allocator** — suggests team assignments based on skills, availability, and project fit
- **Invoice reviewer** — cross-checks time entries against project budgets
- **Knowledge base agent** — answers internal questions from past project documentation

### AI service offering

fusionAIze enables new revenue lines:

- **Managed AI Agent Service** — deploy, monitor, and maintain AI agents for clients as a recurring managed service
- **AI Readiness Audit** — assess a client's workflows and identify automation opportunities
- **Custom Agent Development** — build bespoke agents for client-specific processes
- **AI Training & Enablement** — train client teams on working alongside AI (leverage [Academy](#agency--academy-combo))

## Studio: blueprint authoring for agencies

[Studio](../products/studio/index.md) is fusionAIze's blueprint authoring environment. For agencies, it's the difference between building custom automation for every client and building it once.

=== "Without Studio"

    Every client project starts from scratch. You configure agents, define roles, write policies, test workflows — repeating work you've done before.

=== "With Studio"

    You author a blueprint once. It captures the agent roles, memory structures, Lens compression settings, and OS policies. Deploying to a new client is one command.

```yaml
# Example: A content pipeline blueprint authored in Studio
blueprint:
  name: content-pipeline
  version: "1.4"
  agents:
    - name: researcher
      role: research-analyst
      model: local:llama3.1
      tools: [web_search, document_parser]
    - name: writer
      role: content-writer
      model: local:mistral
      tools: [grammar_check, tone_adjust]
      depends_on: [researcher]
    - name: editor
      role: content-editor
      model: cloud:gpt-4o-mini
      tools: [fact_check, seo_analyze]
      depends_on: [writer]
  memory:
    partitions:
      - brand_voice
      - client_style_guide
      - past_content_library
  policies:
    - agent handoff requires human review
    - editor has final output authority
```

## Agency + Academy combo

[Academy](../products/os/index.md) is fusionAIze's structured learning environment. Agencies use it in two ways:

1. **Internal upskilling** — get your team from "AI-curious" to "AI-operational" with structured learning paths for developers, project managers, and account leads.
2. **Client enablement** — offer AI literacy training as a billable service. Teach client teams how to work effectively with the AI agents you deploy for them.

!!! tip "Training as a differentiator"
    Agencies that offer AI enablement alongside AI deployment win more contracts — and retain clients longer. When your client's team understands how to work with the agents you've built, they get more value, and you get stickier relationships.

## Pricing for agencies

The Agency deployment profile is free in its core (Apache 2.0). Premium features that are particularly relevant for agencies:

| Feature | Value for agencies |
|---------|-------------------|
| **Studio (Premium)** | Blueprint authoring, versioning, and one-click multi-tenant deployment |
| **Signal (Premium)** | Cross-tenant monitoring, health dashboards, cost attribution per client |
| **Advanced Lens (Premium)** | Higher compression ratios → lower cloud model costs passed to clients |
| **Academy (Premium)** | Team training paths, certification, client enablement materials |

!!! note "Transparent pricing for client billing"
    Because fusionAIze's platform costs are predictable (not per-token), you can price your managed AI services with confidence. Know your infrastructure cost before you write the proposal.

## When to move from Solo to Agency profile

If you're currently running the Solo profile and wondering when to upgrade:

- **You have multiple clients** with distinct data isolation needs
- **You're spending time reconfiguring** agents between projects
- **You want team members** to collaborate on the same AI workflows
- **You're starting to offer AI** as a named service line

The migration is straightforward:

```bash
faios profile upgrade --from solo --to agency
```

Your existing agents, memory, and configurations are preserved. The upgrade adds multi-tenancy, white-label options, and the Studio interface.

---

**Next steps:**

- [Deployment profiles](../architecture/deployment.md) — understand the Agency profile in detail
- [Studio documentation](../products/studio/index.md) — start authoring blueprints
- [Signal documentation](../products/signal/index.md) — set up cross-tenant monitoring
- [Academy overview](../products/os/index.md) — plan your team's learning path
