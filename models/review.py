#!/usr/bin/python3
"""Defines the `Review` Class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inheriting from BaseModel class
    """

    place_id = ""
    user_id = ""
    text = ""
