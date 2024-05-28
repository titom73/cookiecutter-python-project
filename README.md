# Python Project template

## Overview

Git repository to easily generate structure for a Python 3 project with the following elements:

- `pyproject.toml` for python packaging
- `Ruff`, `Pylint`, `Mypy` configurations
- `tox` configurations
- `pre-commit` hook configured (not installed)
- `Dockerfile` for easy packaging
- GH actions for standard CI.
- Devcontainer and VScode settings
- Licence selection

## Getting Started

```bash
# Install cookiecutter (if not already installed)
pipx install cookiecutter

# Create your project (custom git server)
cookiecutter git@git.as73.inetsix.net:tom/cookiecutter-python-project.git

# Create your project (github)
cookiecutter gh:titom73/cookiecutter-python-project.git
```

## Project inputs

This project uses following inputs to build content:

- `author`: Author Full Name
- `email`: Author Email address,
- `author_github_handle`: Git Nickname,
- `git_server`: Git server,
- `project_name`: Project's name (similar to repository name),
- `project_slug`: `{{cookiecutter.project_name|lower|replace('-', '_')}}`,
- `pkg_name`: `{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}`,
- `project_description`: Project description,
- `version`: Initial version of the project,
- `include_github_actions`: Activate or no GH Actions,
- `publish_to`: Where to publish package (not in use),
- `codecov`: Activate or no Codecov,
- `dockerfile`: Activate or no Dockerfile,
- `devcontainer`: Activate or no Devcontainer,
- `open_source_license`: Project's licence type,
- `year`: `{% now 'utc', '%Y' %}`,

## Contribution guide

Contributions are welcome. Please refer to the [contribution guide](./CONTRIBUTING.md)

## Licence

The project is published under [{{cookiecutter.open_source_license}}](./LICENSE)
