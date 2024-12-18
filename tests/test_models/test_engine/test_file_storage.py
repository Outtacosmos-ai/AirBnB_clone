#!/usr/bin/python3
"""
Tests for FileStorage Class
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases FileStorage"""

    def setUp(self):
        """Set up"""
        self.storage = FileStorage()
        setattr(FileStorage, "_FileStorage__objects", {})

    def tearDown(self):
        """Clean up"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + obj.id, all_objs)

    def test_reload_empty_file(self):
        """Test reload empty file"""
        open(FileStorage._FileStorage__file_path, "w").close()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 0)


if __name__ == "__main__":
    unittest.main()
