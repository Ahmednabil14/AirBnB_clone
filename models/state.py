#!/usr/bin/python3
"""
This module defines a State class that handles state attributes.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
  Represents a state in the system.

  Attributes
  ----------
  name : str
      The name of the state.
  """
    name = ""
