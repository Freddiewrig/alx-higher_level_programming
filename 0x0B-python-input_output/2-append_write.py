#!/usr/bin/python3
"""Def function to append text"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8).
    
    Args:
        filename(str): name of the text file
        text(str): string to be appended.
    Returns:
        (int)numer of text added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
        return count