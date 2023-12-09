#!/usr/bin/python3
"""Define class base"""


import json
import sys

class Base:
    """Init objects and define the new object"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a list of dictionaries"""
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.
        
        Args:
            list_objs: list of instances that inherits from base
        """
        if list_objs == None:
            return []
        filename = f"{cls.__name__}.json"
        json_string = cls.to_json_string(list_objs)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string == None:
            return []
        else:
            return json.loads(json_string)