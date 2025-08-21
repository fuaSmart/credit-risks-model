

.PHONY: install test lint format


install:
	pip install -r requirements.txt


test:
	pytest -v tests/


lint:
	flake8 scripts/ tests/ api/


format:
	black scripts/ tests/ api/