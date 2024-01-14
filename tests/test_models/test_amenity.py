#!/usr/bin/python3
"""
Test for amenity class. This script contains unit tests for the Amenity class,
which is a subclass of the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
   A test case for the Amenity class.
   """
    def test_amenity_base_class(self):
        """
        Checks if the Amenity class is a subclass of the BaseModel class.
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_new_instance_class(self):
        """
       Checks if a new instance of the Amenity class is an instance of
       both the BaseModel class and the Amenity class.
       """
        self.assertTrue(isinstance(Amenity(), BaseModel))
        self.assertTrue(isinstance(Amenity(), Amenity))

    def test_name(self):
        """
       Tests the name attribute of the Amenity class.
       """
        new_amenity = Amenity()
        new_amenity.name = "ahmed"
        self.assertEqual(new_amenity.name, "ahmed")
        self.assertEqual(type(new_amenity.name), str)

    def test_types(self):
        """ check attributes type """
        self.assertEqual(type(Amenity().name), str)
