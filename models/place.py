#!/usr/bin/python3
"""
This module defines a Place class that handles place attributes.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
   Represents a place in the system.

   Attributes
   ----------
   name : str
       The name of the place.
   city_id : str
       The ID of the city that the place is located in.
       This corresponds to City.id.
   user_id : str
       The ID of the user who owns the place. This corresponds to User.id.
   description : str
       A description of the place.
   number_rooms : int
       The number of rooms in the place.
   number_bathrooms : int
       The number of bathrooms in the place.
   max_guest : int
       The maximum number of guests allowed in the place.
   price_by_night : float
       The price per night for staying in the place.
   latitude : float
       The latitude coordinate of the place.
   longitude : float
       The longitude coordinate of the place.
   amenity_ids : list
       A list of IDs of amenities available in the place.
       This corresponds to Amenity.id.
   """
    name = ""
    city_id = ""  # it will be the City.id
    user_id = ""  # it will be the User.id
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id
