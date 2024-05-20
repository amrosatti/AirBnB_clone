#!/usr/bin/python3
""" A command interpter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpeter from from the cmd class
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exit the program """
        return True

    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
