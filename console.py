#!/usr/bin/python3
"""Defines a command interpter
"""

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpeter from from the cmd class
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
