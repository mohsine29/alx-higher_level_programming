#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(*args)
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
    return (result)
