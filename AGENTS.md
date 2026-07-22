# AGENTS.md — fusionAIze Docs

## Project identity

This repository hosts the **public-facing fusionAIze documentation site** — deployed at
[docs.fusionaize.com](https://docs.fusionaize.com). It covers the complete fusionaize product stack
and ecosystem: Gate, Grid, Lens, Fabric, OS, and Signal.

The site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Repository structure

- `docs/` — All Markdown source pages, organized by section:
  - `docs/getting-started/` — Quickstart guides and onboarding
  - `docs/products/` — Per-product documentation
  - `docs/architecture/` — Architectural overviews
  - `docs/about/` — Company, vision, team
  - `docs/audiences/` — Role-specific content
  - `docs/compliance/` — Security and compliance
  - `docs/contributing/` — Contribution guides
  - `docs/legal/` — Licenses and terms
  - `docs/process/` — Workflow and release conventions
- `mkdocs.yml` — Site navigation, theme, plugins, and Mermaid configuration
- `docs/assets/` — Logo, brand CSS, and static assets

## Editing docs

When making changes to the documentation:

1. **Read existing pages first** — understand the current structure before editing.
2. **Follow the brand voice** — professional, clear, and concise. Match the tone of surrounding pages.
3. **Use MkDocs features** where helpful:
   - Admonitions (`!!! note`, `!!! warning`, `!!! info`) for callouts
   - Mermaid diagrams for architecture and flow visualizations
   - Code blocks with language annotations
   - Tabbed content for platform-specific instructions
4. **Keep the nav in sync** — if you add or remove pages, update `mkdocs.yml`.
5. **Test locally** — run `mkdocs serve` or `mkdocs build` to verify changes render correctly.

## Product priority

This is a **documentation site**, not a product or application.

Do not introduce application code, tests, or runtime logic. The repository contains:
- Markdown content in `docs/`
- MkDocs configuration
- Static assets (CSS, images)
- CI for build and deploy

## SkillWeave helper integration

This repository is part of the fusionaize-planning workspace. When operating within the
SkillWeave planning context, refer to:

- `fusionaize-planning` — overall product strategy, roadmap, and planning artifacts
- `fusionaize-docs` (this repo) — public-facing documentation that reflects planning decisions

When a planning decision changes the product surface, update these docs to match.

## Where to work — Forgejo-first

- **Canonical origin:** `git.langevc.com/fusionaize/fusionaize-docs` (Forgejo). **Do not push to GitHub** — it is a read-only mirror.
- **Local clone:** `~/Documents/repositories/forgejo/fusionaize/fusionaize-docs`.
- **Remotes:** `origin` = Forgejo (canonical), `github` = GitHub mirror (read-only).
- **Pull requests:** open on Forgejo (`git.langevc.com/fusionaize/fusionaize-docs/pulls`).
