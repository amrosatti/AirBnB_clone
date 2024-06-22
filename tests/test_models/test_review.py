#!/usr/bin/python3
"""Defines Test Cases for `Review` Class
"""

from models import storage
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """Review Class Unittest Test Cases
    """

    __attributes = {"place_id": str, "user_id": str, "text": str}
    """dict: Review public class attributes
    """

    def test_init(self):
        """Tests `Review` instantiation
        """
        test_object = Review()

        self.assertEqual(
                    str(type(test_object)),
                    "<class 'models.review.Review'>"
                )
        self.assertIsInstance(test_object, Review)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_attributes(self):
        """Tests `Review` attributes
        """
        test_object = Review()

        for attr, a_type in self.__attributes.items():
            self.assertTrue(hasattr(test_object, attr))
            self.assertEqual(type(getattr(test_object, attr, None)), a_type)


if __name__ == "__main__":
    unittest.main()
