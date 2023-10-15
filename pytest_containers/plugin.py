import pathlib
import typing

import pytest

from .constants import Constants
from .process_spawner import ProcessCaller
from .services import DockerComposeServices


@pytest.hookimpl
def pytest_addoption(parser: pytest.Parser) -> None:
    """Register the plugins command line arguments.

    :params parser: The pytest custom argparser.

    """
    group = parser.getgroup("pytest-containers")
    group.addoption(
        "--keep-alive",
        action="store_true",
        default=False,
        dest="keep_alive",
        help="Keep the compose services running after pytest has exited.",
    )
    group.addoption(
        "--no-docker",
        action="store_true",
        default=False,
        dest="no_docker",
        help="Do not register the plugin, no services will be started.",
    )


@pytest.hookimpl
def pytest_configure(config: pytest.Config) -> None:
    """Conditionally register the plugin."""
    if not config.option.no_docker:
        config.pluginmanager.register(
            plugin=PytestContainersPlugin(config=config, invoker=ProcessCaller()),
            name=Constants.LIBRARY_NAME,
        )


class PytestContainersPlugin:
    """The core pytest-container plugin."""

    def __init__(self, config: pytest.Config, invoker) -> None:
        self.pytestconfig = config
        self.process_invoker = invoker

    @pytest.hookimpl
    def pytest_sessionstart(self) -> None:
        """Handle compose specifics."""


# ----- Fixtures -----


@pytest.fixture(scope="session")
def docker_command() -> str:
    """Returns the prefix compose command that is used when executing subprocesses.

    Override this fixture to use something custom, or to use the older style `docker-compose` command.

    """
    return "docker compose"


@pytest.fixture(scope="session")
def docker_compose_files(
    pytestconfig: pytest.Config,
) -> typing.Union[pathlib.Path, typing.Sequence[pathlib.Path]]:
    """Returns by default a `docker-compose.yml` that exists in the root directory of the project.  In order to
    customise the docker compose yaml file paths override this fixture and provide a sequence of Paths, all of which
    will be passed to docker compose -f.

    :param pytestconfig: The `pytest.Config` object.

    """
    return (pathlib.Path(pytestconfig.rootdir) / Constants.COMPOSE_YML,)


@pytest.fixture(scope="session")
def docker_services(docker_compose_files, docker_command) -> typing.Generator[DockerComposeServices, None, None]:
    """Wraps a docker compose up and down invocation as a context, yielding the running service objects into the tests
    that need them, guaranteeing to teardown the services cluster after the test session has finished.

    # Todo: This is not `xdist` aware and probably should be; each worker can return the running services rather
    than attempt to compose up in a subprocess.

    """
    with DockerComposeServices(
        process_spawner=ProcessCaller(),
        compose_files=docker_compose_files,
        compose_command=docker_command,
    ) as services:
        # automatically compose `down` the services after the pytest session has finished.
        yield services


@pytest.fixture(scope="session")
def docker_project_name() -> str:
    """The project name passed to `-p` for docker compose when starting the project.

    By default the name utilises the pid of the pytest process.

    """
    # Todo: Implement.
    return "pytest_1"
