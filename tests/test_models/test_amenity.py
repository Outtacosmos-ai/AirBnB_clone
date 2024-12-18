#!/usr/bin/python3
"""
test Amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    test Amenity
    """

    def test_attributes(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
