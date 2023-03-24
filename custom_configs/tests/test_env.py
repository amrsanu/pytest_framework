"""Test script for the Env"""

from pytest import mark


def test_env_is_qa(app_config):
    """Testing for QA"""
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://myqa-env.com"
    assert port == 80


@mark.skip(reason="Broken as we are using QA as env")
def test_env_is_dev(app_config):
    """Testing for QA"""

    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://mydev-env.com"
    assert port == 8080

    # Can use the base_url and port to proceed with the process
    # - without explicitly changing anything in the code


@mark.xfail(reason="Staging is not implemented in the env")
def test_env_is_staging(app_config):
    """Testing for Staging files"""
    base_url = app_config.base_url
    assert base_url == "staging"
