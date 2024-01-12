## Setup the venv
.PHONY: mamba create_env update_env dev setup_precommit precommit lint test format ci

mamba:
	/bin/bash ./scripts/install_mamba.sh

create_env:
	/bin/bash ./scripts/create_env.sh

update_env:
	/bin/bash ./scripts/update_env.sh

## Install dev dependencies
## Make sure this is after you have activated the conda environment
dev:
	python -m pip install --upgrade pip
	python -m pip install -r requirements_dev.txt

## Install precommit hooks
setup_precommit:
	pre-commit install

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
format:
	python -m black --version
	python -m black *.py

## Run ci part
ci: precommit tests
