#!/usr/bin/python3
""" test FileSorage class"""

import unittest
import json
from unittest.mock import mock_open, patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import os


class TestFileStorage(unittest.TestCase):
    """ test file storage class"""
    def setUp(self):
        """test setup"""
        FileStorage.__objects = {}
        FileStorage.__file_path = "file.json"

    def test_all(self):
        """ test all"""
        dicObjects = FileStorage.all(self)
        self.assertIsInstance(dicObjects, dict)

    def test_new_method(self):
        """Test the 'new' method by adding an object to the storage"""
        obj = BaseModel()
        FileStorage.new(self, obj)

        """ Assert that the object has been added to the storage"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        objects_dict = FileStorage.all(self)

        self.assertIn(key, objects_dict)
        self.assertIs(objects_dict[key], obj)


class TestReloadMethod(unittest.TestCase):
    """test reload method"""
    def test_reload_method(self):
        """Call the reload method and assert in one go"""
        bs = BaseModel()
        models.storage.new(bs)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bs.id, objs)
