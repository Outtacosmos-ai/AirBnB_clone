#!/usr/bin/python3
""" contains the entry point of the command interpreter """
import cmd
import json
import models
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


class HBNBCommand(cmd.Cmd):
    """using python command line Cmd"""
    prompt = "(hbnb) "

    def do_create(self, line):
        """create Model"""
        if line:
            try:
                create_instance = class_mapping[line]()
                create_instance.save()
                print(create_instance.id)
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """show Model id"""
        if not line:
            print("** class name missing **")
            return
        arg = line.split()
        if arg[0] not in class_mapping:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            if arg[0] in class_mapping:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
            return
        try:
            key = ("{}.{}".format(arg[0], arg[1]))
            loaded_objects = models.storage.all()
            loaded_instance = loaded_objects[key]
            print(loaded_instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """destroy Model id"""
        arg = line.split()
        length = len(arg)

        try:
            key = ("{}.{}".format(arg[0], arg[1]))
            objs = models.storage.all()
            try:
                del objs[key]
                models.storage.save()
            except KeyError:
                if arg[0] not in class_mapping:
                    print("** class doesn't exist **")
                else:
                    print("** no instance found **")
        except IndexError:
            if length == 0:
                print("** class name missing **")
            elif arg[0] not in class_mapping:
                print("** class doesn't exist **")
            elif length == 1:
                print("** instance id missing **")

    def do_all(self, line):
        """all Model"""
        dictio = models.storage.all()
        lista_all = []
        lista_class = []
        for value in dictio.values():
            lista_all.append(str(value))
        if line:
            if line in class_mapping:
                for item in lista_all:
                    if line in item:
                        lista_class.append(item)
                print(lista_class)
            else:
                print("** class doesn't exist **")
        else:
            print(lista_all)

    def do_count(self, line):
        """all Model"""
        dictio = models.storage.all()
        lista_all = []
        lista_class = []
        count_ = 0
        for value in dictio.values():
            count_ += 1
            lista_all.append(str(value))
        if line:
            count_ = 0
            if line in class_mapping:
                for item in lista_all:
                    if line in item:
                        lista_class.append(item)
                        count_ += 1
                print(count_)
            else:
                print("** class doesn't exist **")
        else:
            print(count_)

    def do_update(self, line):
        """update object attributes"""
        comand = line.split()
        ln = len(comand)
        if ln > 4:
            comand = comand[:4]
        try:
            key = "{}.{}".format(comand[0], comand[1])
            try:
                instance = models.storage.all()[key]
                comand[3] = comand[3].strip('"')
                setattr(instance, comand[2], comand[3])
                models.storage.save()
            # except KeyError:
            #     print("** no instance found **")
            except KeyError:
                if comand[0] in class_mapping:
                    print("** no instance found **")
                else:
                    print("** class doesn't exist **")
        except IndexError:
            if ln == 0:
                print("** class name missing **")
            elif ln >= 1 and comand[0] not in class_mapping:
                print("** class doesn't exist **")
            elif ln == 1 and comand[0] in class_mapping:
                print("** instance id missing **")
            elif ln == 2:
                print("** attribute name missing **")
            elif ln == 3:
                print("** value missing **")

    def default(self, line):
        """default command"""
        try:
            list = line[0:-1].split('(')
            if '' in list:
                list.remove('')
            left_list = list[0].split('.')
            function_ = left_list[1]
            class_ = left_list[0]
            if len(list) == 1:
                if function_ == "all":
                    self.do_all(class_)
                if function_ == "count":
                    self.do_count(class_)
            else:
                right_list = list[1].split(',', 1)
                uuid_ = right_list[0].strip('"')
                if function_ == "show":
                    self.do_show(f"{class_} {uuid_}")
                if function_ == "destroy":
                    self.do_destroy(f"{class_} {uuid_}")

                if function_ == "update":
                    jsondata_ = right_list[1].replace("'", '"').strip()
                    if '{' not in jsondata_:
                        key, value = jsondata_.split(',')
                        jsondata_ = f"{{{key.strip()}: {value.strip()}}}"
                    argument_dict = json.loads(jsondata_)
                    for key_, value_ in argument_dict.items():
                        if not isinstance(value_, str):
                            str_ = f"{class_} {uuid_} {key_} {str(value_)}"
                            self.do_update(str_)
                        else:
                            str2_ = f"{class_} {uuid_} {key_} \"{value_}\""
                            self.do_update(str2_)
        except Exception:
            pass

    def do_EOF(self, line):
        """Quit program if EOF entered"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit console"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
