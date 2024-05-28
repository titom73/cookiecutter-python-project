# Python Project template

## Overview

Git repository to easily generate structure for a Python 3 project with the following elements:

- `pyproject.toml` for python packaging
- `Ruff`, `Pylint`, `Mypy` configurations
- `tox` configurations
- `pre-commit` hook configuration (__not installed__: run `pre-commit install`)
- `Dockerfile` for easy packaging
- GH actions for standard CI.
- [Drone CI](https://www.drone.io/) for homelab CI.
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
- `project_name`: Project's name (similar to repository name), it will be used to derive a slug,
- `package_name`: default is `{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}`,
- `project_description`: Project description,
- `version`: Initial version of the project,
- `include_github_actions`: Activate or not GH Actions,
- `include_drone_ci`: Activate or not [Drone-CI](https://www.drone.io/)
- `codecov`: Activate or not Codecov,
- `dockerfile`: Activate or not Dockerfile,
- `devcontainer`: Activate or not Devcontainer,
- `open_source_license`: Project's licence type,

### Hidden variables

Some variables are automatically built by cookicutter:

- `__year`: `{% now 'utc', '%Y' %}`,

## Contribution guide

Contributions are welcome. Please refer to the [contribution guide](./CONTRIBUTING.md)

## Licence

The project is published under [Apache-2.0](./LICENCE)
