#!/usr/bin/env python3
"""
Print all the errors that are available as built-in in Python3
together with their docstrings.
"""
__author__ = "Tsjerk A. Wassenaar"
# IMPORTS
import sys

# CONSTANTS
# FUNCTIONS
def error_doc(err):
    "Return the docstring of an error given as name (str)"
    return getattr(__builtins__, err).__doc__


# MAIN
def main(args):
    """Run the program with argument list args"""
    # Preparation - Collect errors from __builtins__
    # Work - Print the errors with the docstring
    errors = []
    for item in dir(__builtins__):
        if item.endswith("Error"):
            errors.append(item)
            print(item, ":", error_doc(item), end="\n---\n")
    # Finish - nothing to do...
    return 0


if __name__ == "__main__":
    exitcode = main(sys.argv)
    sys.exit(exitcode)
