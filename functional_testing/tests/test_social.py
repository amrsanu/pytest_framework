"""Explore Functional testing"""

import requests


def test_twiiter_is_available():
    """Testing the response from twitter"""
    resp = requests.get("http://google.com", timeout=10)
    assert "google" in resp.text
