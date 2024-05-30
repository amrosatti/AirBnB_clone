#!/usr/bin/python3
"""Defines `FileStorage` Class
"""

from models.base_model import BaseModel
from os.path import getsize
import json


class FileStorage:
    """Serializes/deserializes JSON file to instance and vice versa
    """

    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """Retrieves all stored objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in `__objects` the `obj` with key `<obj class name>.id`

            Args:
                obj (:obj:BaseModel): object to be added in the dictionary
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes `__objects` to the JSON file
        """
        objects_todict = {}
        for k, v in self.__objects.items():
            objects_todict[k] = v.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(objects_todict))

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        try:
            if getsize(self.__file_path) != 0:
                with open(self.__file_path, 'r') as f:
                    json_string = f.read()
                    json_objects = json.loads(json_string)
        except FileNotFoundError:
            return

        for k, v in json_objects.items():
            self.__objects[k] = BaseModel(**v)
