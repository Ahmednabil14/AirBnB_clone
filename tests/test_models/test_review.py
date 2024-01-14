#!/usr/bin/python3
"""
Test for review class.
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ test cases for review class"""
    def test_review_base_class(self):
        """
        Checks if the review class is a subclass of the BaseModel class.
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_new_instance_class(self):
        """
       Checks if a new instance of the review class is an instance of
       both the BaseModel class and the review class.
       """
        self.assertTrue(isinstance(Review(), BaseModel))
        self.assertTrue(isinstance(Review(), Review))

    def test_attributes(self):
        """ check adding attributes"""
        new = Review()
        new.place_id = "123"
        new.user_id = "567"
        new.text = "hi"
        self.assertEqual(new.place_id, "123")
        self.assertEqual(new.user_id, "567")
        self.assertEqual(new.text, "hi")

    def test_types(self):
        """ check attributes type """
        self.assertEqual(type(Review().place_id), str)
        self.assertEqual(type(Review().user_id), str)
        self.assertEqual(type(Review().text), str)
