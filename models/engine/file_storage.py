#!/usr/bin/python3
"""Defines `FileStorage` Class
"""

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
                obj (:obj:BaseModel): object
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes `__objects` to the JSON file
        """
        objects_dict = {}
        for k, v in self.__objects:
            objects_dict[k] = v.to_dict()

        with open(self.__filepath, 'w', encoding="utf-8") as f:
            f.write(json.dumps(self.objects_dict))

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        if not exist(self.__file_path):
            return

        with open(self.__file_path, 'r', encoding="utf-8") as f:
            self.__objects = json.loads(f.read())
