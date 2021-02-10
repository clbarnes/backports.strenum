.PHONY: fmt lint test

fmt:
	black .

lint:
	black --check .
	flake8 backports

test:
	python tests/test_strenum.py
