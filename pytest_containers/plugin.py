import pathlib
import typing

import pytest


@pytest.fixture(scope="session")
def docker_command() -> str:
    """Returns the prefix compose command that is used when executing subprocesses.

    Override this fixture to use something custom, or to use the older style `docker-compose` command.
    """
    return "docker compose"


@pytest.fixture(scope="session")
def docker_compose_files(pytestconfig: pytest.Config) -> typing.Union[pathlib.Path, typing.Sequence[pathlib.Path]]:
    """Returns by default a `docker-compose.yml` that exists in the root directory of the project.  In order to
    customise the docker compose yaml file paths override this fixture and provide a sequence of Paths, all of which
    will be passed to docker compose -f.

    :param pytestconfig: The `pytest.Config` object.
    """
    return tuple(
        pathlib.Path(pytestconfig.rootdir) / "docker-compose.yml",
    )


@pytest.fixture(scope="session")
def docker_services():
    """Wraps a docker compose up and down invocation as a context, yielding the running service objects into the tests
    that need them, guaranteeing to teardown the services cluster after the test session has finished.

    # Todo: This is not `xdist` aware and probably should be; each worker can return the running services rather than
    attempt to compose up in a subprocess.
    """
