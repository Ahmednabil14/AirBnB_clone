#!/usr/bin/python3
"""
This module defines a City class that handles city attributes.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city in the system.
    """
    state_id = ""  # it will be the State.id
    name = ""
