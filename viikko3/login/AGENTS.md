# Login project guidance

## Project shape

- The application is a Flask app. Routes and request handling live in [src/app.py](src/app.py), and the development entry point is [src/index.py](src/index.py).
- Business rules belong in [src/services/user_service.py](src/services/user_service.py); user storage is the in-memory singleton in [src/repositories/user_repository.py](src/repositories/user_repository.py).
- Templates are under [src/templates](src/templates). Preserve form field ids, button text, route paths, and user-facing error messages because the Browser tests assert them.
- The repository intentionally stores users only in memory. Do not assume data survives a process restart or add persistence without an explicit requirement.

## Environment and commands

- This is an `uv` project. Use Python 3.14 or newer as required by [pyproject.toml](pyproject.toml), through the repository's `uv` environment.
- Install the declared dependencies with `uv sync`. Add runtime libraries with `uv add <package>` and development/test libraries with `uv add --dev <package>`; do not install project dependencies directly with `pip`.
- First start the app from the repository root with `uv run python src/index.py` and leave it running; it serves on `http://localhost:5001`.
- After the app is running, open another terminal at the repository root and run the acceptance suite with `uv run robot src/tests`.
- The Browser tests use Chromium and the `robotframework-browser` packages. If the local Browser installation is incomplete, initialize its browser dependencies before running the suite.
- The test setup calls `POST /tests/reset` to clear the in-memory repository. Keep that endpoint available for acceptance-test isolation.

## Implementation conventions

- Keep imports and execution compatible with the current `src` layout. Running `src/index.py` makes the application modules importable as top-level modules.
- Keep username and password validation in `UserService.validate(...)`: registration requires a username of at least 3 characters, and a password of at least 8 characters.
- Keep login validation and authentication in `UserService.check_credentials(...)`: reject missing username or password, then compare the submitted credentials with the user stored in `UserRepository`.
- Keep user storage and duplicate-username checks in `UserRepository`; route handlers should translate service failures into flashed messages and redirects.
- Prefer focused changes and preserve the existing public routes and template structure. Update the relevant Robot test under [src/tests](src/tests) when behavior intentionally changes.
- Treat `output.xml`, `log.html`, and `report.html` as generated test artifacts; do not edit them manually.