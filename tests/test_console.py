#!/usr/bin/python3
""" teste file for console.py """
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
import models
import console
import os
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    console = console.HBNBCommand()

    def test_help(self):
        """test if help works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        output = "EOF  all  count  create  destroy  help  quit  show  update"
        self.assertTrue(output in f.getvalue())

    def test_create(self):
        """test if create works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_quit(self):
        """test if quit works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertTrue(f.getvalue() == "")

    def test_show(self):
        """test if show works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertTrue(f.getvalue() == "** class name missing **\n")

    def test_destroy(self):
        """test if destroy works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertTrue(f.getvalue() == "** class name missing **\n")

    def test_count(self):
        """test if count works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            self.assertEqual(f.getvalue(), "0\n")

    def test_update(self):
        """test if update works right"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertTrue(f.getvalue() == "** class name missing **\n")

    def test_emptyline(self):
        """test if an empty line is handled properly"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertTrue(f.getvalue() == "")

    def test_destroy_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as _:
            obj = models.storage.all()[f"BaseModel.{test_id}"]
            command = f"destroy BaseModel {test_id}"
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, models.storage.all())

    def test_destroy_objects_dot_notation(self):

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as _:
            obj = models.storage.all()[f"BaseModel.{test_id}"]
            command = f"BaseModel.destroy({test_id})"
            HBNBCommand().onecmd(command)
            self.assertNotIn(obj, models.storage.all())

    def test_destroy_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_dot_notatiion(self):
        correct = ""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {object_id}")
            self.assertIn(object_id, f.getvalue().strip())

    def test_create_object(self):

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            test_key = f"BaseModel.{f.getvalue().strip()}"
            self.assertIn(test_key, models.storage.all().keys())

    def test_show_missing_class(self):
        """Test behavior when class name is missing."""
        expected_output = "** class name missing **"

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(expected_output, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(".show()"))
            self.assertNotEqual(expected_output, output.getvalue().strip())

    def test_show_invalid_class(self):
        """Test behavior when class doesn't exist."""
        expected_output = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        """Test behavior when instance id is missing (space notation)."""
        expected_output = "** instance id missing **"
        model_classes = ["BaseModel", "User", "State",
                         "City", "Amenity", "Place", "Review"]

        for model_class in model_classes:
            with patch("sys.stdout", new=StringIO()) as output:
                self.assertFalse(HBNBCommand().onecmd(f"show {model_class}"))
                self.assertEqual(expected_output, output.getvalue().strip())

    def test_show_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(f"BaseModel.show({object_id})")
            self.assertIn(object_id, f.getvalue().strip())

    def test_update_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd(
                    f"update BaseModel {object_id} name 'new_name'"
                    )
            self.console.onecmd(f"show BaseModel {object_id}")
            self.assertIn("new_name", f.getvalue().strip())

    def test_update_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            cmnd = f"BaseModel.update(\"{object_id}\", \"name\", \"new_name\")"
            self.console.onecmd(cmnd)
            self.console.onecmd(f"BaseModel.show({object_id})")
            self.assertIn("new_name", f.getvalue().strip())
            HBNBCommand().onecmd("destroy BaseModel f{object_id}")

    def test_update_id_missing_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            cmnd = "update BaseModel name \"new_name\""
            self.console.onecmd(cmnd)
            self.assertEqual("** no instance found **", f.getvalue().strip())
            HBNBCommand().onecmd("destroy BaseModel f{object_id}")

    def test_update_class_missing_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            cmnd = f"update {object_id} name \"new_name\""
            self.console.onecmd(cmnd)
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())
            HBNBCommand().onecmd("destroy BaseModel f{object_id}")

    def test_update_attribute_value_missing_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            cmnd = f"update BaseModel {object_id} \"new_name\""
            self.console.onecmd(cmnd)
            self.assertEqual("** value missing **", f.getvalue().strip())
            HBNBCommand().onecmd("destroy BaseModel f{object_id}")

    def test_update_attribute_missing_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            cmnd = f"update BaseModel {object_id}"
            self.console.onecmd(cmnd)
            output = "** attribute name missing **"
            self.assertEqual(output, f.getvalue().strip())
            HBNBCommand().onecmd("destroy BaseModel f{object_id}")

    def test_update_instance_not_found_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")

        with patch("sys.stdout", new=StringIO()) as f:
            cmnd = "update BaseModel ffl45ge5w555w name \"value\""
            self.console.onecmd(cmnd)
            output = "** no instance found **"
            self.assertEqual(output, f.getvalue().strip())
            HBNBCommand().onecmd("destroy BaseModel f{object_id}")

    def test_update_class_not_found_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            object_id = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            cmnd = f"update home {object_id} name \"value\""
            self.console.onecmd(cmnd)
            output = "** class doesn't exist **"
            self.assertEqual(output, f.getvalue().strip())
            HBNBCommand().onecmd("destroy BaseModel f{object_id}")

    def test_count_class_dont_exist(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("count country")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())


class TestHBNBCommand_count(unittest.TestCase):
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_base_model(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())

    def test_count_user(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())

    def test_count_state(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())

    def test_count_place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())

    def test_count_city(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())

    def test_count_amenity(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())

    def test_count_review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
