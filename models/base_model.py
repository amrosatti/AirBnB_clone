#!/usr/bin/python3

"""Defines BaseModel Class
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel Class"""

    def __init__(self, **kwargs):
        """Constructor

        Args:
            args (:obj:tuble): Not used
            kwargs (:obj:dict): Arguments dictionary
        """
        if kwargs not None:
            for k, v in kwargs:
                if k = '__class__':
                    continue
                if k in ['created_at', 'updated_at']:
                    self.setattr(k, datetime.fromisoformat(v))

                self.setattr(k, v)
                return

            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """Updates 'updated_at' attribute
        """
        self.setattr('updated_at', datetime.now())

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
                type(self).__name__,
                self.id, self.__dict__
            )
