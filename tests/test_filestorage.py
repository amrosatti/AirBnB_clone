#!/usr/bin/python3
"""Tests `FileStorage` Class
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    
    def SetUp(self):
        """Sets up the objects to test
        """
        self.test_storage = FileStorage()
        self.test_obj = BaseModel()


if __name__ == '__main__':
    unittest.main()
