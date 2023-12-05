#!/usr/bin/python3
"""Define function that checks instance."""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of a class of inherited a_class.
    
    Args:
        obj: object being checked.
        a_class: class being compared
    Returns:
        True - If obj is an instance or inherited instance of a_class
        else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False