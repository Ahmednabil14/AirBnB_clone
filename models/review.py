#!/usr/bin/python3
"""
This module defines a Review class that handles review attributes.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
  Represents a review in the system.

  Attributes
  ----------
  place_id : str
      The ID of the place that the review is for. This corresponds to Place.id.
  user_id : str
      The ID of the user who wrote the review. This corresponds to User.id.
  text : str
      The text of the review.
  """
    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
