"""To test the start"""

from pytest import mark


@mark.smoke
# Custom mark
@mark.engine
def test_self_start():
    """To test the start"""
    assert True
