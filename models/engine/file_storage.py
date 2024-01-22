#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    A simple file-based storage class using JSON to store and retrieve objects.
    """

    __file_path = "file.json"  # File path to store data
    __objects = {}  # Dictionary to hold objects

    def __init__(self, *args, **kwargs):
        """
        Initializes the FileStorage instance.
        Args:
            args: Additional arguments (not used in this implementation).
        """
        pass

    def all(self):
        """:
        Returns all stored objects.
        Returns:
            dict: A dictionary containing all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.
        Args:
            obj: Object to be added to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Saves the current state of objects to a JSON file.
        """
        serializeObj = {}
        for key, obj in FileStorage.__objects.items():
            serializeObj[key] = obj.to_dict() if isinstance(
                obj, BaseModel) else obj
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serializeObj, file)

    def reload(self):
        """Deserializes the JSON file to __objects if it exists;
            otherwise, do nothing."""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                try:
                    objDict = json.load(file)
                    for key, value in objDict.items():
                        FileStorage.__objects[key] = eval(
                            value['__class__'])(**value)
                except json.JSONDecodeError:
                    return
