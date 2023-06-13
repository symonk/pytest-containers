import pathlib
import typing

import pytest


@pytest.fixture(scope="session")
def docker_compose_files(pytestconfig: pytest.Config) -> typing.Union[pathlib.Path, typing.Sequence[pathlib.Path]]:
    """Returns the full path to the compose file used for service startup.

    :param pytestconfig: The pytest config object.
    """
    return pathlib.Path(pytestconfig.rootdir) / "docker-compose.yml"


@pytest.fixture(scope="session")
def docker_services():
    """Wraps a docker compose up and down invocation as a context, yielding the running service objects into the tests
    that need them, guaranteeing to teardown the services cluster after the test session has finished.

    # Todo: This is not `xdist` aware and probably should be; each worker can return the running services rather than
    attempt to compose up in a subprocess.
    """
