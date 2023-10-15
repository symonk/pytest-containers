import pathlib
import typing


class SubProcessInvoker:
    """A simple object that wraps subprocess executions."""

    def __init__(self, compose_files: typing.Sequence[pathlib.Path]) -> None:
        self.compose_files = compose_files

    def run(self):
        """Run a subprocess."""
