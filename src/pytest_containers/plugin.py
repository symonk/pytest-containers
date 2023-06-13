import os
import pathlib
import typing
import pytest


@pytest.hookimpl
def pytest_addoption(parser: pytest.Parser):
    """Register custom commandline options."""
    parser.addoption(
        "--docker-compose-path",
        action="store",
        dest="docker_compose_path",
        type=pathlib.Path,
        default=os.getcwd,
        help="The path to the `docker-compose.yml` file responsible for the services that should be started/stopped. "
        "Defaults to the current working directory.",
    )


@pytest.fixture(scope="session")
def docker_compose_files(pytestconfig: pytest.Config) -> typing.Sequence[str]:
    """Returns the full path to the compose file used for service startup.

    # Todo: We should probably allow multiple compose files.
    :param pytestconfig: The pytest config object.
    """
    return pytestconfig.option.docker_compose_path


@pytest.fixture(scope="session")
def docker_services():
    """Wraps a docker compose up and down invocation as a context, yielding the running service objects into the tests
    that need them, guaranteeing to teardown the services cluster after the test session has finished.

    # Todo: This is not `xdist` aware and probably should be; each worker can return the running services rather than
    attempt to compose up in a subprocess.
    """
