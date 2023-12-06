#!/usr/bin/python3
"""import json to create a obj file"""
import json
def load_from_json_file(filename):
    """
    create an object from a json file
    Args:
        filename: name of the text file
    Return:
        file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)