"""To test the body"""

from pytest import mark


@mark.smoke
@mark.body
def test_body_shield():
    """To test the wind shield"""
    assert True
