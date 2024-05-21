#!/usr/bin/python3
""" A command interpter """
import cmd
from models.base_model import BaseModel
import json
import os


class HBNBCommand(cmd.Cmd):
    """ Command interpeter from from the cmd class
    """
    prompt = '(hbnb)'
    storage = {}

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to
        the JSON file) and prints the id """

        if not arg:
            print("** class name missing **")
        elif arg == "BaseModel":
            instance = BaseModel()
            instance.save()
            HBNBCommand.storage[instance.id] = instance
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the
        class name and id. """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instance = HBNBCommand.storage.get(instance_id)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name != "BaseModel":
            print("** class doesn't exist **")
            return
        instance = HBNBCommand.storage.get(instance_id)
        if not instance:
            print("** no instance found **")
        else:
            del instance
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
