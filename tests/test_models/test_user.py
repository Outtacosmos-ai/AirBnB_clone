#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """  """

    def setUp(self):
        """ initialization method """
        self.user = User()

        # self.user.age = 26
        # self.user.balance = 125.25
        # self.user.email = "kamal@mail.com"
        # self.user.password = "root"
        # self.user.first_name = "kamal"
        # self.user.last_name = "miftah"

    def test_instance(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_inherited_methods(self):
        self.assertTrue(hasattr(self.user, '__str__'))
        self.assertTrue(hasattr(self.user, 'save'))
        self.assertTrue(hasattr(self.user, 'to_dict'))

    def test_type_atrributes(self):
        l1 = ['email', 'password', 'first_name', 'last_name']
        l2 = [str, str, str, str]
        for att, typ in zip(l1, l2):
            self.assertEqual(typ, type(getattr(self.user, att)))


if __name__ == '__main__':
    unittest.main()
