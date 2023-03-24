"""To test the body"""

from pytest import mark


@mark.body
class TestBody:
    """Class to group all the body test"""

    @mark.smoke
    def test_body_shield(self):
        """To test the shield"""
        assert True

    @mark.door
    def test_body_door(self):
        """To test the door"""
        assert True

    def test_body_bumper(self):
        """To test the bumper"""
        assert True

    def test_windshield(self):
        """To test the wind shield"""
        assert True

    def test_body_back_light(self):
        """To test the back_light"""
        assert True

    @mark.ui
    def test_get_car_name(self, available_cars):
        """To test the back_light"""
        assert "Bumblebee" in available_cars
