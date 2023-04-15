
def test_httpbin_is_available(pytester):
    pytester.makepyfile(
    """
    def test_services_are_running():
        assert True
    """
    )
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)