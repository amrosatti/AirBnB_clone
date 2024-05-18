#!/usr/bin/python3
""" A module of the class Amenity that inherites from the
BaseModel """
from base_model import BaseModel


class Amenity(BaseModel):
    """ A classs called amenity which inherites from BaseModel
    with an attribute name """
    name: str = ""
