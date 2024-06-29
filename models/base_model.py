#!/usr/bin/python3
"""Defines BaseModel Class
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel Class
    """

    def __init__(self, **kwargs):
        """Constructor

        Args:
            kwargs (:obj:dict): Arguments dictionary
                                (given if constructing by a dict)
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            return

        for key, value in kwargs.items():
            if key == '__class__':
                continue
            if key in ["created_at", "updated_at"]:
                setattr(self, key, datetime.fromisoformat(value))
                continue
            setattr(self, key, value)

    def save(self):
        """Updates 'updated_at' attribute
        """
        setattr(self, 'updated_at', datetime.now())
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing '__dict__' adding class name
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__

        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict

    def __str__(self):
        """Instance string representation
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id, self.__dict__
            )
