#!/usr/bin/python3
"""Define class check function"""


def is_same_class(obj, a_class):
    """Check if object is of the exact defined class
    
    Args:
        obj: the object to check.
        a_class: the class to compare to.
    Return:
        True- if obj is an instance of a_class.
        False- if obj is not instance of a_classs
    """
    if type(obj) == a_class:
        return True
    return False