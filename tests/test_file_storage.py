#!/usr/bin/python3
"""Tests `FileStorage` Class
"""

import os
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def SetUp(self):
        """Sets up the objects to test
        """
        self.test_storage = FileStorage()
        self.test_object1 = BaseModel()
        self.test_object2 = BaseModel()

    def test_all(self):
        """Tests the `all()` method
        """
        self.assertTrue(not self.test_storage.all())
        self.test_storage.new(self.test_object1)
        self.assertTrue(self.test_storage.all())

    def test_new(self):
        """Test the `new()` method
        """
        test_key = "{}.{}".format(BaseModel.__name__, self.test_object2.id)
        self.test_storage.new(self.test_object2)
        self.assertTrue(test_key in list(self.test_storage.__objects.keys()))
        self.assertEqual(
                    self.test_storage.__objects[test_key],
                    self.test_object2
                )

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
            storage.save()

            mock_open.assert_called_once_with(
                        storage.__file_path,
                        'w',
                        encoding="utf-8"
                    )
            mock_file.write.assert_called_once()

    def test_reload(self):
        """Tests the `reload()` method
        """
        storage = FileStorage()
        test_object = BaseModel(
                    id='1',
                    created_at=datetime.fromisoformat("2021-02-11T16:15:10.1"),
                    updated_at=datetime.now()
                )

        if os.path.exists(self.test_storage.__file_path):
            os.remove(self.test_storage.__file_path)

        storage.reload()
        self.assertTrue(not storage.all())

        storage.new(test_object)
        storage.save()
        self.assertTrue(storage.all())


if __name__ == '__main__':
    unittest.main()
