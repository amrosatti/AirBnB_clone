#!/usr/bin/python3
""" A module documentation for a subclass Review """
from base_model import BaseModel


class Review(BaseModel):
    """ A class Review inheriting from BaseModel class """
    
    place_id: str = ""
    user_id: str = ""
    text: str = ""
