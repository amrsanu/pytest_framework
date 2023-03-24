"""Test script for Television"""

import pytest


@pytest.mark.skip(reason="skipping got a better option ..........")
@pytest.mark.parametrize(
    "tv_brand",
    [
        ("Samsung"),
        ("sony"),
        ("Vizio"),
    ],
)
def test_television_is_on_marker(tv_brand):
    """Test the tv brands for the given parameters"""
    print(f"{tv_brand} turns on as expected")


def test_tv_is_on(tvs):
    """Test the tv brands for the given parameters"""
    print(f"{tvs} turns on as expected")


def test_television_is_on_fixture(test_data):
    """Test the tv brands for the given parameters"""
    print(f"{test_data} turns on as expected")
