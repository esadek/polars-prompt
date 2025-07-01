alias fmt := format

default: format lint

dev:
    uv run src/polars_prompt/main.py

format:
    uv run ruff format

lint:
    uv run ruff check --fix

test:
    uv run pytest

test-all:
    uv run nox
