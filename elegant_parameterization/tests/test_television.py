"""Test script for Television"""

import pytest


@pytest.mark.parametrize(
    "tv_brand",
    [
        ("Samsung"),
        ("sony"),
        ("Vizio"),
    ],
)
def test_television_is_on(tv_brand):
    """Test the tv brands for the given parameters"""
    print(f"{tv_brand} turns on as expected")

