#!/usr/bin/python3
"""Unit tests for the Review class."""


from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test cases for the Review class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test the place_id attribute. """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test the user_id attribute. """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test the text attribute """
        new = self.value()
        self.assertEqual(type(new.text), str)
