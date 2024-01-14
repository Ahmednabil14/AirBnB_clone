#!/usr/bin/python3
"""
Test for place class.
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ test cases for place class"""
    def test_place_base_class(self):
        """
        Checks if the place class is a subclass of the BaseModel class.
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_new_instance_class(self):
        """
       Checks if a new instance of the place class is an instance of
       both the BaseModel class and the place class.
       """
        self.assertTrue(isinstance(Place(), BaseModel))
        self.assertTrue(isinstance(Place(), Place))

    def test_attributes(self):
        """ check adding attributes"""
        new = Place()
        new.user_id = "123"
        new.name = "cairo"
        new.city_id = "123"
        new.description = "hello"
        new.number_rooms = 2
        new.number_bathrooms = 1
        new.max_guest = 3
        new.price_by_night = 100
        new.latitude = 1.2
        new.longitude = 3.3
        new.amenity_ids = ["1", "2", "3"]
        self.assertEqual(new.user_id, "123")
        self.assertEqual(new.name, "cairo")
        self.assertEqual(new.city_id, "123")
        self.assertEqual(new.description, "hello")
        self.assertEqual(new.number_rooms, 2)
        self.assertEqual(new.number_bathrooms, 1)
        self.assertEqual(new.max_guest, 3)
        self.assertEqual(new.price_by_night, 100)
        self.assertEqual(new.latitude, 1.2)
        self.assertEqual(new.longitude, 3.3)
        self.assertEqual(new.amenity_ids, ["1", "2", "3"])

    def test_types(self):
        """ check attributes type """
        self.assertEqual(type(Place().user_id), str)
        self.assertEqual(type(Place().name), str)
        self.assertEqual(type(Place().city_id), str)
        self.assertEqual(type(Place().description), str)
        self.assertEqual(type(Place().number_rooms), int)
        self.assertEqual(type(Place().number_bathrooms), int)
        self.assertEqual(type(Place().max_guest), int)
        self.assertEqual(type(Place().price_by_night), int)
        self.assertEqual(type(Place().latitude), float)
        self.assertEqual(type(Place().longitude), float)
        self.assertEqual(type(Place().amenity_ids), list)
