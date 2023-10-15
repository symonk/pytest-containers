from dataclasses import dataclass
from enum import StrEnum


class Constants(StrEnum):
    """String constants."""

    MASTER = "master"
    LIBRARY_NAME = "pytest-containers"
    COMPOSE_YML = "docker-compose.yml"


class EnvironmentVars(StrEnum):
    """Environment Variable Lookups."""

    PYTEST_XDIST_WORKER = "PYTEST_XDIST_WORKER"
