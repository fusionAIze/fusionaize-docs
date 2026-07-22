# Privacy Policy

fusionAIze is built on the principle that **AI infrastructure should not require data surrender**. This privacy policy explains what data fusionAIze collects, how it is used, and — critically — what we do not collect.

---

## Our philosophy

> **Your data stays yours. Your models stay under your control. Your fusion team operates within your boundaries.**

fusionAIze is designed for on-premise and self-hosted deployment. The entire stack — Gate, Lens, Fabric, Grid, faios — runs inside your infrastructure. We do not have access to your data, your prompts, your model interactions, or your team's internal communications unless you explicitly choose to share them.

This is not a marketing claim. It is a structural property of the architecture, and it is the foundation of every design decision we make.

---

## What we do NOT collect

When you deploy fusionAIze in a **self-hosted** environment:

| Data category | Status | Details |
|---------------|--------|---------|
| Prompts and completions | **Not collected** | All AI interactions remain within your infrastructure. Gate routes data directly to your configured providers. |
| Conversation history | **Not collected** | Fabric stores memory locally within your deployment. We have no access. |
| Source code | **Not collected** | Code reviews, repository access, and build data are processed within your Grid runners. |
| User identities | **Not collected** | Your team members' identities, roles, and permissions are managed by your identity provider. |
| Model fine-tuning data | **Not collected** | Any fine-tuning or training data you provide to models is processed by your model provider, not by us. |
| Payment information | **Not collected** | We do not process payments for self-hosted deployments. Your provider API keys are your own. |
| Behavioural telemetry | **Not collected** | Self-hosted fusionAIze does not phone home. There is no embedded telemetry, no usage tracking, no analytics beacon. |

### No telemetry in self-hosted deployments

!!! important "Zero telemetry by design"
    Self-hosted fusionAIze components send **no telemetry, no usage statistics, no crash reports, and no analytics data** to fusionAIze or any third party. There is no opt-out because there is nothing to opt out of — telemetry is not compiled into the open-source releases.

We believe that AI infrastructure operating inside your organisation should be as private as your file system. Telemetry would violate that trust.

---

## What we DO collect (and when)

fusionAIze collects data only in the following limited contexts:

### 1. Website and documentation analytics

When you visit `fusionaize.dev` or `docs.fusionaize.dev`:

| Data | Purpose | Retention |
|------|---------|-----------|
| Anonymised page views | Understanding which documentation pages are most used, so we can improve them | 26 months |
| Anonymised referrer | Understanding how people discover fusionAIze | 26 months |

We use **Plausible Analytics** — a privacy-first, cookie-less, GDPR-compliant analytics service. No personal data is collected. No cookies are set. No tracking across sessions or sites.

### 2. GitHub / Forgejo interactions

When you star, fork, open issues, or submit pull requests on our public repositories, those interactions are visible on those platforms and governed by their respective privacy policies:

- [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
- Forgejo (self-hosted at `git.langevc.com`) — governed by our own deployment; no data shared with third parties.

### 3. Mailing list and community

When you subscribe to the fusionAIze mailing list or join the community Discord:

| Channel | Data collected | Purpose |
|---------|---------------|---------|
| Mailing list | Email address | Sending project updates, release announcements |
| Discord | Discord username, messages | Community discussion |
| Contact form | Name, email, message content | Responding to inquiries |

You can unsubscribe from the mailing list at any time. Discord data is governed by [Discord's privacy policy](https://discord.com/privacy).

### 4. Commercial interactions

When you purchase a fusionAIze Enterprise license, Academy subscription, or Agency services:

| Data | Purpose | Legal basis | Retention |
|------|---------|-------------|-----------|
| Company name, billing address | Invoicing and contract management | Contractual necessity | Duration of contract + 7 years (legal requirement) |
| Contact name and email | Account management and support | Contractual necessity | Duration of contract + 7 years |
| Payment details | Payment processing | Contractual necessity | Processed by payment provider (Stripe); we do not store full card details |

Commercial data is never used for any purpose other than fulfilling the contractual relationship.

---

## Your model providers

!!! warning "Provider data practices"
    When you send prompts through Gate to a model provider (Anthropic, OpenAI, Google, etc.), **that provider's privacy policy applies to the data you send them.** fusionAIze does not control how third-party providers handle your prompts and completions.

We recommend reviewing the data usage policies of each provider you configure:

- [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
- [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy)
- [Google AI Privacy Notice](https://ai.google.dev/gemini-api/terms)

Gate's provider configuration supports setting provider-specific data usage flags (e.g., opting out of training data usage) where the provider API supports it.

---

## Data we can see (if you self-host)

When you self-host fusionAIze, we see:

Nothing. Zero. Your entire stack runs inside your infrastructure.

When you open an issue or submit a pull request, we see the content you choose to share in that issue or PR. When you ask a question on Discord, we see your message. That's it.

---

## GDPR and data sovereignty

fusionAIze is designed for **data sovereignty by default**:

- **Self-hosted:** All data remains within your infrastructure, in the jurisdiction of your choosing.
- **On-premise:** Grid executes within your network boundaries. No data egress.
- **Provider routing:** Gate routes requests according to your configuration. You control which providers receive which data.
- **No cross-border transfers (from us):** Since we don't have your data, there's nothing to transfer.

For commercial services (licensing, support), data is processed in the EU (Germany) and is subject to GDPR protections.

---

## Your rights

Under applicable data protection laws (including GDPR), you have rights regarding personal data we hold about you. Since the scope of data we collect is intentionally minimal, exercising these rights is straightforward:

| Right | How to exercise |
|-------|----------------|
| **Access** | Request a copy of your data: [privacy@fusionaize.dev](mailto:privacy@fusionaize.dev) |
| **Rectification** | Inform us of inaccuracies and we will correct them promptly. |
| **Erasure** | Request deletion of your data. Mailing list: unsubscribe link in every email. Other data: email us. |
| **Portability** | We'll provide your data in a structured, machine-readable format. |
| **Objection** | Object to processing at any time. We'll comply unless there are overriding legitimate grounds. |
| **Complaint** | You have the right to lodge a complaint with your local data protection authority. |

We respond to all privacy requests within 30 days.

---

## Security

We apply the same security principles to the data we do hold:

- **Minimal collection:** We collect only what we need, for as long as we need it.
- **Access control:** Internal access to commercial data is restricted to personnel who need it to provide the service.
- **Encryption:** Data is encrypted in transit (TLS 1.3) and at rest.
- **No third-party sharing:** We do not sell, rent, or share your data with third parties for their own purposes.

For the security posture of the fusionAIze platform itself, see the [Security documentation](../compliance/security.md).

---

## Changes to this policy

We will notify you of material changes to this privacy policy via:

- The fusionAIze mailing list
- A banner on `fusionaize.dev`
- A notice in the release changelog

The revision history of this document is tracked in the `fusionaize-docs` repository.

---

## Contact

For privacy questions, data requests, or to exercise your rights:

- **Email:** [privacy@fusionaize.dev](mailto:privacy@fusionaize.dev)
- **Postal:** LangeVC GmbH, Attn: Data Protection, Germany (full address available on request)

For security vulnerabilities, do not use the privacy contact. See the [Security Policy](../compliance/security.md).

[:fontawesome-solid-arrow-right: License](license.md){ .md-button }
[:fontawesome-solid-arrow-right: Security](../compliance/security.md){ .md-button }
