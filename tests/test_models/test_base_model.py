#!/usr/bin/python3
"""
Tests for BaseModel
"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests for BaseModel
    """

    def setUp(self):
        """
        Test setUp
        """
        self.base_model = BaseModel()
        self.base_model.name = "Dennis McField"

    def test_model(self):
        self.assertEqual(self.base_model.name, "Dennis McField")

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(uuid.UUID(self.base_model.id), uuid.UUID)

    def test_created_at(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertIn('id', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_str_representation(self):
        expected_str = (
            f"[BaseModel] ({self.base_model.id}) "
            f"{self.base_model.__dict__}"
        )
        self.assertEqual(str(self.base_model), expected_str)

    def test_init_with_kwargs(self):
        data = {
            "id": "123",
            "created_at": "2022-01-01T00:00:00",
            "updated_at": "2022-01-01T00:00:00",
            "name": "Test"
        }
        base_model = BaseModel(**data)
        self.assertEqual(base_model.id, "123")
        self.assertEqual(
                base_model.created_at.isoformat(),
                "2022-01-01T00:00:00"
                )
        self.assertEqual(
                base_model.updated_at.isoformat(), "2022-01-01T00:00:00"
                )
        self.assertEqual(base_model.name, "Test")

    def test_to_dict2(self):
        expected_dict = {
            'id': self.base_model.id,
            '__class__': 'BaseModel',
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat(),
            'name': 'Dennis McField'
        }
        self.assertDictEqual(self.base_model.to_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
