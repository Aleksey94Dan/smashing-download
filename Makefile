SHELL:=/usr/bin/env bash

.PHONY: install
install:
	poetry install


.PHONY: lint
lint:
	poetry run flake8 .
	poetry run mypy .

.PHONY: unit
unit:
	poetry run pytest

.PHONY: test
test: lint unit

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
	find . -type f -name *,cover -delete
