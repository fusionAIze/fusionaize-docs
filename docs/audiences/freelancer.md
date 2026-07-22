# Freelancers & Solopreneurs

You built your business on expertise and relationships. You didn't build it to spend hours on admin, chasing tool configurations, or juggling five different SaaS dashboards. fusionAIze gives you the infrastructure to run AI as your virtual team — on your terms, on your hardware, with no recurring API bills unless you want them.

## What fusionAIze means for your practice

Most AI tools treat you as a consumer of a service. fusionAIze treats you as the **operator of your own AI infrastructure**. The difference matters:

- **You own the stack.** Everything runs on your machine or your server. No one else holds your data, your prompts, or your client context.
- **You set the budget.** Local models cost zero dollars per token. Cloud providers are available when you need them, optional when you don't.
- **You define the team.** fusionAIzeOS lets you give each AI agent a role, a scope of responsibility, and a set of policies — just like onboarding a real team member.

Think of it as the difference between renting desk space in someone else's office versus owning your own studio. Both work. One gives you control.

## The solo deployment profile

The **Solo** deployment profile is designed for a single operator running on a laptop, workstation, or small dedicated server. It bundles the core components you need without the complexity you don't.

| Component | What it does for you |
|-----------|---------------------|
| **Gate** | Routes AI requests to the right model — local or cloud — with one unified interface |
| **Lens** | Filters and compresses context so your agents stay focused and your costs stay low |
| **Fabric** | Stores shared memory across sessions — client preferences, project context, brand voice |
| **Grid** | Runs agent tasks in isolated sandboxes so you can parallelize work safely |
| **OS** | Manages agent roles, policies, and handoffs — your operating system for AI team members |

Deploying the Solo profile takes one command:

```bash
faios deploy --profile solo
```

That's the installation. Configuration is covered in the [Getting Started guide](../getting-started/index.md).

## Local models: zero recurring cost

One of the biggest anxieties for freelancers adopting AI is the unpredictable monthly API bill. You try a new workflow, experiment with longer context windows, run a batch job overnight — and suddenly your OpenAI invoice is three times what you expected.

fusionAIze supports running models **entirely on your own hardware** through [faios](../products/os/index.md) and [faigate](../products/gate/index.md). Popular local model options include:

- **Llama 3** (Meta) — strong general-purpose reasoning
- **Mistral** — excellent for structured output and document processing
- **Phi-3** (Microsoft) — compact, runs comfortably on consumer laptops
- **Qwen 2.5** — strong multilingual performance, particularly good for European languages

Gate handles model switching transparently. Your agents don't need to know whether they're talking to a local Llama or a cloud GPT — they just work.

```yaml
# Example: mixing local and cloud models in your Gate config
providers:
  local:
    type: ollama
    models:
      - llama3.1:8b      # free, runs locally on your laptop
      - mistral:7b        # free, fast structured output
  cloud:
    type: openai
    models:
      - gpt-4o-mini       # pay-per-token, only when you need it
    throttle:
      monthly_budget: 20  # hard cap in EUR — no surprise bills
```

!!! tip "Start local, go cloud when it matters"
    Most freelancer workflows — drafting, summarization, translation, code review — run well on local 7B-8B parameter models. Reserve cloud models for the tasks where the extra capability genuinely justifies the cost.

## Getting started in 10 minutes

You don't need a DevOps background. The Solo profile comes pre-configured for the most common freelancer workflows.

=== "macOS / Linux"

    ```bash
    # 1. Install
    pip install fusionaize

    # 2. Deploy the solo profile
    faios deploy --profile solo

    # 3. Pull a local model (free, runs on your hardware)
    faios model pull llama3.1:8b

    # 4. Start your first agent
    faios agent create \
      --name "Content Assistant" \
      --role content-writer \
      --model llama3.1:8b
    ```

=== "Windows"

    ```powershell
    # 1. Install
    pip install fusionaize

    # 2. Deploy the solo profile
    faios deploy --profile solo

    # 3. Pull a local model
    faios model pull llama3.1:8b

    # 4. Start your first agent
    faios agent create `
      --name "Content Assistant" `
      --role content-writer `
      --model llama3.1:8b
    ```

After these four steps, you have a running AI agent with access to local memory (Fabric), context management (Lens), and the ability to execute tasks in isolated sandboxes (Grid).

## Realistic use cases

These aren't hypotheticals. They're workflows freelancers run today with fusionAIze.

### Content creation pipeline

Your **Content Writer** agent drafts blog posts, social media copy, and newsletters in your brand voice. Your **Editor** agent reviews for consistency, tone, and factual accuracy. Your **Researcher** agent gathers sources and summarizes competitor content.

All three agents share context through Fabric, so the Editor knows the Content Writer's brief and the Researcher's sources. You review the final output — the agents handle the heavy drafting.

```
You (strategy, final review)
    │
    ├── Content Writer agent (drafting)
    ├── Editor agent (quality review)
    └── Researcher agent (source gathering)
```

### Client communication

An **Inbox Triage** agent sorts incoming client messages by urgency and topic. A **Meeting Prep** agent pulls relevant context from past conversations and project files before each client call. A **Follow-up** agent drafts post-meeting summaries and action items.

You stay present in the human relationship. The agents handle the context-switching burden.

### Project management

Your **Sprint Planner** agent tracks deliverables, flags blockers, and suggests task prioritization. Your **Invoice Assistant** agent reviews completed work against time tracking and generates draft invoices.

!!! example "Real workflow: Client proposal generation"
    A freelance web designer uses fusionAIze to generate tailored proposals:

    1. **Researcher agent** scans the client's website, social media, and competitors (15 seconds)
    2. **Proposal Writer agent** drafts a proposal using the research + the designer's template (30 seconds)
    3. **Pricing agent** calculates estimates based on past project data stored in Fabric (5 seconds)
    4. The designer reviews, personalizes, and sends — total time invested: 10 minutes, down from 2 hours

## Pricing philosophy

fusionAIze is **free at the core**. The Solo deployment profile, the base agent runtime (faios), the model router (faigate), and the memory layer (faifabric) are all Apache 2.0 open source. You can run them indefinitely at zero cost with local models.

Premium features are additive, not restrictive:

| Tier | What's included | Best for |
|------|----------------|----------|
| **Core** (free, Apache 2.0) | Gate, Fabric, Lens, Grid, OS — full stack, local models | Getting started, proving value |
| **Premium** | Advanced Lens compression, Fabric cross-session recall, Studio blueprints, Signal monitoring | Growing practice, client delivery |
| **Academy** | Structured learning paths, certified operator programs, community workshops | Skill development, credibility |

There is no token-based pricing on the platform itself. If you use cloud models through Gate, you pay the model provider directly — and Gate's budget throttling keeps that predictable.

!!! note "No vendor lock-in"
    fusionAIze components are modular. You can use just Gate as your model router, or just Fabric as your memory layer. Each component works standalone. Adopt what you need, when you need it.

## The freelancer advantage

Large companies pay per-seat for AI tools. You pay for value. fusionAIze's architecture — local execution, modular components, open-source core — is built for operators who need leverage, not overhead.

Your expertise is the product. fusionAIze is the infrastructure that gives it scale.

---

**Next steps:**

- [Quickstart guide](../getting-started/index.md) — get running in under 10 minutes
- [Gate documentation](../products/gate/index.md) — understand model routing
- [OS documentation](../products/os/index.md) — design your agent team structure
- [Studio documentation](../products/studio/index.md) — create reusable blueprint workflows
