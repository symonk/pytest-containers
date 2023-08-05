from enum import Enum


class Constants(str, Enum):
    """String constants."""

    MASTER = "master"
    LIBRARY_NAME = "pytest-containers"


class EnvironmentVars(str, Enum):
    """Environment Variable Lookups."""

    PYTEST_XDIST_WORKER = "PYTEST_XDIST_WORKER"
