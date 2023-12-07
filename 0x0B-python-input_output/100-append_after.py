#!/usr/bin/python3
"""Define function that appends string"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing a specific string.
    Args:
        search_string(str): string being searched for
        filename(str): name of file being changed
        new_string(str): string to append str
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.truncate(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')