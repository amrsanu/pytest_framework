"""Pytest self configuration script to pick the Fixtures and other info"""

from pytest import fixture
from config import Config


def pytest_addoption(parser):
    """Pytest adoption to argparse to get the command line input. Adds custom option to pytest
    - parser: inbuilt fixture for parsing"""

    parser.addoption(
        "--env", action="store", help="Environment to run the tests against."
    )


@fixture(scope="session")
def env(request):
    """Custom fixture to provide the test function with the environment variable.
    - request: inbuilt fixture to store the information related to tests
    """
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    """To create the object of the Config and return to the test function
    Easier to get the Environment settings for a specific test dev/qa"""
    cfg = Config(env)
    return cfg
