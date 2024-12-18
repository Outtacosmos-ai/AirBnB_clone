#!/usr/bin/python3
""" this module conatins FileStorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class_mapping = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class FileStorage():
    """ This serializes instances to a JSON file """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return all objects """
        return FileStorage.__objects

    def new(self, obj):
        """ create new object """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ save objects into file.json """
        formatted_dictionary = {}
        for key, obj in FileStorage.__objects.items():
            formatted_dictionary[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as fileJSON:
            json.dump(formatted_dictionary, fileJSON)

    def reload(self):
        """
        loads from file.json into objects
        FileStorage.__objects.clear()
        """
        try:
            new__objects = {}
            with open(FileStorage.__file_path, "r") as fileJSON:
                new__objects = json.load(fileJSON)
                for obj in new__objects.values():
                    class_name = obj["__class__"]
                    if class_name in class_mapping:
                        self.new(class_mapping[class_name](**obj))
        except Exception:
            pass
