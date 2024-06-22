#!/usr/bin/python3

"""Unittest for `BaseModel` Class
"""

from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import unittest
import re


class TestBaseModel(unittest.TestCase):
    """Tests `BaseModel` Class
    """

    p = r"[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"
    """str: UUID4 regex pattern

    Raised to the module level for coding style purpose
    """

    def setUp(self):
        """Instantiates a `BaseModel` Object
        """
        self.test_id = str(uuid4())
        self.test_createdat = datetime(2024, 1, 1, 00, 00, 00, 00).isoformat()
        self.test_updatedat = datetime.now().isoformat()
        self.create_time = datetime.now()
        self.test_obj1 = BaseModel()
        self.test_obj2 = BaseModel(**{
                    'id': self.test_id,
                    'created_at': self.test_createdat,
                    'updated_at': self.test_updatedat,
                    'something': 'something_else'
                })
        self.objects = [self.test_obj1, self.test_obj2]

    def test_init(self):
        """Tests the initialization of instances
        """
        '''Empty Arguments'''
        for test_object in self.objects:
            self.assertTrue('id' in dir(test_object))
            self.assertTrue('created_at' in dir(test_object))
            self.assertTrue('updated_at' in dir(test_object))
            if test_object.id == self.test_obj2.id:
                self.assertTrue('something' in dir(test_object))

    def test_attributes(self):
        """Tests the instance attributes
        """
        uuid4_pattern = re.compile(self.p)

        for test_object in self.objects:
            '''id'''
            self.assertTrue(isinstance(test_object.id, str))
            self.assertTrue(uuid4_pattern.match(test_object.id))

            '''created_at'''
            self.assertTrue(isinstance(test_object.created_at, datetime))
            self.assertTrue(isinstance(test_object.created_at, datetime))
            if test_object.created_at == self.test_obj2.created_at:
                self.assertEqual(
                            self.test_obj2.created_at,
                            datetime.fromisoformat('2024-01-01T00:00:00')
                        )

            '''updated_at'''
            self.assertTrue(isinstance(test_object.updated_at, datetime))
            if test_object.updated_at == self.test_obj1.updated_at:
                self.assertEqual(
                        test_object.created_at,
                        test_object.updated_at
                        )

    def test_save(self):
        """Tests `save()` instance method
        """
        for test_object in self.objects:
            old_update = test_object.updated_at
            test_object.save()
            self.assertTrue(old_update != test_object.updated_at)

    def test_to_dict(self):
        """Tests `to_dict()` instance method
        """
        pattern = r"\d{4}-[01]\d-[0-3]\dT[0-2]\d:[0-5]\d:[0-5]\d"
        iso_pattern = re.compile(pattern)
        cls = '__class__'

        for test_object in self.objects:
            self.assertTrue(isinstance(test_object.to_dict(), dict))

            for k in list(test_object.to_dict().keys()):
                if k != cls:
                    self.assertTrue(k in list(test_object.__dict__.keys()))

            self.assertTrue(cls in list(test_object.to_dict().keys()))
            self.assertEqual(BaseModel.__name__, test_object.to_dict()[cls])

            for i in ['created_at', 'updated_at']:
                self.assertTrue(isinstance(test_object.to_dict()[i], str))
                self.assertTrue(iso_pattern.match(test_object.to_dict()[i]))

    def test_str(self):
        """Tests the value of the string representation of the object
        """
        pattern = r"\[BaseModel\] \(%s\) \{.+\}" % self.p
        str_pattern = re.compile(pattern)

        for test_object in self.objects:
            self.assertTrue(str_pattern.match(str(test_object)))


if __name__ == '__main__':
    unittest.main()
