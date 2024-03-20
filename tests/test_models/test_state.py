#!/usr/bin/python3
"""Unit tests for the State class."""


from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test cases for the State class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Test the name attribute. """
        new = self.value()
        self.assertEqual(type(new.name), str)
