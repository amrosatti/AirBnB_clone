#!/usr/bin/python3
"""Defines Test Cases for `City` Class
"""

from models import storage
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """City Class Unittest Test Cases
    """

    __attributes = {"state_id": str, "name": str}
    """dict: City attributes dictinary
    """

    def test_init(self):
        """Tests `City` instantiation
        """
        test_object = City()

        self.assertEqual(
                    str(type(test_object)),
                    "<class 'models.city.City'>"
                )
        self.assertIsInstance(test_object, City)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_attributes(self):
        """Tests `City` attributes
        """
        test_object = City()

        for attr, a_type in self.__attributes.items():
            self.assertTrue(hasattr(test_object, attr))
            self.assertEqual(type(getattr(test_object, attr, None)), a_type)


if __name__ == "__main__":
    unittest.main()
