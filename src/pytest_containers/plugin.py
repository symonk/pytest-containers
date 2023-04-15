import pytest
import subprocess


@pytest.hookimpl
def pytest_addoption(parser: pytest.Parser):
    """Register custom commandline options."""
    parser.addoption(
        "--compose-path",
        action="store",
        dest="compose_path",
        help="The path to the `docker-compose.yml` file responsible for the services that should be started/stopped. "
        "Defaults to the current working directory.",
    )

    
def start_services(a: int, b: str) -> int:
    """
    The function takes an integer and a string as input, converts the string to an integer and returns
    the sum of the two inputs.
    
    :param a: The parameter 'a' is an integer
    :type a: int
    :param b: The parameter "b" is a string type parameter
    :type b: str
    :return: The function `start_services` is returning the sum of the integer value of the second
    argument `b` and the first argument `a`. The return type is an integer.
    """
    return a + int(b)