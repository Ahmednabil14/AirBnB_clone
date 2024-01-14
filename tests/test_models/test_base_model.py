#!/usr/bin/python3
""" test BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class"""
    def test_instantiation(self):
        """Test instantiation of BaseModel"""
        user = BaseModel()
        self.assertIsInstance(user, BaseModel)

    def test_id(self):
        """Test unique id generation for each instance"""
        user1 = BaseModel()
        user2 = BaseModel()
        self.assertNotEqual(user1.id, user2.id)
        self.assertEqual(str, type(user1.id))

    def test_created_at(self):
        """
       Test creation time attribute
       """
        self.assertEqual(datetime, type(BaseModel().created_at))
        user1 = BaseModel()
        user2 = BaseModel()
        self.assertTrue(user1.created_at < user2.created_at)

    def test_update_at(self):
        """
       Test update time attribute
       """
        user = BaseModel()
        user2 = BaseModel()
        self.assertTrue(user.updated_at < user2.updated_at)
        user.name = "ahmed"
        self.assertTrue(user.updated_at > user.created_at)
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str_builtin(self):
        """
       Test string representation of the model
       """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        expected_out_put = "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_out_put)

    def test_using_kwarg(self):
        """
       Test creating a model with keyword arguments
       """
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()

        dictionary = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                      'created_at': date_time_iso,
                      'my_number': 89,
                      'updated_at': date_time_iso,
                      'name': 'My_First_Model'}
        user = BaseModel(dictionary)
        self.assertEqual(type(user.created_at), type(date_time))
        self.assertEqual(type(user.updated_at), type(date_time))


class Test_To_Dict(unittest.TestCase):
    """
   Test conversion of BaseModel to a dictionary
   """
    def test_to_dict(self):
        """
       Test conversion of BaseModel to a dictionary
       """
        my_model = BaseModel()
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        json = my_model.to_dict()
        self.assertEqual(type(json), dict)
        self.assertEqual(type(json['created_at']), str)
        self.assertEqual(type(json['updated_at']), str)
        self.assertTrue('__class__' in json.keys())
        self.assertEqual(json['__class__'], my_model.__class__.__name__)

    def test_to_dict_with_new_attr(self):
        """
       Test conversion of BaseModel to a dictionary with new attributes
       """
        my_model = BaseModel()
        my_model.name = "ahmed"
        json = my_model.to_dict()
        self.assertTrue('name' in json.keys())


class TestSave(unittest.TestCase):
    """
   Test saving changes made to a BaseModel instance
   """
    def test_update_at(self):
        """
       Test updating the updated_at attribute after saving changes
       """
        user = BaseModel()
        before = user.updated_at
        user.save()
        after = user.updated_at
        self.assertTrue(after > before)
