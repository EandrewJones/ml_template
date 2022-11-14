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
|- bin/          # contains scripts and main files that should be run
|- config/       # config files
|- notebooks/    # notebooks for EDA and exploration
|- secrets       # contains api keys and secret parameters. It should be ignored from git
|- src/          # source code - contains functions
|- tests/        # Test files should mirror the src folder
|- Makefile      # automatize taks through make utility
```

## 🏁 Getting Started <a name = "getting_started"></a>

### Clone the project

```bash
$ git clone {{cookiecutter.gitlab_repo_url}}
```

### Prerequisites

Setup your environement and install project dependencies

```
conda create -n {{cookiecutter.project_name}} python={{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}
source activate {{cookiecutter.project_name}}

python -m pip install pip-tools
pip-compile --output-file requirements.txt requirements.in requirements_dev.in
python -m pip install -r requirements.txt
```

### Installing

## 🔧 Running the tests

Tests are implemented in ./tests, you need to run the following command to run them.

```
make tests
```

## 🚀 Deployment

Add additional notes about how to deploy this on a live system.

## ✍️ Authors

{{cookiecutter.full_name}} - {{cookiecutter.email}}
