.PHONY: fmt lint test

fmt:
	poetry run ruff check --fix-only . && \
	poetry run black .

lint:
	poetry run black --check .
	poetry run ruff check .

test:
	poetry run python tests/test_strenum.py
