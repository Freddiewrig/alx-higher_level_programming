#!/usr/bin/python3
"""Define function to check instance"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class
    
    Args:
        obj: object being checked.
        a_class: class to match with
    Returns:
        True - if the object is an instance of a class
        else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False