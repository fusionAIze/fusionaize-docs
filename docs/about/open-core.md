# Open-Core Model

fusionAIze follows an **open-core model** — the foundational stack is free and open source under Apache 2.0, while premium features, enterprise tooling, and commercial extensions are source-available or proprietary.

This isn't a compromise. It's a deliberate architectural decision that aligns our incentives with the people who depend on fusionAIze every day.

---

## Why open-core

We believe three things simultaneously:

1. **Trust requires transparency.** If you can't see how your AI infrastructure handles data, routes requests, and stores context, you can't trust it. Open source is not a nice-to-have; it's the structural foundation for trust in AI operations.

2. **Sustainability requires revenue.** Maintaining a platform of this complexity — Gate, Lens, Fabric, Grid, faios — takes serious, ongoing investment. Goodwill and GitHub stars don't pay maintainers.

3. **The value lies in the operating logic, not the individual components.** Giving away the core stack builds trust and adoption. Charging for enterprise deployment profiles, governance suites, and Academy access funds the work. Both are necessary; neither alone is sufficient.

The open-core model lets us honour all three commitments without pretending the economics don't matter.

---

## License tiers

### Tier 1: Public Open Source — Apache 2.0

All core components are released under the **Apache License, Version 2.0**.

| Component | Repository | License |
|-----------|------------|---------|
| Gate `faigate` | `git.langevc.com/fusionaize/faigate` | Apache 2.0 |
| Lens `failens` | `git.langevc.com/fusionaize/failens` | Apache 2.0 |
| Fabric `faifabric` | `git.langevc.com/fusionaize/faifabric` | Apache 2.0 |
| Grid `faigrid` | `git.langevc.com/fusionaize/faigrid` | Apache 2.0 |
| faios `faios` | `git.langevc.com/fusionaize/faios` | Apache 2.0 |

With Apache 2.0, you can:

- Use the software for any purpose, commercial or non-commercial.
- Modify, distribute, and sublicense the code.
- Integrate it into proprietary products.
- Distribute modified versions under different terms.

You must:

- Include the original copyright notice and license in any distribution.
- State significant changes made to the original code.
- Not use fusionAIze trademarks in ways that suggest endorsement.

### Tier 2: Source-Available

Extended stack components are **source-available** — you can view, inspect, and audit the code, but commercial use, redistribution, and modification are restricted.

| Component | License type | Rationale |
|-----------|-------------|-----------|
| Studio `faistudio` | Source-available | Blueprint authoring is a premium workflow; the source is transparent but not freely redistributable. |
| Signal `faisignal` | Source-available | Operational intelligence dashboards are available for audit and customisation under commercial agreement. |
| SDK `faisdk` | Apache 2.0 | The SDK is open — we want developers integrating fusionAIze into their stack without friction. |

!!! info "Transparency without commoditisation"
    Source-available licenses let you see exactly how Studio and Signal work — inspect the code, verify security claims, understand data flows. They don't let you fork them and compete with the project that funds their development.

### Tier 3: Private / Proprietary

Commercial extensions and enterprise features are **proprietary**:

- **Enterprise deployment profiles** — multi-node Grid deployments with advanced orchestration.
- **Governance suite** — fine-grained RBAC, audit trails, compliance reporting for regulated industries.
- **Academy enterprise tier** — custom training paths, private instance, SSO integration.
- **Managed Agency services** — operated fusion teams with SLAs and dedicated support.
- **Premium support** — SLAs, dedicated support engineers, priority bug fixes.

These tiers fund the core open-source work. Every enterprise customer directly supports the improvement of the Apache 2.0 components every fusionAIze user depends on.

---

## Why Apache 2.0

We chose Apache 2.0 over GPL, MIT, and BSL after careful deliberation.

| Aspect | Apache 2.0 |
|--------|------------|
| **Permissiveness** | Allows integration into proprietary products — essential for enterprise adoption. |
| **Patent protection** | Explicit patent grant protects both contributors and users from patent litigation. |
| **Attribution** | Requires attribution without imposing copyleft restrictions that would block commercial use. |
| **Enterprise familiarity** | Apache 2.0 is the most widely adopted and legally tested permissive license in enterprise software. |
| **Ecosystem compatibility** | Compatible with GPLv3 and most other open-source licenses, maximising integration potential. |

!!! note "What Apache 2.0 does NOT do"
    Apache 2.0 does not require you to open-source modifications. It does not impose copyleft. It does not restrict commercial use. This is intentional — we want fusionAIze embedded deeply into the software ecosystem, and restrictive licensing inhibits adoption.

---

## Practical impact

### For individual developers and small teams

The core stack is fully functional under Apache 2.0. You can run Gate, Lens, Fabric, Grid, and faios on your own hardware, for any purpose, without paying a cent. You get the same core infrastructure that enterprise customers use.

### For freelancers and agencies

Apache 2.0 lets you embed fusionAIze into client projects without worrying about license contamination. Build fusion teams for your clients. Charge for your expertise. The software doesn't get in the way.

### For SMEs and mid-market

Run the Apache 2.0 stack with full data sovereignty — on-premise, in your cloud, however you need. If you need enterprise governance, SSO, or managed services, the commercial tiers are available.

### For enterprise

The open-core model gives your legal and compliance teams full visibility into the software you're deploying. The commercial tiers add the governance, support, and SLAs required for regulated environments.

---

## Commitment

fusionAIze commits to:

- **Never rug-pulling** the open-source core. Components released under Apache 2.0 will remain under Apache 2.0.
- **Transparent licensing** — we will never surprise you with license changes. Any license evolution will be announced well in advance, with clear migration paths.
- **Community governance** — significant architectural decisions are discussed openly, and community input shapes the roadmap.
- **Sustainable investment** — commercial revenue is reinvested into the platform, not extracted by investors who don't understand what we're building.

[:fontawesome-solid-arrow-right: License details](../legal/license.md){ .md-button }
[:fontawesome-solid-arrow-right: Contributing](../contributing/index.md){ .md-button }
[:fontawesome-solid-arrow-right: Roadmap](roadmap.md){ .md-button }
