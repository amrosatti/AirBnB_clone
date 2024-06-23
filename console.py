#!/usr/bin/python3
"""Defines a command interpter
"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpeter from the cmd class
    """

    prompt = '(hbnb) '
    classes = [
                'BaseModel', 'User', 'Place', 'State',
                'City', 'Amenity', 'Review'
            ]

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
        if args not in self.classes:
            print('** class doesn\'t exist **')
            return

        obj = eval(args)()
        storage.save()
        print(obj.id)

    def help_create(self):
        """Documents the `create` command
        """
        print('Creates a new instance of (BaseModel),\n\
                saves it to the JSON file and prints the (id).\n\
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
        if args[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        if length == 1:
            print('** instance id missing **')
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])

        try:
            print(objects[key])
        except KeyError:
            print('** no instance found **')
            return

    def help_show(self):
        """Documents the `show` command
        """
        print('Prints the string representation of an instance,\n\
                based on the class name and (id).\n\
                `usage: show <class name> <id>`')

    def do_destroy(self, args):
        """Delets an instance
        """
        args = args.split()
        length = len(args)

        if length == 0:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        if length == 1:
            print('** instance id missing **')
            return

        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])

        try:
            del objects[key]
            storage.save()
        except KeyError:
            print('** no instance found **')
            return

    def help_destroy(self):
        """Documents the `destroy` command
        """
        print('Deletes an instance\n\
                based on the class name and (id).\n\
                Saves the change into the JSON file.\n\
                `usage: destroy <class name> <id>`')

    def do_all(self, args):
        """Prints all instances
        """
        arg = args
        if arg and arg not in self.classes:
            print('** class doesn\'t exist **')
            return

        objects = storage.all()
        objects_list = []

        if arg:
            for obj in objects.values():
                if arg == type(obj).__name__:
                    objects_list.append(str(obj))
        else:
            objects_list = [str(obj) for obj in objects.values()]

        print(objects_list)

    def help_all(self):
        """Documents the `all` command
        """
        print('Prints all string representation of all instances,\n\
                based or not on the class name.\n\
                `usage: all [<class name>]`')

    def do_update(self, args):
        """Updates an instance
        """
        args = args.split()
        length = len(args)

        if not length:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
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
        print('Updates an instance based on the class name and (id),\n\
                by adding or updating attributes.\n\
                Saves the change into the JSON file.\n\
                `usage: update <class name> <id> <attribute> "<value>"`')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
