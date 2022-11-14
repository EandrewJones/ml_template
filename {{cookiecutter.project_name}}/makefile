## Setup the venv
.PHONY: venv
venv:
	python -m venv venv
	python -m venv dev_venv
## Install your dependencies
.PHONY: install
install:
	python -m pip install --upgrade pip
	python -m pip install pip-tools
	pip-compile --output-file requirements.txt requirements.in requirements_dev.in
	python -m  pip install coverage
	python -m pip install -r requirements.txt
## Run all pre-commit hooks
.PHONY: precommit
precommit:
	pre-commit run --all-file --show-diff-on-failure
## Lint your code using pylint
.PHONY: lint
lint:
	python -m pylint --version
	find . -type f -name "*.py" | xargs python -m pylint
## Run tests using pytest
.PHONY: tests
test:
	python -m pytest --version
	python -m pytest tests
## Format your code using black
.PHONY: black
black:
	python -m black --version
	python -m black *.py
## Run ci part
.PHONY: ci
ci: precommit tests
