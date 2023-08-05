import pytest


def test_docker_compose_default_is_correct(pytester: pytest.Pytester) -> None:
    # Todo: Assertion is lackluster
    pytester.makepyfile(
        """
        def test_default_compose_files(docker_compose_files, tmpdir):
            assert docker_compose_files[0].name == "docker-compose.yml"
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
