# Agent Instructions

## Project

- This is a dependency-free Python 3.14 project. Use the version in `.python-version` and manage execution with `uv`.
- Source files live directly under `src/`; there is no package build step or test suite in this repository.
- Keep changes focused on the query-language exercise and preserve the existing simple module layout.

## Architecture

- `player.py` defines the data model and computed `points` property.
- `player_reader.py` downloads and parses the semicolon-separated NHL player data.
- `statistics.py` owns player collection queries and delegates predicate evaluation to matchers.
- `matchers.py` contains composable predicates. Matchers expose `test(player)`.
- `query_builder.py` provides the fluent query API. Builder methods return a new `QueryBuilder`; do not mutate an existing builder when adding operations.
- `index.py` is the executable example and entry point.

## Development

- Run the example with `uv run python src/index.py`. It requires network access to the NHL statistics URL in `src/index.py`.
- Run a syntax check with `uv run python -m compileall src`.
- There are currently no automated tests, lint settings, or formatting settings. Add focused tests before making broad behavior changes.
- Keep public method names and the matcher protocol stable unless the task explicitly asks for an API change.
- Prefer the standard library and existing abstractions. Avoid adding dependencies for this small exercise.

## Change Guidance

- Keep imports and module boundaries consistent with the existing files, which are designed to run from the `src` entry point.
- When changing parsing or filtering behavior, validate both normal records and malformed/empty input where relevant.
- Do not commit generated output, virtual-environment files, or downloaded player data.