import pytest


def test_default_compose_command(pytester: pytest.Pytester) -> None:
    pytester.makepyfile(
        """
        def test_override_docker_command(docker_command) -> None:
            assert docker_command == "docker compose"
        """,
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


def test_overriding_docker_compose_command_works(pytester: pytest.Pytester) -> None:
    pytester.makeconftest(
        """
    import pytest

    @pytest.fixture(scope='session')
    def docker_command() -> str:
        return "dockercompose"
    """,
    )
    pytester.makepyfile(
        """
        def test_override_docker_command(docker_command) -> None:
            assert docker_command == "dockercompose"
        """,
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


def test_docker_compose_default_is_correct(pytester: pytest.Pytester) -> None:
    pytester.makepyfile(
        """
        def test_default_compose_files(docker_compose_files, tmpdir):
            assert str(docker_compose_files[0]).endswith("docker-compose.yml")
        """,
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)


def test_docker_compose_path_is_a_path(pytester: pytest.Pytester) -> None:
    pytester.makeconftest(
        """
    import pytest

    @pytest.fixture(scope="session")
    def docker_compose_files(pytestconfig):
        return "bar"
    """,
    )
    pytester.makepyfile(
        """
        def test_injected_value(docker_compose_files):
            assert docker_compose_files == "bar"
        """,
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
