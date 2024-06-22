#!/usr/bin/python3
"""Defines Test Cases for `Amenity` Class
"""

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Amenity Class Unittest Test Cases
    """

    __attributes = ("name", str)
    """tuple: Amenity public class attributes
    """


    def test_init(self):
        """Tests `Amenity` instantiation
        """
        test_object = Amenity()

        self.assertEqual(
                    str(type(test_object)),
                    "<class 'models.amenity.Amenity'>"
                )
        self.assertIsInstance(test_object, Amenity)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_attributes(self):
        """Tests `Amenity` attributes
        """
        test_object = Amenity()

        attr, a_type = self.__attributes
        self.assertTrue(hasattr(test_object, attr))
        self.assertEqual(type(getattr(test_object, attr, None)), a_type)


if __name__ == "__main__":
    unittest.main()
