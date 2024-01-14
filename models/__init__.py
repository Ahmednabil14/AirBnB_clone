#!/usr/bin/python3
"""Create an instance of FileStorage and Reload data
from the JSON file (if any)
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
