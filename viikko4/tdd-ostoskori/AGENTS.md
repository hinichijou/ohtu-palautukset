# Agent Instructions

## Project

- This is a small Python TDD exercise for a shopping cart.
- The project requires Python 3.14 or newer; development dependencies are declared in [pyproject.toml](pyproject.toml).
- Source modules are in [src](src), and tests are in [src/tests](src/tests).
- The domain model is split across `Tuote` (product), `Ostos` (cart line item), and `Ostoskori` (shopping cart).

## Development

- This is an uv-managed project. Install and manage all dependencies with `uv`, and run all project commands through `uv` (for example, `uv run ...`); do not use bare `pip`, `python`, or other tool commands.
- Run the test suite with `uv run pytest`.
- Tests use pytest as the runner and `unittest.TestCase` assertions. Add focused regression tests alongside the behavior being changed.
- Preserve the existing Finnish public method and class names unless a task explicitly requires an API change.
- Do not change the code in [src/ostos.py](src/ostos.py) or [src/tuote.py](src/tuote.py).
- Do not edit tests unless the task explicitly asks for test changes.
- Keep changes small and TDD-oriented: update or add a failing test first when implementing missing cart behavior, then make the smallest implementation change that passes it.
- Always implement the absolute minimum code required to make the tests pass.
- Prefer hardcoded values or narrowly scoped behavior when they satisfy the current test; do not solve the general case until a test requires it.
- Do not add runtime dependencies without updating [pyproject.toml](pyproject.toml).

## Style

- Follow the existing simple class-based structure and type annotations where they are already used.
- Avoid unrelated refactors, framework setup, or packaging changes; this project intentionally uses direct module imports from `src`.