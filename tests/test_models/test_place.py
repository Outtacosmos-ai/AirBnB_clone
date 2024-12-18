#!/usr/bin/python3
"""
test Place
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    test Place
    """

    def test_attributes(self):
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])

    def test_inheritance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)


if __name__ == '__main__':
    unittest.main()
