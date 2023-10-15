import pytest


def test_docker_compose_is_started(pytester: pytest.Pytester, pytestconfig) -> None:
    pytester.makeconftest(
        """
                          import pytest
                          import pathlib

                          @pytest.fixture(scope='session')
                          def docker_compose_files(pytestconfig):
                            return (pathlib.Path(pytestconfig.rootdir) / "docker_compose.yml",)
                          """,
    )
    pytester.makefile(
        ".yml",
        docker_compose="""
    version: '2'
    services:
        httpbin:
            image: 'kennethreitz/httpbin'
            ports:
                - '7777:80'
            healthcheck:
                test: ["CMD", "curl", "-f", "http://localhost:80/anything"]
                interval: 30s
                timeout: 10s
                retries: 5
    """,
    )
    pytester.makepyfile(
        """
                        def test_with_services(docker_services):
                            assert True
                        """,
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
