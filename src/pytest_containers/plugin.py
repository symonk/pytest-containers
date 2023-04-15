import os
import pathlib

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
def docker_compose_file(pytestconfig: pytest.Config) -> str:
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


def start_services(a: int, b: str) -> int:
    """The function takes an integer and a string as input, converts the string to an integer and returns the sum of the
    two inputs.

    :param a: The parameter 'a' is an integer
    :type a: int
    :param b: The parameter "b" is a string type parameter
    :type b: str
    :return: The function `start_services` is returning the sum of the integer value of the second
    argument `b` and the first argument `a`. The return type is an integer.
    """
    return a + int(b)
