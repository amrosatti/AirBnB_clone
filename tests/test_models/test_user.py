#!/usr/bin/python3
"""Defines Test Cases for `User` Class
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """User Class Unittest Test Cases
    """

    __attributes = {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            }
    """dict: User attributes dictinary
    """

    def test_init(self):
        """Tests `User` instantiation
        """
        test_object = User()

        self.assertEqual(str(type(test_object)), "<class 'models.user.User'>")
        self.assertIsInstance(test_object, User)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_attributes(self):
        """Tests `User` attributes
        """
        test_object = User()

        for attr, a_type in self.__attributes.items():
            self.assertTrue(hasattr(test_object, attr))
            self.assertEqual(type(getattr(test_object, attr, None)), a_type)


if __name__ == "__main__":
    unittest.main()
