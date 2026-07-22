# EU AI Act Compatibility

The European Union's Artificial Intelligence Act (Regulation 2024/1689) establishes the world's first comprehensive legal framework for AI. It classifies AI systems by risk, imposes requirements on providers and deployers, and sets expectations for transparency, human oversight, and accountability.

fusionAIze is designed to help organizations deploy AI responsibly — not to circumvent regulation. This document maps fusionAIze's architecture to the EU AI Act's requirements and explains how the platform supports compliance.

!!! note "The EU AI Act is new law"
    The EU AI Act was published in the Official Journal in July 2024 and entered into force in August 2024. Obligations phase in over 2025–2027. This document reflects our current understanding of the Act and will be updated as regulatory guidance and delegated acts are published. Consult your legal counsel for compliance advice specific to your AI use cases.

## fusionAIze's role: infrastructure, not an AI system

Under the EU AI Act, fusionAIze is **AI infrastructure** — not an AI system in itself. Think of it as the operating system layer that sits between your organization and the AI models you use. fusionAIze does not:

- Train or fine-tune models
- Make autonomous decisions that affect natural persons
- Determine the purpose or use of the AI models routed through it

As the deployer of AI systems built on fusionAIze, **your organization** is responsible for classifying your specific AI use cases under the Act's risk framework and meeting the corresponding obligations. fusionAIze provides the infrastructure to make meeting those obligations practical.

## Transparent AI roles: not black boxes

A core requirement of the EU AI Act is transparency. Users must know they're interacting with an AI system (Article 50), and high-risk systems must provide clear information about their capabilities, limitations, and intended purpose (Article 13).

fusionAIze's agent architecture is transparent by design:

```yaml
# Every agent has a defined, inspectable role
agent:
  name: customer_support_triage
  role: support-classifier
  purpose: "Classify incoming customer support tickets by urgency and topic.
            Does NOT generate responses to customers. Does NOT make decisions
            about refunds, cancellations, or account changes."
  model: local:llama3.1:8b
  capabilities:
    - ticket_classification
    - urgency_assessment
    - department_routing
  limitations:
    - no_customer_facing_output
    - no_financial_decisions
    - no_account_modifications
  human_oversight:
    required: true
    reviewer_role: support_team_lead
    escalation_path: on_uncertainty | on_disagreement
```

Each agent role is defined in human-readable configuration. The purpose, capabilities, and limitations are documented — not inferred from behavior. This directly supports the EU AI Act's transparency requirements.

### Lens explainability

[Lens](../products/lens/index.md) provides explainability for agent decisions. When an agent makes a classification, recommendation, or generation, Lens can produce structured explanations:

```json
{
  "agent": "customer_support_triage",
  "decision": "classify_ticket",
  "input_summary": "Customer reports login failure after password reset",
  "classification": {
    "topic": "authentication",
    "urgency": "medium",
    "department": "technical_support"
  },
  "reasoning": {
    "key_signals": [
      "password_reset mentioned",
      "login_failure reported",
      "no data_loss_or_security_breach indicators"
    ],
    "confidence": 0.92,
    "alternative_classifications": [
      {"topic": "account_recovery", "confidence": 0.06}
    ]
  },
  "data_sources": [
    "fabric:support_policy_v2",
    "input:customer_message_only"
  ],
  "human_oversight_status": "pending_review"
}
```

This explainability output can be presented to human reviewers, logged for audit, or used as documentation for conformity assessments.

## Human oversight: built into the OS layer

The EU AI Act requires human oversight for high-risk AI systems (Article 14). Oversight must enable humans to:

1. Fully understand the AI system's capabilities and limitations
2. Monitor its operation for anomalies
3. Intervene in or override its outputs
4. Stop the system if necessary

fusionAIzeOS implements human oversight as a first-class architectural concept — not as a checkbox.

```yaml
# OS policy: human oversight configuration
policies:
  human_oversight:
    default_review: required

    # Agent actions that always require human approval
    always_review:
      - type: external_communication  # any output sent to a client or customer
      - type: financial_decision      # any action involving monetary value
      - type: legal_content           # any output that could be construed as legal advice
      - type: system_configuration    # any agent modifying system settings

    # Escalation based on agent confidence
    escalate_on_low_confidence:
      threshold: 0.85
      action: flag_for_human_review

    # Escalation based on disagreement between agents
    escalate_on_agent_disagreement:
      action: escalate_to_designated_human

    # Emergency stop
    emergency_stop:
      trigger: manual  # human operator command
      effect: halt_all_agent_actions
      scope: per_tenant | per_department | per_agent
```

Your human operators retain full control. Agents advise, draft, classify, and research — but the architecture ensures that humans stay in the decision loop wherever the EU AI Act requires it.

## Risk classification and documentation

The EU AI Act classifies AI systems into four risk categories. Here's how fusionAIze supports compliance at each level:

| Risk category | Examples in fusionAIze context | fusionAIze compliance support |
|--------------|-------------------------------|------------------------------|
| **Unacceptable risk** (prohibited) | Social scoring, real-time biometric identification in public spaces | Organization must not deploy. fusionAIze's policy engine can block prohibited use cases. |
| **High risk** (Annex III) | AI in employment decisions, credit scoring, essential services, law enforcement | Role definitions + human oversight policies + Lens explainability + audit trails |
| **Limited risk** (transparency obligations) | Chatbots, customer-facing agents, emotion recognition | Agent identity disclosure, "you are interacting with AI" notices, transparent role descriptions |
| **Minimal risk** (no specific obligations) | Internal productivity, content drafting, code assistance | Voluntary transparency through agent descriptions and explainability |

### Documentation for high-risk systems

Organizations deploying high-risk AI systems under the EU AI Act must maintain technical documentation (Article 11) and perform conformity assessments (Article 43). fusionAIze supports this with:

- **Agent blueprints in Studio** — capture the exact configuration, model, policies, and data sources for each AI system
- **Version-controlled configurations** — every blueprint change is tracked, providing a history of how the system was configured at any point
- **Audit logs via Signal** — structured event logs documenting every agent action, decision, and human intervention
- **Lens explainability reports** — generate documentation explaining how specific decisions were reached

```bash
# Generate a conformity assessment documentation package for an agent
faios compliance export --agent customer_support_triage \
  --format pdf \
  --include configuration,data_flow,risk_assessment,test_results \
  --output ./compliance/customer_support_triage_dossier.pdf
```

## Audit trails via Signal

[Signal](../products/signal/index.md) (currently in development) will provide comprehensive audit trail capabilities that support EU AI Act record-keeping requirements:

- **Complete event logging** — every agent interaction, human review decision, escalation, and override
- **Immutable audit records** — append-only, timestamped, attributable to specific actors (human or agent)
- **Chain of reasoning** — trace any agent output back through the prompt, context sources, model, and configuration that produced it
- **Retention policies** — configurable to meet regulatory requirements in your jurisdiction

!!! info "Signal development status"
    Signal audit trail capabilities are in active development. Current logging is available through Gate and Grid structured log output. See the [roadmap](../about/roadmap.md) for Signal availability timelines.

## Open-source transparency

The EU AI Act encourages transparency in AI systems. As an open-core platform, fusionAIze provides a level of transparency that proprietary AI platforms cannot match:

- **Full source code availability** for Gate, Lens, Fabric, Grid, and OS (Apache 2.0)
- **Public architecture documentation** explaining how data flows through the system
- **Community review** — the code is open to inspection by regulators, auditors, and the public
- **No hidden processing** — every data transformation, every model call, every storage operation is traceable in the source

This transparency directly supports EU AI Act expectations for AI system documentation and accountability.

## Practical steps for EU AI Act readiness with fusionAIze

1. **Classify your AI use cases.** Determine which risk category each of your fusionAIze-powered workflows falls under.
2. **Document agent purposes.** For each agent, define its purpose, capabilities, limitations, and intended use context — use Studio blueprints for version-controlled documentation.
3. **Configure human oversight.** Set OS policies that match the risk level of each agent workflow. High-risk systems need comprehensive oversight; minimal-risk systems may need only basic review.
4. **Enable explainability.** Use Lens to generate structured explanations for agent outputs, especially for high-risk use cases.
5. **Maintain audit records.** Log agent actions, human reviews, and decisions. Retain per your regulatory obligations.
6. **Monitor and update.** Use Signal to track agent performance, detect anomalies, and trigger reviews when behavior changes.

---

**Next steps:**

- [GDPR compliance](../compliance/gdpr.md) — data protection requirements
- [On-premise & sovereignty](../compliance/sovereignty.md) — infrastructure control for regulatory compliance
- [OS documentation](../products/os/index.md) — configure human oversight policies
- [Lens documentation](../products/lens/index.md) — enable explainability for your agents
