import pathlib
import subprocess
import typing


class ProcessCaller:
    """A simple object that wraps subprocess executions."""

    def __init__(self) -> None: 
        ...
        
    def spawn(self, args: typing.Sequence[str], **kwargs) -> subprocess.CompletedProcess:
        """Run a subprocess.  kwargs are shovelled right through to the
        subprocess run call.
        
        :param: arguments to run.
        """
        return subprocess.run(args=args, **kwargs)
