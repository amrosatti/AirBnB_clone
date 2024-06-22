#!/usr/bin/python3
"""Defines Test Cases for `Place` Class
"""

from models import storage
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """Place Class Unittest Test Cases
    """

    __attributes = {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathrooms": int,
                "price_by_night": int,
                "latitude": float,
                "longitude": float,
                "amenity_ids": list
            }
    """dict: Place attributes dictinary
    """

    def test_init(self):
        """Tests `Place` instantiation
        """
        test_object = Place()

        self.assertEqual(
                    str(type(test_object)),
                    "<class 'models.place.Place'>"
                )
        self.assertIsInstance(test_object, Place)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_attributes(self):
        """Tests `Place` attributes
        """
        test_object = Place()

        for attr, a_type in self.__attributes.items():
            self.assertTrue(hasattr(test_object, attr))
            self.assertEqual(type(getattr(test_object, attr, None)), a_type)


if __name__ == "__main__":
    unittest.main()
