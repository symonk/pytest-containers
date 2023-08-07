import pytest


@pytest.mark.skip(reason="not registering properly")
def test_class_plugin_is_loaded_by_default(pytester: pytest.Pytester):
    pytester.makepyfile(
        """
        def test_no_plugin(pytestconfig) -> None:
            assert pytestconfig.pluginmanager.has_plugin("pytest-containers")
        """,
    )
    result = pytester.runpytest([])
    result.assert_outcomes(passed=1)


@pytest.mark.skip(reason="not registering properly")
def test_disable_docker_does_not_register_plugin(pytester: pytest.Pytester):
    pytester.makepyfile(
        """
        def test_no_plugin(pytestconfig) -> None:
            assert not pytestconfig.pluginmanager.has_plugin("pytest-containers")
        """,
    )
    result = pytester.runpytest(["--disable-docker"])
    result.assert_outcomes(passed=1)
