#!/usr/bin/python3
"""
Base class that is the parent class for all classes
"""

import uuid
import datetime
import models


class BaseModel:
    """
    the parent class
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """ unformal string form of the class"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        class method that updates the public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        class method that returns a dictionary containing
        all keys/values of __dict__ of the instance.

        convert created_at & updated_at to string object in ISO format.
        """
        c_dic = self.__dict__.copy()
        c_dic['__class__'] = self.__class__.__name__
        c_dic['created_at'] = self.created_at.isoformat()
        c_dic['updated_at'] = self.updated_at.isoformat()
        return c_dic
