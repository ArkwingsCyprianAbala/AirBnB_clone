#!/usr/bin/python3
"""

"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Define the HBNB console
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """
        Quit the program
        """
        return True

    def do_create(self, arg):
        """
        create a new instance of Basemodel and save it to the JSON file.
        usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class
        Usage: all [class_name]
        """
        objects = storage.all()
        commands = shlex.split(arg)
        print(f"{commands = }")
        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class name missing **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def default(self, arg):
        """
        Default behaviour for cmd module for invalid system
        """
        arg_list = arg.split('.')
        incoming_class_name = arg_list[0]
        command = arg_list[1].split('(')
        incoming_method = command[0]
        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update
        }
        if incoming_method in method_dict.keys():
            return method_dict[incoming_method]("{} {}".format(incoming_class_name, ''))
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_update(self, arg):
        """
        Update an instance by adding or updating attribute.
        Usage: update <class_name> <id> <attribute_name> <attribute_value>
        """
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr_name = commands[2]
                attr_value = commands[3]
                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_help(self, arg):
        """

        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handle the End-of-File (Ctrl+0) event to exit the program
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
