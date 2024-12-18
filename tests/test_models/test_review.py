#!/usr/bin/python3
"""
test review
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    test Review
    """

    def test_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_inheritance(self):
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == '__main__':
    unittest.main()
