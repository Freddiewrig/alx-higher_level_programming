#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as exe:
        print("Exception: {}".format(exe), file=sys.stderr)
        return None
    else:
        return result