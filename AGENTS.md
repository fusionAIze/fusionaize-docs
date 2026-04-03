# AGENTS.md — fusionAIze Docs

## Project identity

This repository hosts `fusionAIze Docs`, a public Apache-2.0-licensed browser-based operator dashboard for the fusionAIze stack.

fusionAIze Docs provides:

1. unified browser interface for monitoring fusionAIze components,
2. real-time operational visibility across Gate, Grid, Lens, Fabric, and OS,
3. interactive dashboards for health, cost, quality, and collaboration signals,
4. a path toward cross-component operator interventions and policy tuning.

## Naming status

The product, runtime, and GitHub repository use `fusionAIze Docs` identifiers.

## Product priority

The operator dashboard is the product.

Do not turn this repository into a monolithic observability platform, BI suite, or full control plane.

Prioritize:

- intuitive browser interface for operators,
- real-time visibility across fusionAIze components,
- actionable insights over raw data,
- cross-layer signal correlation,
- clean integration with Signal for deeper diagnostics,
- local and cloud deployment flexibility.

## Architecture principles

Use a pragmatic browser-first architecture:

- small dashboard core,
- clear component integration boundaries,
- real-time data streams from fusionAIze components,
- optional extensions for alerts, interventions, and policy tuning,
- operational clarity over dashboard sprawl.

Prefer standard web APIs and real-time protocols first.
If a component can expose metrics via Prometheus or OpenTelemetry, use that before adding custom collectors.

## Supported interaction surfaces

fusionAIze Docs should support these surfaces over time:

### Current

- Browser-based dashboard for operators
- Real-time metrics from Gate and Grid
- Basic health and cost visualizations

### Near term

- Integration with Lens context quality signals
- Integration with Fabric memory signals
- Integration with OS collaboration signals
- Alerting and notification hooks

### Later

- Advanced cross-component correlation views
- Interactive policy tuning interfaces
- Historical trend analysis
- Integration with Signal for deeper diagnostics

## Implementation rules

Implement now:

- real-time data ingestion from Gate and Grid,
- intuitive browser dashboard with health and cost views,
- basic alerting and notification system,
- clean integration with fusionAIze component APIs,
- release and process documentation.

Defer or keep optional:

- heavy analytics and BI features,
- hard-coupled control plane logic,
- mandatory AI-assisted dashboard generation,
- tool-specific integrations when standard metrics APIs already work.

## Code quality rules

- keep modules small and testable
- prefer explicit contracts over implicit behavior
- avoid hidden routing magic
- keep operational failure modes visible in logs and health output
- preserve backwards compatibility where it is intentionally promised

## Workflow rules

Work in small coherent steps.
Prefer commit-sized implementation blocks.
Stop after each major block and summarize what changed, what remains, and what is intentionally deferred.

After every 4 or 5 merged PRs, do a full review pass that includes:

- unit test coverage review
- integration test coverage review
- functional test review against real workflows where possible
- documentation review and update across every relevant Markdown file
- roadmap and process review if the project direction changed
- community-health and security baseline review (`CODE_OF_CONDUCT.md`, `SECURITY.md`, issue templates, PR template, Dependabot, CodeQL)

Follow the branch workflow defined in:

- `docs/process/git-workflow.md`

Default branch model:

- `main`
- `feature/<topic>-<date>`
- `review/<topic>-<date>`
- `hotfix/<topic>-<date>` when production-oriented urgency justifies it

Do not introduce a long-lived `develop` branch unless the repository truly needs one.

## RTK shell command preference

For Codex and other shell-driven agents without stronger native command hooks, prefer RTK-wrapped shell commands whenever applicable.

Use raw commands only when RTK is not available or not a good fit, and state that briefly.

## Documentation rules

Maintain:

- the README as the primary public landing page,
- roadmap documentation,
- architecture, integration, onboarding, and troubleshooting docs for external users,
- release and changelog documentation,
- process documentation for workflow-critical conventions,
- migration notes when external names and runtime names differ.

Do not document features that do not exist.

## Security rules

- never hardcode secrets
- never commit `.env`, keys, databases, sqlite files, or logs
- keep runtime state outside the repo checkout
- treat repo-safety rules as mandatory guardrails, not optional hygiene

## Release rules

- `main` should remain stable and releaseable
- document user-visible changes in `CHANGELOG.md`
- use lightweight semantic versioning in `x.y.z` form
- prefer minor bumps for meaningful features or operational behavior changes
- prefer patch bumps for fixes, polish, and small compatibility updates
- reserve major bumps for explicit breaking changes and documented migrations
