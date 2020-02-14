#!/usr/bin/env python3
""" # 01: needed a quote
A silly program with a collection of syntax errors
"""
__author__ = "Tsjerk A. Wassenaar"  # 08 insert =
# IMPORTS
import sys  # 02: remove ':'

# CONSTANTS (use upper case for global variables)
TWO_TIMES_PI = 6.283185  # 10 two instead of 2
MASS = {
    "H": 1.008,  # 09 , instead of ;
    "C": 12.011,
    "O": 15.998,
}  # 03: remove '}'

# FUNCTIONS
# def 04: remove def
def fun(a, b, c):  # 05 added :
    """ function that calculates ((a) + (b)) * c """
    return ((a) + (b)) * c  # 06 wrong parenthis order


# MAIN
def main(args):
    """ main function """
    print(fun(MASS["H"], MASS["C"], MASS["O"]))
    return 0


if __name__ == "__main__":  # 06 == instead of =
    EXITCODE = main(sys.argv)  # 07 sys.argv instead of sys..argv
    sys.exit(EXITCODE)  # 11
