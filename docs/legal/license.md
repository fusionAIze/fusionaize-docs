# License

fusionAIze core components are released under the **Apache License, Version 2.0** ("Apache 2.0").

---

## Apache 2.0 summary

The Apache 2.0 license is one of the most widely adopted and enterprise-friendly open-source licenses. It grants broad permissions while providing clear legal protections for both contributors and users.

### What the license allows

| Right | Description |
|-------|-------------|
| **Commercial use** | You may use fusionAIze for any purpose, including commercial and for-profit applications. No royalties, no revenue sharing. |
| **Modification** | You may modify the source code to suit your needs. Create derivatives, add features, fork the project. |
| **Distribution** | You may distribute the original or modified software, including as part of a larger work or commercial product. |
| **Patent use** | The license includes an express grant of patent rights from contributors to users. This means contributors cannot later sue you for patent infringement for using their contributions. |
| **Private use** | You may use fusionAIze privately within your organisation without any obligation to disclose modifications. |
| **Sublicensing** | You may sublicense the software under different terms, provided you comply with the original license's conditions. |

### What the license requires

| Requirement | Description |
|-------------|-------------|
| **License and copyright notice** | You must include a copy of the Apache 2.0 license and all copyright notices in any distribution of the software. |
| **State changes** | If you modify a file, you must state that you changed it (e.g., by adding a notice in the modified file). |
| **Attribution** | You must retain all existing notices — including attribution, patent, trademark, and copyright notices — in any distribution. |
| **NOTICE file** | If the project includes a `NOTICE` file with attribution notices, you must include it in any distribution. |

### What the license does NOT require

- You do **not** need to open-source your modifications (no copyleft).
- You do **not** need to disclose your proprietary code that uses fusionAIze.
- You do **not** need to contribute back (though we welcome it).
- You do **not** need to display a "Powered by fusionAIze" badge (though we appreciate it).

---

## Core vs. extended stack

fusionAIze follows an [open-core model](../about/open-core.md). Licensing differs between the core and extended stacks:

### Core stack — Apache 2.0

| Component | License | Repository |
|-----------|---------|------------|
| Gate (`faigate`) | Apache 2.0 | [git.langevc.com/fusionaize/faigate](https://git.langevc.com/fusionaize/faigate) |
| Lens (`failens`) | Apache 2.0 | [git.langevc.com/fusionaize/failens](https://git.langevc.com/fusionaize/failens) |
| Fabric (`faifabric`) | Apache 2.0 | [git.langevc.com/fusionaize/faifabric](https://git.langevc.com/fusionaize/faifabric) |
| Grid (`faigrid`) | Apache 2.0 | [git.langevc.com/fusionaize/faigrid](https://git.langevc.com/fusionaize/faigrid) |
| faios | Apache 2.0 | [git.langevc.com/fusionaize/faios](https://git.langevc.com/fusionaize/faios) |

### Extended stack — source-available / proprietary

| Component | License | Notes |
|-----------|---------|-------|
| Studio (`faistudio`) | Source-available | Viewable source; commercial use requires a license |
| Signal (`faisignal`) | Proprietary | Included in fusionAIze Enterprise |
| Academy | Proprietary | Course content and certification materials |
| Agency | N/A | Managed service, not distributed software |

!!! info "Open-core rationale"
    The core stack under Apache 2.0 ensures that the foundational capabilities — the gateway, context layer, memory fabric, execution substrate, and team logic — remain free and open forever. The extended stack funds ongoing development through commercial licensing. Read more in the [open-core overview](../about/open-core.md).

---

## Patent grant

!!! note "Section 3 of the Apache 2.0 license"
    The license includes a **perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable patent license** from every contributor to every user.

This means that if a fusionAIze contributor holds a patent on a technique used in the code, they grant every user a license to that patent for the purpose of using, modifying, or distributing the software. This is a critical protection that some other open-source licenses do not provide.

If a user initiates patent litigation against any entity alleging that the software infringes a patent, **their patent license from contributors terminates automatically**. This is a defensive termination clause — it protects the project and its community from patent aggression.

---

## Attribution requirements

### When you must provide attribution

You must include attribution when you:

1. Distribute fusionAIze (compiled or source) to others outside your organisation.
2. Include fusionAIze in a product or service that you distribute to others.
3. Publish a modified version of fusionAIze.

### When you do NOT need attribution

You do not need to provide attribution when you:

1. Use fusionAIze internally within your organisation (private use).
2. Run fusionAIze as a backend service that your users interact with (SaaS).
3. Include fusionAIze in a compiled application distributed to end users (but you must include the license text in your documentation or about page).

### How to provide attribution

Include the following in your distribution:

```text
This product includes software developed by the fusionAIze project
(https://fusionaize.dev) and its contributors, licensed under the
Apache License, Version 2.0.

Copyright (c) 2024—present LangeVC and fusionAIze contributors.

A copy of the Apache 2.0 license is available at:
https://www.apache.org/licenses/LICENSE-2.0
```

If the component repository includes a `NOTICE` file, include it as well.

---

## Third-party dependencies

fusionAIze components depend on third-party open-source libraries, each under its own license. We maintain a bill of materials (SBOM) in each repository under `THIRD_PARTY_NOTICES.md`. Build dependencies and transitive dependencies are documented in the `pyproject.toml` and lock files.

We do not bundle or redistribute third-party code directly. All dependencies are declared and resolved through standard Python package management.

---

## FAQ

!!! question "Can I use fusionAIze in a commercial product?"
    **Yes.** The Apache 2.0 license explicitly permits commercial use. You can integrate fusionAIze core components into your product and sell it without paying royalties or obtaining a separate license.

!!! question "Do I have to open-source my modifications?"
    **No.** Apache 2.0 is a permissive license, not a copyleft license. If you modify fusionAIze for internal use, you do not need to share those modifications. If you distribute your modified version, you must include the license and attribution, but you are not required to release your source code.

!!! question "Can I contribute to fusionAIze and retain copyright?"
    **Yes.** You retain copyright on your contributions. By contributing, you license your contribution under Apache 2.0, which grants fusionAIze and all users the rights described in this document.

!!! question "What if I want to use an extended-stack component in a commercial product?"
    Extended-stack components (Studio, Signal, Academy) are not under Apache 2.0. Contact [license@fusionaize.dev](mailto:license@fusionaize.dev) for commercial licensing.

!!! question "How do I report a license violation?"
    Contact [legal@fusionaize.dev](mailto:legal@fusionaize.dev). Please include specific details about the violation and any supporting evidence.

---

## Full license text

The complete Apache License, Version 2.0 is available at:

- [apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)
- `LICENSE` file in every core repository

[:fontawesome-solid-arrow-right: Open-core model](../about/open-core.md){ .md-button }
[:fontawesome-solid-arrow-right: Privacy policy](privacy.md){ .md-button }
