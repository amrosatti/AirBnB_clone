#!/usr/bin/python3
"""Defines `FileStorage` Class
"""

import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes/deserializes JSON file to instance and vice versa
    """

    __file_path = "file.json"
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

        with open(self.__file_path, 'w', encoding="utf-8") as json_file:
            json_file.write(json.dumps(objects_todict))

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as json_file:
                json_objects = json.loads(json_file.read())

            for key, obj in json_objects.items():
                self.__objects[key] = eval(obj["__class__"])(**obj)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
