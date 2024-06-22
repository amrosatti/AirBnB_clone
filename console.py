#!/usr/bin/python3
"""Defines a command interpter
"""

import cmd
import re
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpeter from the cmd class
    """

    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Creates a new instance
        """
        if len(args) == 0:
            print('** class name missing **')
            return
        if args != 'BaseModel':
            print('** class doesn\'t exist **')
            return

        obj = BaseModel()
        storage.save()
        print(obj.id)

    def help_create(self):
        """Documents the `create` command
        """
        print('Creates a new instance of (BaseModel),\
                saves it to the JSON file and prints the (id).\
                `usage: create <class name>`')

    def do_show(self, args):
        """Prints the instance
        """
        args = args.split()
        length = len(args)

        objects = storage.all()
        if length > 1:
            key = "BaseModel.{}".format(args[1])

        if length == 0:
            print('** class name missing **')
            return
        if 'BaseModel' not in args:
            print('** class doesn\'t exist **')
            return
        if args[0] == 'BaseModel' and length == 1:
            print('** instance id missing **')
            return

        try:
            print(objects[key])
        except KeyError:
            print('** no instance found **')
            return

    def help_show(self):
        """Documents the `show` command
        """
        print('Prints the string representation of an instance,\
                based on the class name and (id).\
                `usage: show <class name> <id>`')

    def do_destroy(self, args):
        """Delets an instance
        """
        args = args.split()
        length = len(args)

        objects = storage.all()
        if length > 1:
            key = "BaseModel.{}".format(args[1])

        if length == 0:
            print('** class name missing **')
            return
        if 'BaseModel' not in args:
            print('** class doesn\'t exist **')
            return
        if args[0] == 'BaseModel' and length == 1:
            print('** instance id missing **')
            return

        try:
            del objects[key]
            storage.save()
        except KeyError:
            print('** no instance found **')
            return

    def help_destroy(self):
        """Documents the `destroy` command
        """
        print('Deletes an instance\
                based on the class name and (id).\
                Saves the change into the JSON file.\
                `usage: destroy <class name> <id>`')

    def do_all(self, args):
        """Prints all instances
        """
        if args and args != 'BaseModel':
            print('** class doesn\'t exist **')
            return

        objects = storage.all()
        objects_list = [str(obj) for obj in objects.values()]
        print(objects_list)

    def help_all(self):
        """Documents the `all` command
        """
        print('Prints all string representation of all instances,\
                based or not on the class name.\
                `usage: all [<class name>]`')

    def do_update(self, args):
        """Updates an instance
        """
        args = args.split()
        length = len(args)

        if not length:
            print('** class name missing **')
            return
        if args[0] != 'BaseModel':
            print('** class doesn\'t exist **')
            return
        if length == 1:
            print('** instance id missing **')
            return
        if length == 2:
            print('** attribute name missing **')
            return
        if length == 3:
            print('** value missing **')
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        try:
            setattr(objects[key], args[2], args[3].strip('"'))
            objects[key].save()
        except KeyError:
            print('** no instance found **')
            return

    def help_update(self):
        """Documets the `update` command
        """
        print('Updates an instance based on the class name and (id),\
                by adding or updating attributes.\
                Saves the change into the JSON file.\
                `usage: update <class name> <id> <attribute> "<value>"`')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
