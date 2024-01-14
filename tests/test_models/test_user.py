#!/usr/bin/python3
""" Test User Unittest module
"""

import unittest
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def test_inheritance(self):
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user, User)

    def test_public_attributes(self):
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')

    def test_custom_attributes(self):
        user = User()
        user.email = 'test@example.com'
        user.password = 'pass'
        user.first_name = 'elias'
        user.last_name = 'elias'

        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'pass')
        self.assertEqual(user.first_name, 'elias')
        self.assertEqual(user.last_name, 'elias')

    def test_id(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)
        self.assertEqual(str, type(user1.id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))
        user1 = User()
        user2 = User()
        self.assertTrue(user1.created_at < user2.created_at)

    def test_update_at(self):
        user = User()
        user2 = User()
        self.assertTrue(user.updated_at < user2.updated_at)
        user.name = "ahmed"
        self.assertTrue(user.updated_at > user.created_at)
        self.assertEqual(datetime, type(User().updated_at))

    def test_str_builtin(self):
        my_model = User()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        expected_out_put = "[{}] ({}) {}".format(
            my_model.__class__.__name__, my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_out_put)

    def test_using_kwarg(self):
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()

        dictionary = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                      'created_at': date_time_iso,
                      'my_number': 89,
                      'updated_at': date_time_iso,
                      'name': 'My_First_Model'}
        user = User(dictionary)
        self.assertEqual(type(user.created_at), type(date_time))
        self.assertEqual(type(user.updated_at), type(date_time))


class Test_To_Dict(unittest.TestCase):
    def test_to_dict(self):
        my_model = User()
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        json = my_model.to_dict()
        self.assertEqual(type(json), dict)
        self.assertEqual(type(json['created_at']), str)
        self.assertEqual(type(json['updated_at']), str)
        self.assertTrue('__class__' in json.keys())
        self.assertEqual(json['__class__'], my_model.__class__.__name__)

    def test_to_dict_with_new_attr(self):
        my_model = User()
        my_model.name = "ahmed"
        json = my_model.to_dict()
        self.assertTrue('name' in json.keys())


class TestSave(unittest.TestCase):
    def test_update_at(self):
        user = User()
        before = user.updated_at
        user.save()
        after = user.updated_at
        self.assertTrue(after > before)
