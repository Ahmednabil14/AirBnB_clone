#!/usr/bin/python3
"""
Test for State class.
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ test cases for State class"""
    def test_state_base_class(self):
        """
        Checks if the state class is a subclass of the BaseModel class.
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_new_instance_class(self):
        """
       Checks if a new instance of the State class is an instance of
       both the BaseModel class and the State class.
       """
        self.assertTrue(isinstance(State(), BaseModel))
        self.assertTrue(isinstance(State(), State))

    def test_attributes(self):
        """ check adding attributes"""
        new = State()
        new.name = "cairo"
        self.assertEqual(new.name, "cairo")

    def test_types(self):
        """ check attributes type """
        self.assertEqual(type(State().name), str)
