#!/usr/bin/python3
""" Unit tests for the City class."""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Test cases for the City class."""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Test the state_id attribute."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """est the state_id attribute. """
        new = self.value()
        self.assertEqual(type(new.name), str)
