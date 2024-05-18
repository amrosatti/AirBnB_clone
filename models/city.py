#!/usr/bin/python3
""" Module documentation of the subclass City """
from base_model import BaseModel


class City(BaseModel):
    """ A class city that contains name and state_id """

    state_id: str = ""
    name: str = ""
