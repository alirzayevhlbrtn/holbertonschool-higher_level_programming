#!/usr/bin/python3
"""
Student to json
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            res = {}
            for att in attrs:
                if att in self.__dict__:
                    res[att] = self.__dict__[att]
            return res

    def reload_from_json(self, json):
        if json:
            for key in self.__dict__.keys():
                self.__dict__[key] = json[key]
