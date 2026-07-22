# Enterprise

fusionAIze's enterprise capabilities are under active development. This document describes the vision, the architecture, and what's available today — so your security, compliance, and architecture teams can evaluate fusionAIze against your requirements now, even as we build toward the full enterprise feature set.

!!! info "Enterprise features: development status"
    The deployment model, security architecture, and core platform are production-ready. Enterprise-specific features — SSO, advanced RBAC, SLA tiers, and dedicated support — are in development with planned availability in stages. See our [public roadmap](../about/roadmap.md) for timelines, and [contact us](mailto:enterprise@fusionaize.com) for early-access discussions.

## Enterprise deployment profile

The **Enterprise** deployment profile is designed for organizations with dedicated infrastructure teams, formal change management processes, and regulatory compliance requirements.

```bash
faios deploy --profile enterprise
```

| Capability | Enterprise configuration |
|-----------|--------------------------|
| **Deployment** | Kubernetes-native, Helm charts, GitOps-ready (ArgoCD / Flux) |
| **High availability** | Multi-node with automatic failover, leader election |
| **Scaling** | Horizontal pod autoscaling for Gate and Grid components |
| **Storage** | External database support (PostgreSQL, external S3-compatible object storage) |
| **Networking** | Internal service mesh, ingress with TLS termination |
| **Observability** | Prometheus metrics, OpenTelemetry traces, structured JSON logging |
| **Backup** | Automated backup scheduling for Fabric memory stores |

### Architecture for enterprise

```
Enterprise Deployment
│
├── Ingress / API Gateway (your existing infrastructure)
│   ├── TLS termination
│   ├── Rate limiting
│   └── WAF integration
│
├── fusionAIze Control Plane
│   ├── Gate (model routing) — HA deployment, 3+ replicas
│   ├── OS (team logic) — centralized policy management
│   └── Signal (monitoring) — enterprise metrics pipeline
│
├── fusionAIze Data Plane
│   ├── Fabric (memory) — PostgreSQL-backed, multi-read-replica
│   ├── Grid (execution) — auto-scaling runner pods
│   └── Lens (context) — per-workload compression workers
│
└── External integrations
    ├── IdP (SSO) — planned
    ├── SIEM (audit log shipping) — planned
    └── Existing enterprise systems (ERP, CRM, DAM) — via SDK
```

## Security and compliance

fusionAIze is designed with enterprise security requirements from the ground up — not bolted on afterward.

### Current security capabilities

| Control | Status | Details |
|---------|--------|---------|
| **On-premise deployment** | Available | Full stack runs within your infrastructure, no external dependencies |
| **Local model support** | Available | Models run on your hardware; no data sent to external AI providers |
| **TLS everywhere** | Available | All component communication encrypted via TLS 1.3 |
| **API authentication** | Available | API key-based auth with token rotation support |
| **Code security** | Available | CodeQL static analysis, Dependabot dependency scanning, gitleaks secret detection in CI |
| **Pre-commit security gates** | Available | Automated checks before code reaches the repository |

### Compliance trajectory

| Standard | Status |
|----------|--------|
| **SOC 2 Type II** | Planned — architecture designed for SOC 2 audit readiness |
| **ISO 27001** | Planned — information security management system alignment in progress |
| **GDPR / DSGVO** | Supported — full on-premise deployment with data locality guarantees. See [GDPR documentation](../compliance/gdpr.md) |
| **EU AI Act** | Aligned — transparent AI roles, human oversight, explainability via Lens. See [EU AI Act documentation](../compliance/eu-ai-act.md) |
| **HIPAA** | On-premise deployment model is architecturally compatible; formal BAAs not yet available |

!!! note "Enterprise compliance review"
    Enterprise customers may request a security architecture review, penetration test results, and compliance documentation under NDA. Contact [enterprise@fusionaize.com](mailto:enterprise@fusionaize.com).

## Identity and access management

### Available today

| Feature | Description |
|---------|-------------|
| API key authentication | Programmatic access with scoped API tokens |
| Role-based access | OS-level role definitions for agent permissions and action scopes |
| Audit trail | All agent actions logged with timestamps, actor identity, and decision rationale |

### In development

| Feature | Planned availability |
|---------|---------------------|
| **SAML/OIDC SSO** | Integrate with Okta, Azure AD, Ping, Keycloak, and other IdPs |
| **SCIM provisioning** | Automated user lifecycle management |
| **Fine-grained RBAC** | Per-component, per-resource access policies |
| **MFA enforcement** | Mandatory multi-factor for operator and administrator roles |
| **Privileged access management** | Just-in-time elevation for sensitive operations |

## Audit logging

fusionAIze generates structured audit events for all significant actions:

```json
{
  "event": "agent.execution.completed",
  "timestamp": "2026-07-19T14:31:22Z",
  "actor": {
    "agent_id": "agent-4f8a2b",
    "agent_role": "content-writer",
    "operator": "user:julia.mueller"
  },
  "action": {
    "type": "text_generation",
    "model": "local:llama3.1:8b",
    "tokens_used": 1247,
    "context_sources": ["fabric:brand-guidelines", "fabric:client-alpha-brief"]
  },
  "result": {
    "status": "success",
    "review_required": true,
    "reviewer": "user:julia.mueller"
  }
}
```

All audit events are structured JSON. They can be shipped to your existing SIEM (Splunk, Elastic, Datadog) for correlation with other security events.

## SLA and support tiers

| Tier | Response time (critical) | Response time (standard) | Availability target |
|------|-------------------------|-------------------------|-------------------|
| **Community** | Best effort | Best effort | Self-managed |
| **Professional** (in development) | 4 hours | 1 business day | 99.5% |
| **Enterprise** (in development) | 1 hour | 4 hours | 99.9% |

Enterprise support includes:

- Dedicated technical account manager
- Quarterly architecture reviews
- Priority bug fixes and feature requests
- Assisted upgrade planning and execution
- On-call escalation path for critical incidents

## Custom virtual employee development

fusionAIze's agent framework is extensible. Enterprise customers can build custom agents tailored to proprietary workflows:

=== "Custom agent definition"

    ```yaml
    # Custom enterprise agent: financial_report_analyst
    agent:
      name: financial_report_analyst
      role: financial-analyst
      model: local:llama3.1:70b
      tools:
        - spreadsheet_reader
        - financial_formula_validator
        - compliance_checker_baFin
      memory:
        partitions:
          - quarterly_templates
          - regulatory_guidelines
          - past_audit_findings
      policies:
        - output requires sign-off by finance director
        - data access limited to finance department
        - model must run on-premise (no cloud)
    ```

=== "Integration via SDK"

    ```python
    from fusionaize_sdk import Agent, Tool, Policy

    # Define a custom tool for enterprise ERP integration
    erp_tool = Tool(
        name="sap_invoice_lookup",
        description="Query SAP for invoice details by ID",
        endpoint="https://internal-sap-api.company.local/v1/invoices",
        auth_type="oauth2_client_credentials",
        rate_limit="100/minute"
    )

    # Create an agent with enterprise integrations
    agent = Agent(
        name="finance_reconciliation_agent",
        role="financial-analyst",
        tools=[erp_tool],
        policy=Policy(
            require_human_review=True,
            data_scope=["finance_department"],
            model_constraint={"location": "on-premise-only"}
        )
    )
    ```

Custom agents can integrate with any internal system that exposes an API — ERP (SAP, Oracle), CRM (Salesforce, HubSpot), document management (SharePoint, Alfresco), or proprietary internal tools. The [SDK](../products/sdk/index.md) provides the integration layer.

## Integration with existing enterprise systems

```
fusionAIze Enterprise
│
├── IdP (planned)
│   ├── Okta / Azure AD / Ping / Keycloak
│   └── SCIM user provisioning
│
├── Observability
│   ├── Prometheus / Grafana (metrics) ✓
│   ├── OpenTelemetry (traces) ✓
│   └── Splunk / Elastic / Datadog (logs) ✓
│
├── Enterprise Systems (via SDK)
│   ├── ERP (SAP, Oracle, Microsoft Dynamics)
│   ├── CRM (Salesforce, HubSpot, Microsoft Dynamics)
│   ├── DAM (Adobe, Bynder, custom)
│   └── Internal APIs and microservices
│
└── Infrastructure
    ├── Kubernetes (EKS, AKS, GKE, OpenShift)
    ├── Helm-based deployment ✓
    └── GitOps (ArgoCD, Flux) ✓
```

## Data residency and sovereignty

For enterprises operating in regulated jurisdictions or with data sovereignty requirements, fusionAIze's on-premise and private-cloud deployment models provide full control:

- **Deploy in your own VPC** (AWS, Azure, GCP) or on bare-metal in your data center
- **No data egress** to external AI services when using local models
- **EU-based infrastructure** available (see [sovereignty documentation](../compliance/sovereignty.md))
- **Air-gapped deployment** support for classified or high-security environments

## Current status and getting involved

Enterprise features are developed in the open. You can track progress:

- [Public roadmap](../about/roadmap.md) — feature timelines and milestones
- [GitHub repository](https://github.com/fusionAIze/faigate) — issues, discussions, and contribution guidelines
- [Enterprise mailing list](mailto:enterprise@fusionaize.com) — early access, design partnerships, and evaluation support

!!! tip "Evaluate fusionAIze in your environment today"
    The core platform is production-ready. You can deploy the on-premise profile in your infrastructure today, run local models, and begin evaluating agent workflows. The enterprise features under development (SSO, RBAC, SLAs) are additive — they layer on top of the existing platform without requiring migration.

---

**Next steps:**

- [Deployment architecture](../architecture/deployment.md) — enterprise deployment patterns
- [Security model](../architecture/security.md) — technical security architecture
- [Compliance documentation](../compliance/gdpr.md) — GDPR, EU AI Act, and sovereignty
- [SDK documentation](../products/sdk/index.md) — integrate with existing systems
- [Contact enterprise team](mailto:enterprise@fusionaize.com) — schedule an architecture review
