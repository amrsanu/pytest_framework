"""Explore Functional testing"""

import requests


def test_sucessfull_request():
    """Testing the response"""
    resp = requests.get("http://google.com", timeout=10)
    assert resp.status_code == 200
