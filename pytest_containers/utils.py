import os
import pathlib

from .constants import Constants
from .constants import EnvironmentVars


def is_docker_compose_file(path: pathlib.Path) -> bool:
    """Checks the docker compose file path is a valid compose file."""
    return False


def is_xdist_worker() -> bool:
    """Decipher if the executable pytest process is one of an xdist execnet gateway/worker."""
    return os.environ.get(EnvironmentVars.PYTEST_XDIST_WORKER, Constants.MASTER) == Constants.MASTER
