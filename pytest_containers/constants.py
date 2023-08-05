from dataclasses import dataclass

@dataclass
class Constants:
    """String constants."""

    MASTER = "master"
    LIBRARY_NAME = "pytest-containers"
    COMPOSE_YML = "docker-compose.yml"

@dataclass
class EnvironmentVars:
    """Environment Variable Lookups."""

    PYTEST_XDIST_WORKER = "PYTEST_XDIST_WORKER"
