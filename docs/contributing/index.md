# Contributing

fusionAIze is an open-core project built in the open. We welcome contributions from individuals, teams, and organisations — whether it's a bug fix, a documentation improvement, a new provider integration, or a completely new component.

---

## Code of Conduct

All contributors are expected to follow our **Code of Conduct**. In summary:

- Be respectful and inclusive in all interactions.
- Assume good intent. Disagreements are fine; personal attacks are not.
- Prioritise the health of the community over individual preferences.
- Report unacceptable behaviour to [conduct@fusionaize.dev](mailto:conduct@fusionaize.dev).

The full Code of Conduct lives in the root of every repository: `CODE_OF_CONDUCT.md`.

---

## Where to find issues

We track all work publicly:

| Source | Link |
|--------|------|
| **Primary (Forgejo)** | [git.langevc.com/fusionaize](https://git.langevc.com/fusionaize) |
| **GitHub (Mirror)** | [github.com/fusionAIze](https://github.com/fusionAIze) |

Issues are labelled by component, difficulty, and type:

| Label | Meaning |
|-------|---------|
| `good-first-issue` | Small, self-contained, well-documented — ideal for new contributors |
| `help-wanted` | We need someone to own this; all skill levels welcome |
| `component/gate` | Issues in the Gate AI gateway |
| `component/lens` | Issues in the Lens context layer |
| `component/fabric` | Issues in the Fabric memory system |
| `component/grid` | Issues in the Grid execution substrate |
| `component/faios` | Issues in the faios operating logic |
| `type/bug` | Confirmed bug |
| `type/feature` | Feature request or enhancement |
| `type/docs` | Documentation improvements |
| `priority/critical` | Must be addressed immediately |

!!! tip "New contributor?"
    Start with issues labelled `good-first-issue`. They're small, self-contained, and come with context and guidance in the issue description. We actively maintain and refresh this label.

---

## Development setup

fusionAIze is a multi-repository project. Each component has its own repository with a consistent structure.

### Prerequisites

- Python 3.10+
- Git 2.40+
- Docker 24.0+ (for Grid and integration tests)
- A code editor with Python support

### Setting up a component for development

```bash
# Clone the component you want to work on
git clone https://git.langevc.com/fusionaize/faigate.git
cd faigate

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install in development mode with all dev dependencies
pip install -e ".[dev,test,docs]"

# Install pre-commit hooks
pre-commit install

# Run the test suite to confirm everything works
pytest
```

### Project structure

Every component repository follows this layout:

```
faigate/                        # Example: Gate repository
├── pyproject.toml              # Build config, dependencies, tool settings
├── src/
│   └── faigate/                # Source code
│       ├── __init__.py
│       ├── server.py           # HTTP server entry point
│       ├── providers/          # Provider implementations
│       ├── routing/            # Request routing logic
│       ├── models/             # Pydantic models and schemas
│       └── cli.py              # Command-line interface
├── tests/                      # Test suite
│   ├── unit/
│   ├── integration/
│   └── conftest.py             # Shared fixtures
├── docker/                     # Dockerfiles and Compose configs
├── docs/                       # Component-specific documentation
├── CONTRIBUTING.md             # Component-specific contributing notes
├── CODE_OF_CONDUCT.md
└── LICENSE
```

### Running a component locally

```bash
# Gate
faigate serve                    # Starts on http://localhost:8120

# Lens (requires Gate)
failens serve                    # Starts on http://localhost:8121

# Fabric
faifabric serve                  # Starts on http://localhost:8122

# All components support hot reload in development mode
faigate serve --reload
```

### Full stack for integration testing

```bash
git clone https://git.langevc.com/fusionaize/full-stack.git
cd full-stack
docker compose -f docker-compose.dev.yaml up -d
```

---

## Pull request process

1. **Find or create an issue.** All PRs should reference an existing issue. If one doesn't exist, create it first. This gives us a chance to discuss the approach before you invest time in code.

2. **Fork the repository.** Work on a feature branch: `git checkout -b feature/my-feature`.

3. **Write code and tests.** Follow the conventions below. All PRs must include tests for new functionality.

4. **Run the full test suite locally.**

    ```bash
    pytest
    ruff check .
    mypy src/
    ```

5. **Update documentation.** If your change affects user-facing behaviour, update the relevant docs in the PR.

6. **Open the PR.** Include:
    - Reference to the issue: `Closes #123`
    - A clear description of what changed and why
    - Screenshots or logs for UI or behavioural changes
    - Any breaking changes called out explicitly

7. **Code review.** At least one maintainer must approve. Reviewers will check for correctness, style, test coverage, and documentation.

8. **Merge.** Once approved and CI passes, a maintainer will merge.

### PR checklist

Before opening a pull request, confirm:

- [ ] Tests pass locally (`pytest`)
- [ ] Linting passes (`ruff check .`)
- [ ] Type checking passes (`mypy src/`)
- [ ] New functionality has tests
- [ ] Documentation is updated (if applicable)
- [ ] Commit messages follow the convention
- [ ] PR references the relevant issue

---

## Commit conventions

We use **[Conventional Commits](https://www.conventionalcommits.org/)** for all repositories.

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Usage |
|------|-------|
| `feat` | A new feature |
| `fix` | A bug fix |
| `docs` | Documentation changes only |
| `style` | Formatting, missing semicolons, etc. — no code change |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `perf` | Performance improvement |
| `test` | Adding or correcting tests |
| `chore` | Build process, tooling, CI changes |
| `ci` | CI/CD configuration changes |

### Scopes

Use the component name: `gate`, `lens`, `fabric`, `grid`, `faios`, `sdk`, `cli`, `studio`, `signal`, `docs`.

### Examples

```
feat(gate): add Google Gemini provider support
fix(lens): handle empty context gracefully in extractive compression
docs(fabric): document ChromaDB installation for Apple Silicon
refactor(grid): extract runner lifecycle into RunnerManager class
test(gate): add integration tests for priority-failover routing
chore(deps): bump httpx to 0.27.0
```

---

## Testing requirements

### Test framework

We use **pytest** with the following plugins:

```bash
pip install pytest pytest-asyncio pytest-cov pytest-mock
```

### Test structure

```
tests/
├── unit/                  # Isolated unit tests — no external dependencies
│   ├── test_providers.py
│   ├── test_routing.py
│   └── test_config.py
├── integration/           # Tests with real or containerised dependencies
│   ├── test_gate_api.py
│   ├── test_fabric_store.py
│   └── test_grid_runner.py
└── conftest.py            # Shared fixtures and helpers
```

### Writing tests

- **Every new feature must have tests.** PRs without tests will not be merged.
- **Test behaviour, not implementation.** Tests should validate observable outcomes, not internal state.
- **Use fixtures for shared setup.** Avoid duplicating test infrastructure.
- **Mock external services.** Use `pytest-mock` or `responses` for HTTP mocks. Unit tests must not require network access.

```python
# Example: testing a Gate provider
import pytest
from faigate.providers import AnthropicProvider

@pytest.fixture
def anthropic_provider():
    return AnthropicProvider(
        id="test-anthropic",
        api_key="test-key",
        default_model="claude-sonnet-4-20250514",
    )

@pytest.mark.asyncio
async def test_provider_health_check(anthropic_provider):
    result = await anthropic_provider.health_check()
    assert result["status"] == "ok"
    assert result["provider"] == "anthropic"

@pytest.mark.asyncio
async def test_provider_handles_invalid_api_key(anthropic_provider, mocker):
    mocker.patch.object(anthropic_provider._client, "models", side_effect=AuthError())
    with pytest.raises(ProviderAuthError):
        await anthropic_provider.validate_connection()
```

### Running tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src/faigate --cov-report=term-missing

# Run only unit tests
pytest tests/unit/

# Run a specific test file
pytest tests/unit/test_routing.py

# Run with verbose output
pytest -v
```

### CI

All PRs run the following checks automatically:

1. `pytest` — full test suite
2. `ruff check` — linting
3. `mypy src/` — type checking
4. `ruff format --check` — formatting
5. Integration tests (for PRs touching Gate, Lens, Fabric, or Grid)

---

## Development guidelines

### Code style

- We follow **PEP 8** enforced by **ruff**.
- **Type hints are mandatory** for all public functions and methods.
- Use **Pydantic** for data models and configuration schemas.
- Prefer **async/await** for I/O-bound operations.
- Keep functions small and single-purpose.

### Documentation

- All public APIs must have docstrings (Google style).
- User-facing documentation lives in the `fusionaize-docs` repository.
- Component-specific `README.md` should cover setup, usage, and API surface.

### Dependencies

- Minimise new dependencies. Every added dependency must be justified in the PR.
- Pin dependencies with minimum and maximum version constraints in `pyproject.toml`.
- Use optional dependency groups (`[dev]`, `[test]`, `[anthropic]`, `[openai]`) to keep the core install lean.

### Breaking changes

- Breaking changes must be documented in the PR and the release notes.
- Deprecate before removing: mark as deprecated, keep working for one release, then remove.
- Update the migration guide in the docs.

---

## Contributor license agreement

By contributing to fusionAIze, you agree that your contributions will be licensed under the same license as the project (Apache 2.0 for core components). We do not require a separate CLA — the Apache 2.0 license provides sufficient legal clarity through its inbound=outbound contribution model.

---

## Recognition

All contributors are recognised in:

- The **CONTRIBUTORS.md** file in each repository
- Release notes for contributions that ship in a release
- The fusionAIze community page (opt-in)

---

## Questions?

- **Development discussion:** Open a discussion on [GitHub Discussions](https://github.com/fusionAIze/discussions) or our Forgejo instance.
- **Real-time chat:** Join our community Discord (link in repository READMEs).
- **Security issues:** Do not open public issues. See our [Security Policy](../compliance/security.md).

[:fontawesome-solid-rocket: Get started with the quickstart](index.md){ .md-button }
