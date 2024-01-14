Welcome to the AirBnB clone project!
Project Overview
Purpose
Build a command interpreter to manage AirBnB objects.
Lay the foundation for a full web application (AirBnB clone).
Key Steps
Create a parent class (BaseModel) for initialization, serialization, and deserialization.
Implement serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
Create classes for AirBnB objects (User, State, City, Place) inheriting from BaseModel.
Develop the first abstracted storage engine: File storage.
Write unittests to validate all classes and the storage engine.
Command Interpreter
Similar to a Shell, but specific to managing AirBnB objects.
Operations include creating, retrieving, counting, computing stats, updating attributes, and destroying objects.
Resources
Utilize Python modules such as cmd, uuid, datetime, and unittest.
Reference Python documentation for cmd, packages, uuid, datetime, and unittest.
Explore args/kwargs and understand how to handle named arguments in functions.
Learning Objectives
General
Create a Python package.
Develop a command interpreter using the cmd module.
Understand and implement Unit testing in a large project.
Learn how to serialize and deserialize a class.
Practice writing and reading JSON files.
Manage datetime and UUID in Python.
Understand and use *args and **kwargs.
Handle named arguments in functions.