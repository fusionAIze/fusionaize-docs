# The Capacium Universe

Capacium is the **capability packaging infrastructure** for AI agents. It provides the primitives for packaging discrete AI capabilities, discovering them across an ecosystem, verifying their behaviour, and establishing trust between capability authors and consumers.

fusionAIze is the operating brand and product stack built on top of Capacium — maintained by the same organisation, sharing the same vision, and contributing to the same open-source ecosystem.

---

## What is Capacium?

Most AI tools are monolithic: a single application that bundles a specific set of capabilities. Capacium takes a different approach: it treats every AI capability as a discrete, self-describing, independently verifiable unit.

Think of Capacium as the **operating system for AI capability distribution** — what package managers did for software libraries, Capacium does for AI agent capabilities.

### Core primitives

| Primitive | Description |
|-----------|-------------|
| **Capability packaging** | A standard format for describing, bundling, and distributing AI capabilities. A capability package declares its interface, dependencies, resource requirements, expected inputs and outputs, and behavioural guarantees. |
| **Discovery** | A registry and search system that lets agents, developers, and platforms discover available capabilities by purpose, interface, quality, and trust signals. |
| **Verification** | Automated testing and behavioural analysis that verifies a capability does what it claims. Verification results are published as attestations. |
| **Trust fabric** | A reputation and attestation system that allows capability consumers to make informed trust decisions — who built this, has it been verified, what do other consumers report? |

---

## Capacium + fusionAIze

Capacium is the **infrastructure layer**. fusionAIze is the **operating brand and product stack** built on that layer.

```
┌─────────────────────────────────────────────────┐
│                                                 │
│              fusionAIze                         │
│    (Operating Brand, Product Stack)             │
│                                                 │
│    Gate · Lens · Fabric · Grid · faios          │
│    Studio · Signal · SDK                        │
│    Academy · Agency · Services                   │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│              Capacium                           │
│    (Capability Packaging Infrastructure)        │
│                                                 │
│    Packaging · Discovery · Verification         │
│    Trust Fabric · Registry                      │
│                                                 │
└─────────────────────────────────────────────────┘
```

fusionAIze components (Gate, Lens, Fabric, Grid) consume and produce Capacium capability packages. A Lens compression profile, a Grid runner profile, a Fabric knowledge schema — these are all Capacium capabilities under the hood. When you configure Gate with a new provider, you're using a Capacium-packaged provider adapter.

Capacium is the substrate. fusionAIze is what you interact with.

---

## The Capacium organisation

Both Capacium and fusionAIze are maintained by the same organisation — **LangeVC** — under a shared governance model:

- **Capacium infrastructure and spec** — Apache 2.0, community-governed, open RFC process for new features.
- **fusionAIze product stack** — Open-core, product-driven, with commercial extended-stack components funding ongoing development.

This separation ensures that the capability packaging infrastructure remains a neutral, community-owned substrate, while fusionAIze competes as a product built on that substrate. Anyone can build on Capacium — fusionAIze is the first, and most complete, product to do so.

[:fontawesome-solid-arrow-right: docs.capacium.xyz](https://docs.capacium.xyz){ .md-button }

---

## Ecosystem projects

LangeVC maintains and contributes to multiple projects in the Capacium ecosystem:

### fusionAIze
The operating platform for human-AI fusion teams. Gate, Lens, Fabric, Grid, faios — the complete stack for deploying and operating AI-powered virtual employees.

### SkillWeave
A multi-agent AI development workflow system. SkillWeave provides the orchestration fabric for complex AI development processes: PRD generation through guided interviews (Blueprint), multi-model council deliberation (Council), dependency-aware prompt chain execution (PromptChain Execute), and full release pipelines with Ralph Loop-powered iterative development (ReleaseChain).

[:fontawesome-solid-arrow-right: SkillWeave on GitHub](https://github.com/LangeVC/skillweave)

### Elementeer
An intelligent assistant for Elementor-based WordPress sites. Elementeer provides 172+ MCP tools for reading, editing, and managing WordPress content through Elementor and 12 additional page builders — without touching the database or theme files directly.

### Understand Anything
A codebase analysis toolkit that produces interactive knowledge graphs for understanding software architecture, components, and relationships. Works with any codebase, any language.

### MemPalace
A persistent memory system for AI agents using the AAAK compressed memory format. MemPalace provides wings, rooms, and drawers for organising agent memory with cross-wing tunnels for connecting related knowledge.

### txtHumanizer
A three-stage German-language text humaniser that removes AI-typical patterns and makes text more natural, using Wikipedia's AI-detection criteria as its analytical foundation.

---

## The LangeVC ecosystem

LangeVC is the organisation behind Capacium and fusionAIze. The ecosystem spans:

| Layer | Projects |
|-------|----------|
| **Infrastructure** | Capacium (capability packaging) |
| **Platform** | fusionAIze (human-AI fusion teams) |
| **Workflows** | SkillWeave (multi-agent orchestration), SkillWeave Council (multi-model deliberation) |
| **Applications** | Elementeer (WordPress AI), Understand Anything (code analysis) |
| **Tooling** | MemPalace (agent memory), txtHumanizer (text quality) |

Everything LangeVC builds shares a common philosophy:

- **Open-core where possible.** Core infrastructure and specifications are open-source. Premium capabilities fund ongoing development.
- **Deploy where you trust.** Self-hosted, on-premise, sovereign. No cloud lock-in.
- **Agents are colleagues, not tools.** Every project treats AI agents as team members with defined roles, persistent memory, and operational boundaries.
- **Capabilities are packages.** Discrete, discoverable, verifiable. The Capacium model applies at every layer.

---

## The vision

The Capacium ecosystem exists to answer a single question: **what would the software industry look like if AI capabilities were as easy to package, discover, verify, and trust as software libraries are today?**

We're building toward a future where:

1. An AI agent can discover a capability it needs from a registry — the same way a developer pulls a library from npm or PyPI.
2. That capability comes with verified behavioural guarantees — not just a README, but machine-verifiable attestations.
3. The agent's operating system (fusionAIze) enforces boundaries, manages memory, and routes execution appropriately.
4. Humans and AIs collaborate in defined roles with persistent context — not as tool and user, but as colleagues.

The path there is long. Capacium is the substrate. fusionAIze is the first complete product. The ecosystem is growing.

---

[:fontawesome-solid-globe: docs.capacium.xyz](https://docs.capacium.xyz){ .md-button }
[:fontawesome-solid-arrow-right: fusionAIze vision](vision.md){ .md-button }
[:fontawesome-solid-arrow-right: Platform overview](platform.md){ .md-button }
