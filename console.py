#!/usr/bin/python3
"""Defines a command interpter
"""

import cmd
import re
import sys
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpeter from the cmd class
    """

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = storage.classes()

    def default(self, line):
        """Catching commands
        """
        self._precmd(line)

    def preloop(self):
        """Prints the prompt if non-interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def _precmd(self, line):
        """Reformat command line for advanced command syntax

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        """
        match_line = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match_line:
            return line

        classname = match_line.group(1)
        command = match_line.group(2)
        args = match_line.group(3)

        match_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_args:
            _id = match_args.group(1)
            params = match_args.group(2)
        else:
            _id = args
            params = False

        attr_val = ""

        if command == 'update' and params:
            match_dict = re.search('^({.*})$', params)
            if match_dict:
                self._update(classname, _id, match_dict.group(1))
                return ""

            match_attr_val = re.search('(?:"([^"]*)")?(?:, (.*))?$', params)
            if match_attr_val:
                attr_val = (match_attr_val.group(1) or "") + " " +\
                        (match_attr_val.group(2) or "")

        command = f"{command} {classname} {_id} {attr_val}"
        self.onecmd(command)
        return command

    def _update(self, classname, _id, params):
        """Updates an instance by dictionary
        """
        params = params.replace("'", '"')
        params_dict: dict = json.loads(params)

        if not classname:
            print('** class name missing **')
            return
        if classname not in self.classes:
            print('** class doesn\'t exist **')
            return
        if not _id:
            print('** instance id missing **')
            return

        objects = storage.all()
        key = "{}.{}".format(classname, _id)

        try:
            attributes = storage.attributes()[classname]
            for attr, val in params_dict.items():
                if attr in attributes:
                    val = attributes[attr](val)
                setattr(objects[key], attr, val)

            objects[key].save()
        except KeyError:
            print('** no instance found **')
            return

    def postcmd(self, stop, line):
        """Prints the prompt if non-interactive mode
        """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')

        return stop

    def do_quit(self, line):
        """Exits the program
        """
        print('Bye..')
        return True

    def do_EOF(self, line):
        """Handles End Of File character to exit the program
        """
        print()
        print('Bye..')
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Creates a new instance
        """
        if not args:
            print('** class name missing **')
            return
        if args not in self.classes:
            print('** class doesn\'t exist **')
            return

        obj = self.classes[args]()
        storage.save()
        print(obj.id)

    def help_create(self):
        """Documents the `create` command
        """
        print('Creates a new instance of a given class')
        print('saves it to the JSON file and prints the id.', end="\n\n")
        print('usage: create <class name>', end="\n\n")

    def do_show(self, args):
        """Prints the instance
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
        print('Prints the string representation of an instance,')
        print('based on the class name and id.', end="\n\n")
        print('usage: show <class name> <id>', end="\n\n")

    def do_destroy(self, args):
        """Delets an instance
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
        print('Deletes an instance')
        print('based on the class name and id.')
        print('Saves the change into the JSON file.', end="\n\n")
        print('usage: destroy <class name> <id>', end="\n\n")

    def do_all(self, args):
        """Prints all instances
        """
        objects = storage.all().values()

        if args:
            if args not in self.classes:
                print('** class doesn\'t exist **')
                return

            objects = [str(obj) for obj in objects
                       if args == type(obj).__name__]
        else:
            objects = [str(obj) for obj in objects]

        print(objects)

    def help_all(self):
        """Documents the `all` command
        """
        print('Prints all string representation of all instances,')
        print('based or not on the class name.', end="\n\n")
        print('usage: all [<class name>]')

    def do_count(self, args):
        """Counts the number of a class instances
        """
        if not args:
            print('** class name missing **')
            return
        if args not in self.classes:
            print('** class doesn\'t exist **')
            return

        objects = storage.all().values()
        objects = [obj for obj in objects if args == type(obj).__name__]

        print(len(objects))

    def help_count(self):
        """Documents the `count` command
        """
        print('Counts the number of instances of a given class.', end="\n\n")
        print('usage: count <class name>', end="\n\n")

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

        attr = args[2]
        value = args[3]

        type_cast = None
        if not re.search('^".*"$', args[3]):
            if '.' in args[3]:
                type_cast = float
            else:
                type_cast = int
        else:
            value = value.replace('"', '')

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print('** no instance found **')
            return

        attributes = storage.attributes()[args[0]]

        if attr in attributes:
            value = attributes[attr](value)
        elif type_cast:
            try:
                value = type_cast(value)
            except ValueError:
                pass

        setattr(objects[key], attr, value)
        objects[key].save()

    def help_update(self):
        """Documets the `update` command
        """
        print('Updates an instance based on the class name and id,')
        print('by adding or updating attributes.')
        print('Saves the change into the JSON file.', end="\n\n")
        print(
                'usage: update <class name> <id> <attribute> "<value>"',
                end="\n\n"
             )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
