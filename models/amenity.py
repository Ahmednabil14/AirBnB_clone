#!/usr/bin/python3
"""
This module defines an Amenity class that handles amenity attributes.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity in the system.

    Attributes
    ----------
    name : str
        The name of the amenity.
    """
    name = ""
