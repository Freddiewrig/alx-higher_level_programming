#!/usr/bin/python3
"""define json function"""
import json
def from_json_string(my_str):
    """
    Return the Python object represented by a JSON string.

    Args:
    - my_str (str): The JSON-formatted string.

    Returns:
    object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)