#!/usr/bin/python3
"""
test State
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    test State
    """

    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
