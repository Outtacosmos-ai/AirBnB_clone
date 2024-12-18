#!/usr/bin/python3
"""
test City
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    test City
    """

    def test_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
