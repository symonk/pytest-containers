import pathlib


def resolve_docker_compose_command() -> str:
    """Returns the command to use for launching docker compose for the system."""
    return ""


def is_docker_compose_file(path: pathlib.Path) -> bool:
    """Checks the docker compose file path is a valid compose file."""
    return False
