# DSGVO / GDPR Compliance

Data protection is not an afterthought in fusionAIze — it's a design principle. The General Data Protection Regulation (GDPR / DSGVO) sets the global standard for personal data protection, and fusionAIze is architected to support compliance by default, not by workaround.

This document explains how fusionAIze's architecture maps to GDPR requirements and what you need to know as an operator deploying fusionAIze in a GDPR-governed context.

!!! note "This is not legal advice"
    This document describes fusionAIze's technical architecture as it relates to GDPR compliance. It does not constitute legal advice. You should consult your Data Protection Officer (DPO) or legal counsel for specific compliance guidance related to your use case.

## The fundamental shift: on-premise deployment

Most AI platforms operate as SaaS: your data is processed on their servers, by their infrastructure, in jurisdictions they choose. GDPR compliance in that model requires complex Data Processing Agreements (DPAs), Standard Contractual Clauses (SCCs), and trust in third-party security practices.

fusionAIze takes a simpler approach: **you run the software, you control the data.**

| Concern | SaaS AI platform | fusionAIze on-premise |
|---------|-----------------|----------------------|
| Where is data processed? | Provider's cloud (may be outside EU) | Your infrastructure, your jurisdiction |
| Who has access? | Provider's staff, subcontractors | Your team, under your access controls |
| Where are models hosted? | Provider's infrastructure | Your servers (local models) or provider you explicitly choose |
| Who handles deletion? | Provider's retention policies | You control storage and deletion directly |
| Is a DPA needed? | Yes — complex third-party agreement | Not for fusionAIze itself (you operate it) |

When you deploy fusionAIze on your own hardware with local models, **no personal data leaves your infrastructure through the AI pipeline.** Prompts, responses, context documents, and agent memory all remain within your controlled environment.

```bash
# Full GDPR-compatible deployment: everything on your hardware
faios deploy --profile smb --mode on-premise

# Use only local models — zero outbound AI traffic
faios model pull llama3.1:8b
faios model pull mistral:7b
```

## Local model support: data never leaves your infrastructure

The most significant GDPR risk in AI adoption is sending personal data to external model providers. Every prompt you send to a cloud AI API potentially transfers personal data to a third-party processor — often in jurisdictions with different privacy standards.

fusionAIze's local model support eliminates this risk entirely:

```yaml
# Gate configuration: local-only, no cloud providers
gate:
  providers:
    - id: local_llama
      type: ollama
      model: llama3.1:8b
      location: on-premise  # runs on your hardware
    - id: local_mistral
      type: ollama
      model: mistral:7b
      location: on-premise

  # Explicitly disabled — no data can leave
  cloud_providers: []
```

When a model runs on your hardware:

- Prompts are processed in your server's RAM
- Responses are generated locally and returned directly to your application
- No prompt text, context documents, or generated output is transmitted to an external service
- Model weights are loaded once and used entirely locally

!!! tip "Mixed deployment for non-personal data"
    You can configure Gate to route only non-personal-data workloads to cloud models while keeping personal-data workloads local. See the [Gate documentation](../products/gate/index.md) for content-based routing rules.

## Data processing, storage, and deletion

### Where data lives in fusionAIze

| Data category | Storage location | Your control |
|--------------|-----------------|-------------|
| Agent prompts and responses | Gate logs (local) | Configurable retention period; delete on demand |
| Document context and embeddings | Fabric memory store (local) | Full CRUD via API; delete individual documents or entire partitions |
| Agent execution traces | Grid logs (local) | Configurable retention; exportable for audit |
| User and role definitions | OS configuration (local file or database) | Direct file or database access |
| Blueprint definitions | Studio storage (local) | Version history with delete capability |

All data stores are local to your deployment. There is no hidden telemetry, no usage data collection, and no external analytics. fusionAIze does not phone home.

### Data deletion

fusionAIze supports granular data deletion to comply with GDPR Article 17 (Right to Erasure):

```bash
# Delete all data related to a specific data subject
faios privacy delete --subject-id user-42

# This removes:
# - All prompts and responses associated with user-42 from Gate logs
# - All context documents and embeddings for user-42 from Fabric
# - All agent execution traces for user-42 from Grid
# - User profile and role assignments from OS
```

For programmatic integration with your existing deletion workflows:

```python
from fusionaize_sdk import PrivacyManager

privacy = PrivacyManager()

# GDPR Article 17: Right to erasure
await privacy.delete_subject_data(
    subject_id="user-42",
    include_derived_data=True,  # embeddings, cached context
    generate_audit_report=True  # document what was deleted
)
```

### Data minimization

fusionAIze's architecture encourages data minimization by design:

- **Lens compression** reduces the amount of context data that passes through the pipeline, minimizing exposure of unnecessary personal data
- **Fabric partitioning** lets you isolate personal data by purpose, making it straightforward to identify and delete data related to specific processing activities
- **Agent role scoping** ensures agents only see the data they need for their specific function — a customer support agent doesn't have access to HR records, and vice versa

## Data Processing Agreement (DPA)

When you self-host fusionAIze, you are the data controller and the platform operator. fusionAIze GmbH does not process your data — we provide software that you run.

For organizations that use fusionAIze's EU-based cloud hosting (Hetzner), a DPA is available upon request:

- **Controller-to-Processor DPA** covering fusionAIze GmbH's limited role as infrastructure provider
- Incorporates the EU Standard Contractual Clauses (SCCs) for international data transfers
- Documents technical and organizational measures (TOMs) in place at our hosting provider

Contact [privacy@fusionaize.com](mailto:privacy@fusionaize.com) to request the current DPA.

## EU-based hosting

For organizations that prefer managed infrastructure over self-hosting, fusionAIze offers EU-based hosting through Hetzner (German data centers):

| Hosting attribute | Detail |
|------------------|--------|
| **Data center location** | Germany (Nuremberg, Falkenstein) or Finland (Helsinki) |
| **Jurisdiction** | EU / German data protection law |
| **Certifications** | ISO 27001 (Hetzner infrastructure) |
| **Data processing** | fusionAIze GmbH as processor under DPA |
| **Sub-processors** | Hetzner Online GmbH (infrastructure); no AI model sub-processors when using local models |

!!! info "Self-hosting is the default recommendation"
    For maximum GDPR compliance simplicity, we recommend self-hosting. When you run fusionAIze on your own infrastructure with local models, the analysis is straightforward: you're the controller, you operate the processing, and no personal data leaves your environment. Our EU hosting option is available for teams that prefer managed infrastructure.

## No third-party data sharing

fusionAIze does not:

- Share your data with third parties for any purpose
- Use your data to train models (we don't operate model training infrastructure)
- Sell or monetize your data
- Send telemetry or usage data to external services
- Integrate with advertising or tracking networks

The software you run is the software you get. There are no hidden data flows.

## Practical GDPR checklist for fusionAIze operators

| Requirement | How to satisfy with fusionAIze |
|------------|-------------------------------|
| **Lawful basis for processing** | You define which data your agents process — you establish the legal basis under Article 6 |
| **Data Processing Agreement** | Not required for self-hosting (you operate the software); available for EU hosting |
| **Data Protection Impact Assessment (DPIA)** | Document your agent workflows, data flows, and access controls; fusionAIze's architecture supports DPIA documentation |
| **Right of access (Art. 15)** | Query Gate logs, Fabric stores, and Grid traces to produce subject access reports |
| **Right to erasure (Art. 17)** | Use `faios privacy delete --subject-id` for automated deletion across all components |
| **Data portability (Art. 20)** | Export Gate logs, Fabric memories, and agent outputs in structured JSON format |
| **Privacy by design (Art. 25)** | On-premise deployment, data minimization through Lens compression, role-based access controls |
| **Records of processing (Art. 30)** | Signal monitoring provides automatic activity logging suitable for processing records |
| **Breach notification (Art. 33/34)** | Signal alerting can detect anomalies and notify your DPO through configured channels |
| **Cross-border transfers (Art. 44-49)** | Data stays in your jurisdiction when self-hosted; EU-based hosting available for managed deployments |

## Data Protection Officer contact

For privacy-related inquiries, DPA requests, or data protection questions:

- **Email:** [privacy@fusionaize.com](mailto:privacy@fusionaize.com)
- **Response time:** Within 72 hours for privacy-related inquiries
- **Postal address:** Available upon request

---

**Next steps:**

- [On-premise & sovereignty](../compliance/sovereignty.md) — data locality and infrastructure control
- [Security practices](../compliance/security.md) — technical security measures
- [Deployment architecture](../architecture/deployment.md) — choose your deployment model
- [Lens documentation](../products/lens/index.md) — understand data minimization through context compression
