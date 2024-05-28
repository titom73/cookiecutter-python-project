"""{{cookiecutter.__project_slug}} Library."""

import importlib.metadata

__version__ = f"v{importlib.metadata.version('{{cookiecutter.pkg_name}}')}"
__credits__ = [
    "{{cookiecutter.author}} <{{cookiecutter.email}}>",
]
__copyright__ = "Copyright 2022-{{cookiecutter._year}}."


def print_demo(v: str) -> str:
    """Foo function."""
    return v
