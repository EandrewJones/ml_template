# template_ds_project

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">{{cookiecutter.project_name}}</h3>

<div align="center">

[![code coverage](coverage.svg "Code coverage")]()

</div>

---

## 🧐 About <a name = "about"></a>

{{cookiecutter.project_short_description}}

## 🔖 Project structure

```
Project_folder/
|- bin/          # Contains entrypoints for the docker container
|- config/       # Config files
|- notebooks/    # notebooks for EDA, exploration, and model training
|- secrets       # Contains api keys and secret parameters. It should be ignored from git
|- src/          # Source code - contains FastAPI app and any other source code for the models
|- tests/        # Test files 
|- weights/      # Contains model weights
|- Makefile      # Automate tasks through make utility
```

## 🏁 Getting Started <a name = "getting_started"></a>

### Clone the project

```bash
$ git clone {{cookiecutter.git_repo_url}}
```

### Prerequisites

This project assumes you have Conda installed as a package manager. It then uses Conda to install Mamba, a re-implementation of the conda package manager in C++. It is faster than conda and has a more robust dependency solver.


```bash
make mamba
```

### Initializing the Dependency Environment

The project utilizes a `Makefile`` to simplify routine tasks. The first time you run the poject, you need to create the mamba (conda) environment and activate it. You will never need to create the environment again; however, you will need to activate it every time you start a new terminal session.

```bash
make create_env
mamba activate {{ cookiecutter.environment_name }}
```

---
**NOTE**

The script that creates the env is NOT idempotent. If you run it a second time, it will not overwrite the existing environment. If you need to update the environment because the dependencies have changed, there is a separate command for that.

---

For development, you need to install the additional development dependencies. See `requirements_dev.txt` for the full list of dependencies or in case you need to make changes. These are intentionally specified outside the conda environment so that they are not bundled into the production environment.

```bash
make dev
```

This project uses pre-commit hooks to ensure that the code is formatted correctly and that the tests pass before committing. To install the pre-commit hooks, run the following command:

```bash
make setup_precommit
```

### Updating Dependencies

If you make changes to **production** dependencies, you need to manually update the `environment.yml`. We *encourage pinning versions of dependencies whenever possible* to increase reproducibility. Once you've updated the file, you can update the environment with the following command:

```bash
make update_env
```

If you need to update the **development** dependencies, you must change the `requirements_dev.txt` file. Once you've updated the file, you can update the environment with the following command:

```bash
make create_dev
```


## 🔧 Utility Methods

### Running tests
Tests are implemented in ./tests, you need to run the following command to run them.

```bash
make test
```

### Precommit hooks

The precommit hooks will run before committing the code; however, if you would like to run them manually, you can run the following command:

```bash
make precommit
```

### Linting

Linting is done with pylint. To run the linter, run the following command:

```bash
make lint
```

### Formatting

Formatting is done with black. To run the formatter, run the following command:

```bash
make format
```

## 🚀 Deployment

Add additional notes about how to deploy this on a live system.

## ✍️ Authors

{{cookiecutter.full_name}} - {{cookiecutter.email}}
