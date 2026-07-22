# Security

fusionAIze takes security seriously. This document describes our security practices, how we protect the codebase, and how to report security issues.

## Security architecture

fusionAIze's security posture rests on three principles:

1. **Local-first design.** The platform runs on your infrastructure. Attack surface is limited to what you deploy — there's no fusionAIze-controlled cloud service to compromise.
2. **Least privilege by default.** Agents run with explicitly defined scopes. The OS layer enforces boundaries between agents, tenants, and data partitions.
3. **Defense in depth.** Security controls operate at multiple layers — from pre-commit hooks through CI gates to runtime policies.

## Code security

### Static analysis (CodeQL)

Every push and pull request is analyzed by GitHub's CodeQL engine. CodeQL builds a database of the codebase and runs security queries that detect:

- Injection vulnerabilities (SQL, command, code)
- Insecure cryptographic practices
- Information exposure through logging or error messages
- Authentication and authorization bypass patterns
- Unsafe deserialization

CodeQL runs on all supported languages in the repository and blocks merging when high-severity findings are detected.

### Secret detection (gitleaks)

[gitleaks](https://github.com/gitleaks/gitleaks) scans every commit for secrets — API keys, tokens, credentials, private keys — before they reach the repository:

```yaml
# Pre-commit hook: gitleaks
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
```

The CI pipeline also runs gitleaks on every push. A secret that makes it past pre-commit hooks is caught before merge.

### Additional pre-commit guards

| Hook | What it prevents |
|------|-----------------|
| `detect-private-key` | Blocks commits containing RSA, DSA, EC, or ED25519 private keys |
| `check-merge-conflict` | Prevents unresolved merge conflict markers from being committed |
| `check-yaml` | Validates YAML syntax — catches duplicate keys that could silently override security settings |

## Dependency management

### Dependabot

[Dependabot](https://docs.github.com/en/code-security/dependabot) automatically monitors all dependencies for known vulnerabilities:

- **Daily vulnerability scans** against the GitHub Advisory Database, NVD (National Vulnerability Database), and OSV (Open Source Vulnerabilities)
- **Automated pull requests** with version bumps when a patch is available
- **Grouped updates** to reduce PR noise while maintaining freshness
- **Configurable alerting** — repository maintainers are notified of critical vulnerabilities immediately

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
    open-pull-requests-limit: 10
    labels:
      - "dependencies"
      - "security"

  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

### Supply chain security

- **Pinned dependency versions** in `requirements.txt` — no floating version ranges in production
- **Hash verification** where supported by the package ecosystem
- **Docker images** built from minimal base images with known provenance
- **SBOM generation** planned for future releases (Software Bill of Materials)

## CI/CD security gates

The CI pipeline enforces security at multiple stages. For a detailed explanation of the CI gate architecture, see [CI Safeguards](../process/ci-safeguards.md).

```
Developer Push
     │
     ▼
Pre-commit hooks (local)
├── gitleaks (secret detection)
├── detect-private-key
├── check-merge-conflict
├── ruff (linting)
├── bandit (Python security analysis)
└── ruff-format (style)
     │
     ▼
CI Pipeline (GitHub Actions)
├── CodeQL analysis
├── Test suite
├── Lint (ruff, mypy)
├── Security scan (bandit, gitleaks)
└── Package / build verification
     │
     ▼
CI Gate
├── All checks passed → merge allowed
└── Any check failed → merge blocked
```

!!! note "The gate cannot be bypassed"
    Branch protection rules enforce that the CI Gate check must pass before merging to `main`. Administrator bypass is disabled. The only way to merge is for all security, test, and lint checks to pass. This is intentional and permanent.

## Runtime security

### Agent isolation

Each agent runs in an isolated execution context through [Grid](../products/grid/index.md):

- **Filesystem isolation** — agents cannot access files outside their designated workspace
- **Network segmentation** — agents access only the network endpoints explicitly granted in their configuration
- **Resource limits** — CPU, memory, and execution time quotas prevent denial-of-service from runaway agents
- **Model access control** — Gate enforces which models each agent may use, blocking access to unauthorized providers

### Data isolation

[Fabric](../products/fabric/index.md) memory partitions enforce data separation:

- Agents in tenant A cannot access memories stored for tenant B
- Agents in department X cannot access documents stored for department Y
- Granular permissions control which agents can read, write, or delete specific memory partitions

### Authentication and authorization

Current authentication mechanisms:

- **API key authentication** — scoped tokens for programmatic access
- **Role-based access control** — OS-level role definitions controlling what each agent can do
- **Action authorization** — sensitive actions (external communication, financial operations, configuration changes) require explicit authorization per agent policy

Planned authentication enhancements (see [enterprise roadmap](../audiences/enterprise.md)):

- SAML/OIDC SSO integration
- Multi-factor authentication
- Fine-grained RBAC with per-resource permissions
- Just-in-time privilege escalation

### Transport security

All communication between fusionAIze components uses **TLS 1.3**:

- Gate-to-model connections (when using remote providers)
- Inter-component communication (Gate ↔ Lens, Lens ↔ Fabric, Grid ↔ OS)
- Client-to-platform connections (API, dashboard)
- Signal metric and log collection

Self-signed certificates are supported for internal deployments. Certificate management is configurable — integrate with your existing PKI or use auto-generated certificates.

## Responsible disclosure

We welcome security research and vulnerability reports. We commit to:

- **Acknowledging** your report within 48 hours
- **Investigating** and providing an initial assessment within 5 business days
- **Fixing** confirmed vulnerabilities as quickly as possible, targeting:
    - Critical: 72 hours
    - High: 7 days
    - Medium: 30 days
    - Low: Next release cycle
- **Crediting** you in the release notes and security advisory (unless you prefer to remain anonymous)
- **Not pursuing legal action** against researchers who follow responsible disclosure practices

### How to report a vulnerability

**Do not report security vulnerabilities through public GitHub issues.**

Instead, send a report to:

- **Email:** [security@fusionaize.com](mailto:security@fusionaize.com)
- **PGP key:** Available at [https://fusionaize.com/security.asc](https://fusionaize.com/security.asc)
- **Fingerprint:** `XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX` (to be published)

Please include:

1. A description of the vulnerability and its potential impact
2. Steps to reproduce, including environment details
3. Any proof-of-concept code or screenshots
4. Your preferred contact method for follow-up

### What to expect

1. **48 hours:** Acknowledgment of receipt
2. **5 business days:** Initial assessment and confirmation
3. **Fix timeline:** Based on severity (see above)
4. **Public disclosure:** Coordinated with you; we'll agree on a disclosure date

!!! info "Safe Harbor"
    fusionAIze considers security research conducted in good faith under responsible disclosure principles to be authorized access under applicable anti-hacking laws. We will not pursue legal action against researchers who:
    
    - Report vulnerabilities to us before public disclosure
    - Avoid accessing, modifying, or deleting data that does not belong to them
    - Avoid degrading the service for other users
    - Comply with applicable laws

## Security contact

- **Security issues:** [security@fusionaize.com](mailto:security@fusionaize.com)
- **General inquiries:** [contact@fusionaize.com](mailto:contact@fusionaize.com)
- **Enterprise security review requests:** [enterprise@fusionaize.com](mailto:enterprise@fusionaize.com)

Security documentation and advisories are published at:

- [https://docs.fusionaize.com/compliance/security/](https://docs.fusionaize.com/compliance/security/)
- [https://github.com/fusionAIze/faigate/security](https://github.com/fusionAIze/faigate/security)

---

**Next steps:**

- [CI Safeguards](../process/ci-safeguards.md) — detailed CI security gate documentation
- [Security model](../architecture/security.md) — architectural security design
- [GDPR compliance](../compliance/gdpr.md) — data protection practices
- [SECURITY.md](https://github.com/fusionAIze/faigate/blob/main/SECURITY.md) — security policy in the main repository
