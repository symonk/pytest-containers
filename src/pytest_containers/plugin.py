import pytest


@pytest.hookimpl
def pytest_addoption(parser: pytest.Parser):
    """Register custom commandline options."""
    parser.addoption(
        "--compose-path",
        action="store",
        dest="compose_path",
        help="The path to the `docker-compose.yml` file responsible for the services that should be started/stopped. "
        "Defaults to the current working directory.",
    )
