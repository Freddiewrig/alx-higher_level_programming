#!/usr/bin/python3
"""Define the function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8).
    
    Args:
        filename: name of file being writen.
        text: text being written.
    Returns: no of charactes written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        num = f.write(text)
        return num