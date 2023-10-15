from __future__ import annotations

import pathlib
import subprocess
import types
import typing

from .protocols import Spawnable


class DockerComposeServices:
    """Access to the underlying docker services."""

    def __init__(
        self,
        compose_files: typing.Sequence[pathlib.Path],
        subproc_caller: Spawnable,
        compose_command: str,
    ) -> None:
        self.compose_files = compose_files
        self.services: typing.Dict[typing.Any, typing.Any] = {}
        self.subproc_caller = subproc_caller
        self.compose_command = compose_command

    def start(self) -> subprocess.CompletedProcess:
        """Attempt to start the docker services."""
        result = self.subproc_caller.spawn(
            args=(self.compose_command, "--file", str(self.compose_files[0]), "up"),
            shell=True,  # Todo: Resolve not using this.
            capture_output=True,
        )
        return result

    def stop(self) -> None:
        """Stop the docker compose services."""

    def __enter__(self) -> DockerComposeServices:
        self.start()
        return self

    def __exit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]] = None,
        exc_value: typing.Optional[BaseException] = None,
        traceback: typing.Optional[types.TracebackType] = None,
    ) -> typing.Optional[bool]:
        return None
