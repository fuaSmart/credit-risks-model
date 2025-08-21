# Makefile for build automation

.PHONY: install test lint format

# Install all project dependencies from requirements.txt
install:
	pip install -r requirements.txt

# Run all tests using pytest
test:
	pytest -v tests/

# Check for style issues and errors with flake8
lint:
	flake8 scripts/ tests/ api/

# Automatically format code with black
format:
	black scripts/ tests/ api/