#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    Class of Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON to string
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save JSON file
        """
        if list_objs is None:
            list_dictionary = []
        else:
            list_dictionary = [obj.to_dictionary() for obj in list_objs]

        fname = "{}.json".format(cls.__name__)
        with open(fname, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        """
        From string to json
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create class
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load class
        """
        fname = "{}.json".format(cls.__name__)

        try:
            with open(fname, "r", encoding="utf-8") as f:
                json_string = f.read()
                ls = cls.from_json_string(json_string)
                inst = []
                for i in ls:
                    ins = cls.create(**i)
                    inst.append(ins)
                return inst
        except IOError:
            return []
