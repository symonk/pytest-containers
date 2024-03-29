#!/bin/env python
import subprocess
import sys
import typing


def main() -> int:
    return_code = 0
    return_code += remove_lock_if_exists()
    return_code += poetry_update()
    return_code += pre_commit_update()
    return_code += poetry_upgrade()
    if not return_code:
        print("Updating dependencies on the remote now.")
        commit_and_push()
    else:
        print("No dependencies to update.")
    return return_code


def remove_lock_if_exists():
    return _run_command(("rm", "-f", "poetry.lock"))


def poetry_upgrade():
    return _run_command(("poetry", "up", "--latest"))


def poetry_update():
    return _run_command(("poetry", "update"))


def pre_commit_update():
    return _run_command(("pre-commit", "autoupdate", "--bleeding-edge"))


def commit_and_push():
    return (
        _run_command(("git", "add", "poetry.lock", ".pre-commit-config.yaml", "pyproject.toml"))
        + _run_command(("git", "commit", "-m", "`(chore)` :rocket: `dependency upgrades`."))
        + _run_command(("git", "push"))
    )


def _run_command(command: typing.Tuple[str, ...]) -> int:
    """Run a command and return the subprocess exit code.

    :param command: Command to run.
    :return:

    """
    return subprocess.run(command, stdout=sys.stdout, stderr=subprocess.STDOUT).returncode


if __name__ == "__main__":
    """A rather naive utility script for updating poetry and pre-commit dependencies."""
    raise SystemExit(main())
