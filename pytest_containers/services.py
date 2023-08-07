from __future__ import annotations

import pathlib
import types
import typing
from dataclasses import dataclass

from .protocols import Runnable


@dataclass
class DockerComposeServices:
    """Access to the underlying docker services."""

    def __init__(self, compose_files: typing.Sequence[pathlib.Path], invoker: Runnable) -> None:
        self.files = compose_files
        self.service: typing.Dict[typing.Any, typing.Any] = {}
        self.invoker = invoker

    def start(self) -> None:
        ...

    def stop(self) -> None:
        return None

    def __enter__(self) -> DockerComposeServices:
        return self

    def __exit__(
        self,
        exc_type: typing.Optional[typing.Type[BaseException]] = None,
        exc_value: typing.Optional[BaseException] = None,
        traceback: typing.Optional[types.TracebackType] = None,
    ) -> typing.Optional[bool]:
        ...
