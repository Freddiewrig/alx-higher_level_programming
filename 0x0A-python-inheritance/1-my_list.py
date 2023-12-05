#!/usr/bin/python3
"""Define class my_list that inherits from list"""


class Mylist(list):
    """Implement a print for the sorted list."""

    def print_sorted(self):
        """Print in ascending order"""
        print(sorted(self))