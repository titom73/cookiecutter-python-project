"""{{cookiecutter.pkg_name}} Tests."""

from {{cookiecutter.pkg_name}} import print_demo


def test_demo() -> None:
    """Test demo function."""
    assert print_demo("foo") == "foo"
