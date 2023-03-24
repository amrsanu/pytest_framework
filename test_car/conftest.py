"""To define the test configurations
Defining the fixtures for the tests.
"""
from random import choice

from pytest import fixture


@fixture(scope="function")
def available_cars():
    """Car name generator"""
    cars_names = [
        "Bumblebee",
        "Oatmeal",
        "Party Wagon",
        "Gina",
        "Bessie",
        "Battle Shell",
        "The Beast",
        "Rascal, Arrowcar",
        "Boomer Siren",
        "Underdog",
        "Turtle Taxi",
        "Waggy",
        "Guardian",
        "Spit Fires",
        "Jitter Bug",
        "Wired",
    ]
    yield cars_names

    print("------ Tear down CAR Names ----------------------------------")
