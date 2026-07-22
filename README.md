# fusionAIze Documentation

> [!NOTE]
> **Canonical repository: self-hosted Forgejo.** This GitHub copy is a
> read-only mirror kept in sync.

Public documentation for the [fusionAIze](https://fusionaize.com) product stack — sovereign AI infrastructure.

**Site**: [docs.fusionaize.com](https://docs.fusionaize.com)  
**Built with**: [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)  
**Maintained by**: [fusionaize.com](https://github.com/fusionAIze)

## Build

```bash
pip install mkdocs-material
mkdocs build
```

Output in `site/`.

## Deploy

Site is served via Cloudflare Pages. To update:

```bash
mkdocs build
# Deploy site/ to Cloudflare Pages or via rsync to server
```

## Structure

- `docs/` — Markdown source, organized by section:
  - `docs/getting-started/` — Quickstart guides and onboarding
  - `docs/products/` — Product documentation for Gate, Grid, Lens, Fabric, OS, and Signal
  - `docs/architecture/` — Architectural overviews and design principles
  - `docs/about/` — Company, vision, and team
  - `docs/audiences/` — Content tailored for specific user roles
  - `docs/compliance/` — Security, privacy, and compliance documentation
  - `docs/contributing/` — Contribution guides and community resources
  - `docs/legal/` — License, terms, and legal documents
  - `docs/process/` — Workflow conventions and release processes
- `mkdocs.yml` — MkDocs configuration (nav, theme, plugins, Mermaid)
- `docs/assets/` — Logo, brand CSS, static assets

## License

Apache 2.0 — see [LICENSE](https://github.com/fusionAIze/fusionaize-docs/blob/main/LICENSE)

## Development

Canonical repository: **self-hosted Forgejo** — `git.langevc.com/fusionaize/fusionaize-docs`
(`git clone git@git.langevc.com:fusionaize/fusionaize-docs.git`). Develop against the Forgejo
clone and open pull requests there. The GitHub copy is a read-only mirror.
