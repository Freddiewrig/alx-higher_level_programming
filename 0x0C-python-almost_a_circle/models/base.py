#!/usr/bin/python3
"""Define class base"""


import json
import sys
import csv
import turtle

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
    
    def create(cls, **dictionary):
        """return an instance with attribbutes set"""
        if cls.__name__ == "Rectangle":
            dummy_rec = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_rec = cls(1)
        dummy_rec.update(**dictionary)
        return dummy_rec
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                json_list = json.loads(json_string)
                return [cls.create(**obj) for obj in json_list]
        except FileNotFoundError:
            return[]
        
    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r', newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                return [cls.create(*map(int, row)) for row in csv_reader]
        except FileNotFoundError:
            return []
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.speed(2)

        def draw_shape(shape, color, x, y, width, height):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()

            for _ in range(4):
                turtle.forward(width if shape == "Rectangle" else width)
                turtle.left(90)

            turtle.end_fill()

        for rect in list_rectangles:
            draw_shape("Rectangle", "blue", rect.x, rect.y, rect.width, rect.height)

        for square in list_squares:
            draw_shape("Square", "red", square.x, square.y, square.size, square.size)

        turtle.exitonclick()