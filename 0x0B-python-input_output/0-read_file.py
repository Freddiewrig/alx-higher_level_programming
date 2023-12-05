#!/usr/bin/python3
"""Define a function that reads a text file"""


def read_file(filename=""):
    """Read and print the contents of a text file to stdout.

    Args:
    - filename (str): The name of the text file to be read.

    Returns:
    None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')