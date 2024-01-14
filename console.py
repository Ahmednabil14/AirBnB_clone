#!/usr/bin/python3
""" the entry point of the command interpreter """
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
import json
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """ the class that handel the command interpreter
        inherit from the cmd class
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    do_EOF = do_quit

    def emptyline(self):
        """
        override the empty line function to excute nothing
        if empty line entered
        """
        pass

    def do_create(self, arg):
        """
        function that create a new instance of BaseModel and
        save it's attributes to the json file.
        """
        if arg:
            if arg in globals() and (
                 arg == "BaseModel" or issubclass(eval(arg), BaseModel)):
                new_model = eval(arg)()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id
        """

        try:
            class_name, id = line.split()
        except ValueError:
            class_name = line
            id = None
        if class_name:
            if class_name in globals() and (
                 class_name == "BaseModel" or issubclass(
                     eval(class_name), BaseModel)):
                if id:
                    key = "{}.{}".format(class_name, id)
                    if key in FileStorage.all(self).keys():
                        print(FileStorage.all(self)[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id
        """
        try:
            class_name, id = line.split()
        except ValueError:
            class_name = line
            id = None
        if class_name:
            if class_name in globals() and (
                 class_name == "BaseModel" or issubclass(
                     eval(class_name), BaseModel)):
                if id:
                    key = "{}.{}".format(class_name, id)
                    if key in FileStorage.all(self).keys():
                        del FileStorage.all(self)[key]
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based or
        not on the class name. Ex: $ all BaseModel or $ all
        """
        list_of_instance = []
        if line == "":
            for value in FileStorage.all(self).values():
                list_of_instance.append(value.__str__())
            print(list_of_instance)
        else:
            if line in globals() and (
                line == "BaseModel" or issubclass(
                    eval(line), BaseModel)):
                for key, value in FileStorage.all(self).items():
                    class_name, id = key.split(".")
                    if class_name == line:
                        list_of_instance.append(value.__str__())

                print(list_of_instance)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and
           id by adding or updating attribute

        Args:
            line : the line which user pass
        """

        try:
            args = line.split()
            class_name = args[0]
        except Exception:
            print("** class name missing **")
            return
        try:
            user_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        try:
            attribute_name = args[2]
        except IndexError:
            print("** attribute name missing **")
            return
        try:
            attribute_value = args[3]
        except IndexError:
            print("** value missing **")
            return
        if class_name in globals() and (
                class_name == "BaseModel" or issubclass(
                    eval(class_name), BaseModel)):
            for key in FileStorage.all(self).keys():
                instance_key = key.split(".")
                instance_found = False
                if instance_key[1] == user_id:
                    instance_found = True
                    break
            if instance_found is True:
                instance = FileStorage.all(self)[key]
                value_type = type(instance.__dict__[attribute_name])
                instance.__dict__[attribute_name] = value_type(
                    eval(attribute_value))
                instance.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_count(self, class_name):
        x = 0
        for key in FileStorage.all(self).items():
            if class_name in globals() and (
                    class_name == "BaseModel" or issubclass(
                        eval(class_name), BaseModel)):
                x += 1
        print(x)

    def precmd(self, argument):
        """Executed just before the command line is interpreted."""
        # Using regular expression to match patterns like "Class.method(...)"
        match = re.match(r"([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)\((.*)\)", argument)
        if match:
            class_name, method, other_arguments = match.groups()
            return f"{method} {class_name} {other_arguments}"
        else:
            return argument


if __name__ == '__main__':
    HBNBCommand().cmdloop()