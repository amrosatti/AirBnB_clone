#!/usr/bin/python3
"""Tests `FileStorage` Class
"""

import models
import os
import unittest
from unittest.mock import patch
from unittest.mock import Mock
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Sets up the objects to test
        """
        self.test_storage = FileStorage()
        self.test_object1 = BaseModel()
        self.test_object2 = BaseModel()
        self.test_storage._FileStorage__objects.clear()

    def test_all(self):
        """Tests the `all()` method
        """
        self.assertEqual(self.test_storage.all(), {})
        self.test_storage.new(self.test_object1)
        self.assertTrue(self.test_object1 in self.test_storage.all().values())

    def test_new(self):
        """Test the `new()` method
        """
        objects = self.test_storage._FileStorage__objects
        test_key = "{}.{}".format(BaseModel.__name__, self.test_object2.id)
        self.test_storage.new(self.test_object2)

        self.assertTrue(test_key in objects.keys())
        self.assertEqual(objects[test_key], self.test_object2)

    def test_save(self):
        """Tests the `save()` method

        Using `unittest.mock` to test the openning and writing operations,
        without actually creating or modifiying files.
        """
        with patch('builtins.open') as mock_open:
            mock_file = mock_open.return_value
            mock_file.write.return_value = None

            storage = FileStorage()
            test_obj = BaseModel()
            storage.new(test_obj)

            save_mock = Mock(side_effect=storage.save())
            save_mock()

            save_mock.assert_called_once()
            mock_open.assert_called_once_with(
                        storage._FileStorage__file_path,
                        'w',
                        encoding="utf-8"
                    )

    def test_reload(self):
        """Tests the `reload()` method
        """
        file_path = storage._FileStorage__file_path
        test_storage = FileStorage()

        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass

        with open(file_path, "w", encoding="utf-8") as file_w:
            file_w.write("{}")

        with open(file_path, "r", encoding="utf-8") as file_r:
            self.assertEqual(file_r.read(), "{}")

        self.assertIs(test_storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
