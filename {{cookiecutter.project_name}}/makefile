## Setup the venv
.PHONY: venv install precommit lint tests black ci
venv:
	python -m venv venv
	python -m venv dev_venv

## Install your dependencies
install:
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	pip-compile --output-file requirements.txt requirements.in requirements_dev.in
	python -m  pip install coverage
	python -m pip install -r requirements.txt

## Run all pre-commit hooks
precommit:
	pre-commit run --all-file --show-diff-on-failure

## Lint your code using pylint
lint:
	python -m pylint --version
	find . -type f -name "*.py" | xargs python -m pylint

## Run tests using pytest
test:
	python -m pytest --version
	python -m pytest tests

## Format your code using black
black:
	python -m black --version
	python -m black *.py

## Run ci part
ci: precommit tests
