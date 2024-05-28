"""
This example script imports the {{cookiecutter.pkg_name}} package and
prints out the version.
"""

import {{cookiecutter.pkg_name}}


def main():
    print(f"{{cookiecutter.pkg_name}} version: {% raw -%}{{%- endraw %}{{cookiecutter.pkg_name}}.__version__{% raw -%}}{%- endraw %}")


if __name__ == "__main__":
    main()
