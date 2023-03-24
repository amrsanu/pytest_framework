"""Defining Fixtures"""

from pytest import fixture
import json

DATA_PATH = "tests/test_data.json"


@fixture(params=["Samsung", "Sony", "LG", "MI"])
def tvs(request):
    """Defining fixture for tv brands"""
    # request.param will change 4 times here for all the values of params
    # - Leaving the test function using 'tvs' fixture to run for 4 times for all the params
    tv_brand = request.param
    yield tv_brand


def load_test_data(path):
    """To read and return the json data"""
    with open(path, "r", encoding="utf-8") as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data(DATA_PATH))
def test_data(request):
    """Reading tv_brands from data file"""
    data = request.param
    yield data
