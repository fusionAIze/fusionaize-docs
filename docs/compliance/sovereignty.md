# Data Sovereignty & On-Premise

Data sovereignty is the principle that data is subject to the laws of the country where it is stored and processed. For many organizations — European public sector bodies, regulated industries, critical infrastructure operators — cloud AI services that process data in foreign jurisdictions are not an option. fusionAIze is built for these organizations.

## Why sovereignty matters for AI

When you send a prompt to a cloud AI API, you don't know:

- **Where** the data is physically processed
- **Which jurisdiction's** laws apply to that processing
- **Who** has administrative access to the servers
- **Whether** the data is logged, retained, or used for model training
- **If** the provider's subcontractors have access to your data

For a casual user asking about dinner recipes, this uncertainty is acceptable. For a hospital processing patient records, a law firm analyzing privileged documents, or a government agency handling classified information, it is not.

!!! quote "Schrems II and the reality of international data transfers"
    The Court of Justice of the European Union's *Schrems II* decision (2020) invalidated the EU-US Privacy Shield and imposed heightened requirements on international data transfers. For organizations handling sensitive personal data, the cleanest compliance strategy is to avoid transferring data across jurisdictions entirely. fusionAIze's on-premise architecture makes this practical for AI workloads.

## fusionAIze's sovereignty architecture

fusionAIze is built on a simple premise: **AI infrastructure should run where your data lives, not the other way around.**

```
Traditional Cloud AI:
Your Data → [Internet] → Provider's Server (US/EU/Unknown) → Model → Response
                                                                    │
                                              Data logged? Retained? Training?
                                              Subcontractors? Jurisdiction?

fusionAIze On-Premise:
Your Data → Your Server → Local Model → Response
    │
    └── Everything stays within your controlled environment
        Physical location: your choice
        Jurisdiction: your local law
        Access: your team only
```

## Deployment options for sovereignty

fusionAIze supports a spectrum of deployment models, each providing a different level of data sovereignty:

### Tier 1: Full on-premise (maximum sovereignty)

Everything runs on your hardware, in your facility, under your physical control.

```bash
faios deploy --profile smb --mode on-premise --air-gapped
```

| Attribute | Detail |
|-----------|--------|
| Servers | Your own hardware, your data center |
| Models | Downloaded once, run locally thereafter |
| Internet | Not required after initial model download |
| Data egress | Zero — no outbound AI traffic |
| Physical access | Your team, your security |
| Jurisdiction | Your country's laws |

This is the recommended configuration for: government agencies, defense contractors, critical infrastructure, hospitals handling patient data, and any organization where data sovereignty is a hard requirement.

### Tier 2: Private cloud (strong sovereignty)

fusionAIze runs on dedicated infrastructure in a private cloud — your own VPC (Virtual Private Cloud) on AWS, Azure, or GCP, or a European cloud provider.

```bash
faios deploy --profile enterprise --mode private-cloud
```

| Attribute | Detail |
|-----------|--------|
| Servers | Dedicated VMs or bare-metal in your cloud account |
| Region | You select the region (e.g., eu-central-1, eu-west-3) |
| Models | Local models run on your VMs; cloud models optional |
| Data egress | Minimal — manageable for compliance review |
| Physical access | Cloud provider data center (with your encryption keys) |
| Jurisdiction | Region you select |

Recommended for: enterprises with existing cloud infrastructure who need strong data locality assurances without managing physical hardware.

### Tier 3: EU-managed hosting (standard sovereignty)

fusionAIze GmbH provides managed hosting on Hetzner infrastructure in German and Finnish data centers.

```bash
# Managed deployment — fusionAIze GmbH handles infrastructure
faios deploy --profile smb --mode managed-eu
```

| Attribute | Detail |
|-----------|--------|
| Servers | Dedicated servers at Hetzner (Germany / Finland) |
| Region | EU only |
| Models | Local models run on your dedicated servers |
| Data egress | Within EU |
| Access | fusionAIze operations team + your administrators |
| Jurisdiction | German / EU law |
| DPA | Available — controller-to-processor agreement |

Recommended for: organizations that prefer managed infrastructure while maintaining EU data residency, and whose data sensitivity allows for a managed service model.

## Local models: the sovereignty enabler

Cloud AI's sovereignty problem starts with the model. When you call an API, your data is processed on servers you don't control, by a company you have limited contractual leverage over. Local models change the equation entirely.

fusionAIze supports running models entirely on your hardware:

| Model | Size | Capability level | Runs on |
|-------|------|-----------------|---------|
| Llama 3.1 8B | ~5 GB | Strong general purpose | Laptop, workstation |
| Llama 3.1 70B | ~40 GB | Near cloud-tier reasoning | Server with GPU |
| Mistral 7B | ~4 GB | Excellent structured output | Laptop, workstation |
| Qwen 2.5 7B | ~4 GB | Strong multilingual (EU languages) | Laptop, workstation |
| Phi-3 Mini | ~2 GB | Compact, runs anywhere | Laptop (even without GPU) |

!!! tip "Model selection for regulated environments"
    All models listed above are available under permissive licenses (Apache 2.0, MIT, or equivalent). You own the model files on your disk. There is no ongoing relationship with the model creator — no API calls, no telemetry, no usage reporting.

## Air-gapped deployment

For the highest-security environments, fusionAIze supports air-gapped deployment: the system runs entirely disconnected from the internet after initial setup.

```bash
# Phase 1: Prepare on a connected machine
faios model pull llama3.1:8b
faios model pull mistral:7b
faios model export --all --output ./model_bundle/

# Phase 2: Transfer to air-gapped environment
# (via approved transfer mechanism — encrypted drive, one-way diode, etc.)

# Phase 3: Deploy on air-gapped machine
faios deploy --profile smb --mode on-premise --air-gapped
faios model import ./model_bundle/
```

In air-gapped mode:

- No internet connectivity required or attempted
- Models are loaded from local storage only
- All networking is local (localhost or internal network)
- Updates are performed via approved transfer mechanisms

## Comparison with cloud-only AI platforms

| Capability | Cloud-only AI (OpenAI, Anthropic, etc.) | fusionAIze on-premise |
|-----------|----------------------------------------|----------------------|
| Data processed in your jurisdiction | Depends on provider's region support | Always — you choose the location |
| Data used for model training | Varies by provider and plan | Never — models run locally |
| Accessible by provider staff | Yes, for operational purposes | Only your team |
| Sub-processor risk | Provider's supply chain | None (for local models) |
| Survives provider outage | No — dependent on their infrastructure | Yes — fully self-contained |
| Survives provider policy change | No — subject to their terms | Yes — open source, no dependency |
| Subject to foreign surveillance laws | Yes (US CLOUD Act, FISA, etc.) | No — local jurisdiction only |
| Independent security audit | Provider's infrastructure, limited visibility | Full — your infrastructure, your audit |

## German and European infrastructure

fusionAIze GmbH is a German company. Our operations, development, and infrastructure are European by default:

| Aspect | Detail |
|--------|--------|
| **Company jurisdiction** | Germany |
| **Applicable law** | German and EU law |
| **Development** | Europe-based team |
| **Managed hosting** | Hetzner (German/Finnish data centers) |
| **Source code** | Apache 2.0, self-hosted Forgejo |
| **Community** | Global, European-majority |

For European public sector organizations, this means fusionAIze can satisfy procurement requirements that mandate EU-based vendors and EU-based infrastructure.

!!! info "Gaia-X and European cloud initiatives"
    fusionAIze's architecture aligns with European digital sovereignty initiatives like Gaia-X. The on-premise, private-cloud, and EU-managed deployment models give you control over digital infrastructure that cloud-only solutions cannot provide. We're tracking Gaia-X federation standards for potential future integration.

## Practical sovereignty checklist

| Requirement | fusionAIze approach |
|------------|-------------------|
| Data stored in specified jurisdiction | On-premise deployment: your choice of location |
| No unauthorized cross-border transfers | Local models = no outbound AI traffic |
| Access limited to authorized personnel | Your access controls, your identity provider |
| Encryption at rest and in transit | TLS 1.3 for all component communication; disk encryption at OS level |
| Data deletion upon request | Granular API: `faios privacy delete --subject-id` |
| Sub-processor inventory | None for self-hosted; Hetzner only for managed hosting |
| Breach notification capability | Signal monitoring + configurable alert channels |
| Right to audit | Full — you operate the infrastructure; no restrictions on inspection |

---

**Next steps:**

- [GDPR compliance](../compliance/gdpr.md) — data protection framework
- [Security practices](../compliance/security.md) — technical security measures
- [Deployment architecture](../architecture/deployment.md) — choose your deployment model
- [Enterprise outlook](../audiences/enterprise.md) — enterprise-grade deployment patterns
