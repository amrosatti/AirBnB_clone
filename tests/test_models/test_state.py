#!/usr/bin/python3
"""Defines Test Cases for `State` Class
"""

from models import storage
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """State Class Unittest Test Cases
    """

    __attributes = ("name", str)
    """dict: State attributes dictinary
    """

    def test_init(self):
        """Tests `State` instantiation
        """
        test_object = State()

        self.assertEqual(
                    str(type(test_object)),
                    "<class 'models.state.State'>"
                )
        self.assertIsInstance(test_object, State)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_attributes(self):
        """Tests `State` attributes
        """
        test_object = State()

        attr, a_type = self.__attributes
        self.assertTrue(hasattr(test_object, attr))
        self.assertEqual(type(getattr(test_object, attr, None)), a_type)


if __name__ == "__main__":
    unittest.main()
