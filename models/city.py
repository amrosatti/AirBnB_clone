#!/usr/bin/python3
"""Defines the `City` Class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City inheriting from BaseModel class
    """

    state_id = ""
    name = ""
