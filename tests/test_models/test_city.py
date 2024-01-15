#!/usr/bin/python3
"""
Test for city class.
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ test cases for city class"""
    def test_city_base_class(self):
        """
        Checks if the city class is a subclass of the BaseModel class.
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_new_instance_class(self):
        """
       Checks if a new instance of the city class is an instance of
       both the BaseModel class and the city class.
       """
        self.assertTrue(isinstance(City(), BaseModel))
        self.assertTrue(isinstance(City(), City))

    def test_attributes(self):
        """ check adding attributes"""
        new_city = City()
        new_city.state_id = "123"
        new_city.name = "cairo"
        self.assertEqual(new_city.state_id, "123")
        self.assertEqual(new_city.name, "cairo")

    def test_types(self):
        """ check attributes type """
        self.assertEqual(type(City().state_id), str)
        self.assertEqual(type(City().name), str)
