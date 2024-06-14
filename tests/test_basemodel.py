#!/usr/bin/python3

"""Unittest for `BaseModel` Class
"""

from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest
import re

<<<<<<< HEAD

=======
>>>>>>> fileStorage_engine
class TestBaseModel(unittest.TestCase):
    """Tests `BaseModel` Class
    """

    def setUp(self):
        """Instantiates a `BaseModel` Object
        """
        self.test_id = str(uuid4())
        self.test_createdat = datetime(
                2024, 1, 1,
                00, 00, 00, 00).isoformat()
        self.test_updatedat = datetime.now().isoformat()
        self.test_obj1 = BaseModel()
        self.test_obj2 = BaseModel(
                    id=self.test_id, created_at=self.test_createdat,
                    updated_at=self.test_updatedat, something='something_else'
                )

    def test_init(self):
        """Tests the initialization of instances
        """
<<<<<<< HEAD
=======
        self.assertTrue('id' in dir(self.test_obj1))
        self.assertTrue('created_at' in dir(self.test_obj1))
        self.assertTrue('updated_at' in dir(self.test_obj1))

    def test_init_kwargs(self):
        """Valid kwargs
        """
        self.assertTrue('id' in dir(self.test_obj2))
        self.assertTrue('created_at' in dir(self.test_obj2))
        self.assertTrue('updated_at' in dir(self.test_obj2))
        self.assertTrue('something' in dir(self.test_obj2))

    def test_attributes_id(self):
        """Tests the instance attribute `id`
        """
        self.assertTrue(isinstance(self.test_obj1.id, str))
        self.assertTrue(isinstance(self.test_obj2.id, str))

    def test_attributes_created_at(self):
        """Tests `created_at` attribute
        """
        self.assertTrue(isinstance(self.test_obj1.created_at, datetime))
        self.assertTrue(isinstance(self.test_obj2.created_at, datetime))
        self.assertEqual(
                    self.test_obj2.created_at,
                    datetime.fromisoformat('2024-01-01T00:00:00')
                )

    def test_attributes_updated_at(self):
        """Tests `updated_at` attribute
        """
        self.assertTrue(isinstance(self.test_obj1.updated_at, datetime))
        self.assertTrue(isinstance(self.test_obj2.updated_at, datetime))
        self.assertEqual(self.test_obj1.created_at, self.test_obj1.updated_at)

    def test_save(self):
        """Tests `save()` instance method
        """
        test_update1 = self.test_obj1.updated_at
        test_update2 = self.test_obj2.updated_at
        self.test_obj1.save()
        self.test_obj2.save()
        self.assertTrue(test_update1 != self.test_obj1.updated_at)
        self.assertTrue(test_update2 != self.test_obj2.updated_at)

    def test_to_dict(self):
        """Tests `to_dict()` instance method
        """
        self.assertTrue(isinstance(self.test_obj1.to_dict(), dict))
        self.assertTrue(isinstance(self.test_obj2.to_dict(), dict))
        for k in list(self.test_obj1.to_dict().keys()):
            if k != '__class__':
                self.assertTrue(k in list(self.test_obj1.__dict__.keys()))

        for k in list(self.test_obj2.to_dict().keys()):
            if k != '__class__':
                self.assertTrue(k in list(self.test_obj2.__dict__.keys()))

        self.assertTrue('__class__' in list(self.test_obj1.to_dict().keys()))
        self.assertTrue('__class__' in list(self.test_obj2.to_dict().keys()))
        self.assertEqual(
                BaseModel.__name__,
                self.test_obj1.to_dict()['__class__']
                )
        self.assertEqual(
                BaseModel.__name__,
                self.test_obj2.to_dict()['__class__']
                )

    def test_to_dict_dates(self):
        """Tests the dates in instance
        """
        dt_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.?\d*'
        self.assertTrue(isinstance(
            self.test_obj1.to_dict()['created_at'],
            str
            ))
        self.assertEqual(
                    re.findall(
                            dt_pattern,
                            self.test_obj1.to_dict()['created_at']
                        ),
                    [self.test_obj1.to_dict()['created_at']]
                )
        self.assertTrue(isinstance(
            self.test_obj1.to_dict()['updated_at'],
            str
            ))
        self.assertEqual(
                    re.findall(
                            dt_pattern,
                            self.test_obj1.to_dict()['updated_at']
                        ),
                    [self.test_obj1.to_dict()['updated_at']]
                )
        self.assertTrue(isinstance(
            self.test_obj2.to_dict()['created_at'],
            str
            ))
        self.assertEqual(
                    re.findall(
                            dt_pattern,
                            self.test_obj2.to_dict()['created_at']
                        ),
                    [self.test_obj2.to_dict()['created_at']]
                )
        self.assertTrue(isinstance(
            self.test_obj2.to_dict()['updated_at'],
            str
            ))
        self.assertEqual(
                    re.findall(
                            dt_pattern,
                            self.test_obj2.to_dict()['updated_at']
                        ),
                    [self.test_obj2.to_dict()['updated_at']]
                )


if __name__ == '__main__':
    unittest.main()
