"""Test script for the Env"""


def test_env_is_qa(app_config):
    """Testing for QA"""
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://myqa-env.com"
    assert port == 80


def test_env_is_dev(app_config):
    """Testing for QA"""

    base_url = app_config.base_url
    port = app_config.app_port
    # assert base_url == "https://mydev-env.com"
    # assert port == 8080

    # Can use the base_url and port to proceed with the process
    # - without explicitly changing anything in the code
