#!/usr/bin/python3
"""Def function to write json"""
import json
def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
    - my_obj: The object to be serialized to JSON.
    - filename (str): The name of the text file.

    Returns:
    None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)