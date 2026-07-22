# Small & Medium Enterprises

Your team is small, your ambitions aren't. You compete against larger competitors by being faster, more personal, and more efficient. fusionAIze gives your team AI leverage without the enterprise price tag — augmenting your people instead of replacing them.

## The SMB AI challenge

Small and medium businesses face a structural disadvantage in AI adoption:

- **Enterprise tools** are priced for companies with procurement departments, not owner-operators.
- **Consumer AI tools** aren't built for team workflows, data privacy, or process integration.
- **Hiring AI specialists** is expensive and competitive — if you can find them at all.

fusionAIze is built for the gap in between: powerful enough to run real business processes, accessible enough that your existing team can operate it.

## How fusionAIze augments your team

fusionAIze doesn't try to replace your people. It gives them leverage.

| Your team member | With fusionAIze |
|-----------------|-----------------|
| Customer support rep | Handles complex cases while an AI triage agent sorts routine inquiries, drafts response templates, and surfaces relevant account history |
| Operations manager | Reviews AI-generated process optimization suggestions instead of digging through spreadsheets |
| Junior developer | Gets code review and documentation suggestions from an AI pair-programming agent |
| Marketing lead | Briefs a content draft agent that produces first drafts in the brand voice, freeing time for strategy |
| HR coordinator | Onboards new hires with an AI assistant that answers policy questions and guides paperwork completion |

The goal is **augmentation, not automation**. Your people stay in control. The AI handles the repetitive, the routine, and the research-intensive — freeing human attention for judgment, creativity, and relationships.

## The SMB deployment profile

The **SMB** deployment profile is designed for teams of 5 to 250 people. It runs on a single server or small cluster — on-premise or in a private cloud.

```bash
faios deploy --profile smb
```

| Component | SMB configuration |
|-----------|------------------|
| **Gate** | Multi-user model routing with role-based access control |
| **Lens** | Team-shared context compression settings — optimize for your common document types |
| **Fabric** | Persistent team memory — project context, client history, internal knowledge base |
| **Grid** | Isolated execution sandboxes — multiple team members can run agents concurrently |
| **OS** | Role definitions per department, approval workflows for sensitive actions |

### Hardware requirements

For a team of 20-50 people using a mix of local and cloud models:

| Resource | Minimum | Recommended |
|----------|---------|-------------|
| CPU | 8 cores | 16+ cores |
| RAM | 32 GB | 64 GB |
| Storage | 100 GB SSD | 500 GB NVMe |
| GPU (for local models) | Optional | 1× RTX 4060 or better |

The GPU is optional. fusionAIze runs well on CPU-only servers when using cloud models or small local models. Add a GPU when you want to run larger local models with lower latency.

## On-premise deployment for sensitive industries

Some industries can't send data to third-party AI services. Period. Legal practices, medical clinics, accounting firms, and financial advisors operate under professional obligations that cloud AI tools often can't satisfy.

fusionAIze's **full on-premise deployment** addresses this directly:

!!! info "On-premise means on-premise"
    - All model inference runs on your hardware
    - All data — prompts, responses, documents, memory — stays on your servers
    - No outbound API calls to AI providers (unless you explicitly configure them)
    - No telemetry, no usage tracking, no data sharing

```bash
# Air-gapped deployment: no internet required after install
faios deploy --profile smb --mode on-premise --air-gapped
```

For medical practices bound by HIPAA (or GDPR for EU medical data), legal firms bound by attorney-client privilege, and financial services bound by SEC/FCA/BaFin regulations, on-premise deployment is not a luxury — it's a compliance requirement.

!!! example "Medical practice use case"
    A 12-physician practice uses fusionAIze running on a local server to:

    - Draft patient summary letters (Lens compresses medical records into focused context)
    - Triage insurance inquiry emails (classification agent routes to correct department)
    - Generate appointment follow-up instructions (patient-facing, reviewed by physician)
    - Surface relevant treatment guidelines during case review (Fabric stores medical reference)

    All data remains on the practice's server. No patient information touches an external AI provider.

## Change management: bringing your team along

Technology adoption fails more often from people issues than technical ones. Here's a practical approach to introducing fusionAIze in your organization.

### Phase 1: Demonstrate (Week 1-2)

Pick one person in one department. Give them a single agent for a well-defined, repetitive task. Let them use it for a week.

!!! success "Good first agent"
    An **internal FAQ agent** connected to your company handbook and policies. Employees ask it questions instead of interrupting HR or their manager. Low risk, high visibility, immediate time savings.

### Phase 2: Expand (Week 3-6)

Add agents to the departments where Phase 1 showed results. Start with augmentation roles (assist, draft, research) — not autonomous decision-makers. People need to build trust before they accept AI output without review.

### Phase 3: Embed (Month 2-3)

Integrate agents into existing workflows. Notifications from agents appear in Slack or Teams. Agent outputs feed into your existing tools (CRM, project management, document systems). The agents become part of the workflow, not a separate thing to check.

### Phase 4: Optimize (Month 4+)

Review usage data from [Signal](../products/signal/index.md). Which agents are actually being used? Which prompts are people repeating? Where are agents producing low-quality output? Tune the configuration based on real adoption data.

!!! tip "The 80/20 rule for team adoption"
    Expect 20% of your team to embrace AI agents immediately, 60% to adopt gradually once they see peers succeeding, and 20% to resist until the workflow makes it impractical not to. Don't spend your energy on the last 20% in Phase 1 — let the early adopters demonstrate the value.

## Use cases by department

### Customer support

- **Triage agent** classifies incoming tickets by urgency, topic, and required expertise
- **Draft agent** generates response templates that support staff personalize and send
- **Knowledge agent** surfaces relevant help articles, past tickets, and product specs

### Data analysis

- **Report generator** drafts weekly performance summaries from raw metrics
- **Anomaly detector** flags unusual patterns in sales, support volume, or operations data
- **Query assistant** translates natural-language questions into database queries (read-only, reviewed by analyst)

### Process automation

- **Invoice processor** extracts data from PDF invoices and populates accounting entries
- **Contract reviewer** flags non-standard clauses against your template library
- **Inventory monitor** generates reorder suggestions based on historical consumption patterns

### HR onboarding

- **Welcome agent** guides new hires through first-week setup, answers policy questions, and schedules introduction meetings
- **Document agent** ensures all required forms are completed and filed correctly
- **Training agent** recommends learning materials based on role and experience level

## ROI framing

The ROI of fusionAIze for an SMB comes from three sources:

### 1. Time recovery

The most immediate return. Track hours recovered per employee per week.

| Department | Example task | Weekly hours recovered (per person) |
|-----------|-------------|-------------------------------------|
| Support | Ticket triage and draft responses | 5-8 |
| Marketing | Content first drafts | 4-6 |
| Operations | Report generation | 3-5 |
| HR | Onboarding paperwork | 2-4 |

A 20-person company recovering an average of 4 hours per person per week gains **80 hours of productive capacity — the equivalent of two full-time hires — without adding headcount.**

### 2. Quality improvement

Harder to quantify but often more valuable:

- **Faster response times** in customer support (minutes instead of hours for first response)
- **Fewer errors** in repetitive tasks (data entry, calculations, document review)
- **Consistent brand voice** in client communications (agents follow your style guide, every time)
- **Better documentation** (agents generate it as a byproduct of work, not as a separate task)

### 3. Scalability without linear cost

This is the strategic ROI. Traditional scaling means hiring. AI-augmented scaling means:

- Handle 30% more support tickets without adding headcount
- Onboard clients faster (agent handles document collection and initial setup)
- Expand to new markets with fewer new hires (translation agents, localization assistants)

!!! note "Infrastructure cost comparison"
    | Approach | Annual cost (20-person team) |
    |----------|----------------------------|
    | Per-seat SaaS AI tools | €6,000 – €24,000 |
    | Cloud API bills (GPT-4 level) | €12,000 – €48,000 |
    | **fusionAIze SMB on-premise** | **€0 – €3,000** (hardware only, if needed) |

    fusionAIze core is free. Your primary cost is the hardware you choose to run it on — and you may already have sufficient capacity.

---

**Next steps:**

- [SMB deployment guide](../architecture/deployment.md) — hardware sizing and configuration
- [Getting started](../getting-started/index.md) — install and run your first agent
- [OS documentation](../products/os/index.md) — design your team's agent roles
- [Compliance overview](../compliance/gdpr.md) — GDPR and on-premise data handling
