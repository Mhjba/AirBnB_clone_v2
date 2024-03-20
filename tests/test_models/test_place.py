#!/usr/bin/python3


"""Unit tests for the Place class. """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test cases for the Place class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test the city_id attribute. """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """Test the user_id attribute. """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """Test the name attribute. """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """Test the description attribute. """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """Test the number_rooms attribute. """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
