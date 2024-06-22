#!/usr/bin/python3
"""Defines Test Cases for `User` Class
"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Tests User class
    """

    def test_attributes(self):
        """Tests `User` attributes
        """
        test_object = User()
        self.assertTrue(hasattr(test_object, "email"))
        self.assertTrue(hasattr(test_object, "password"))
        self.assertTrue(hasattr(test_object, "first_name"))
        self.assertTrue(hasattr(test_object, "last_name"))


if __name__ == "__main__":
    unittest.main()
