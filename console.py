#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help message for the EOF command."""
        print("EOF signal to exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()