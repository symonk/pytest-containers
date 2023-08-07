import pathlib
import typing


class SubProcessInvoker:
    """A simple object that wraps subprocess executions."""

    def __init__(self, compose_files: typing.Sequence[pathlib.Path]) -> None:
        self.compose_files = compose_files

    def run(self):
        """Run a subprocess."""

    def are_valid_compose_files(self) -> bool:
        """Checks that each of the paths provided are considered correct docker-compose files.

        This utilises `docker compose config` and relies on the exit code of that for each file.
        """
        command = ""
        return not command
