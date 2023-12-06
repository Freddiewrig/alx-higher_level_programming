#!/usr/bin/python3
"""Define class"""
class Student:
    def __init__(self, first_name, last_name, age):
        """
        defines a student by.
        Args:
            first_name(str): first name.
            last_name(str): last name.
            age(int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Return self dict"""
        return self.__dict__