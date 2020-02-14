#!usr/bin/#!/usr/bin/env python3

""" Program that generate errors """
# There should be 12 other errors in the list from assignment 1 that
# you should be able to understand. Select 10 errors and write a program
# or small programs in which your code causes those. If you can isolate
# the code in a function (like ZeroDivisionError) do that and don't call
# the function. Otherwise write and test the code and then make it a comment block.
# You are allowed to discuss (calmly) and you can browse the internet to
# find more background and maybe examples of error raising code.

__author__ = "fennaf"

import sys
import math


def index_error():
    """ create index error by calling index that does not exist (only 0..3)"""
    some_list = ["there", "are", "four", "elements"]
    return some_list[4]


def zero_division_error():
    """ create zero devision error by divide by zero """
    return 2 / 0


def type_error():
    """ crreate type error by adding int and string  """
    return 1 + "2"


def file_not_found_error(file):
    """ create file not found error by opening an non-existing file """
    fasta = open(file)
    fasta.close()
    return 0


def attribute_error():
    """ create attribute error by using an attribute next that does not belong to object"""
    pdb = open("BRCA1.gbk")
    pdb.next()
    pdb.close()
    return 0


def key_error():
    """ creatte a key error by using a key that does not exists """
    my_dict = {"C": "cake", "T": "thee"}
    return my_dict["K"]


def name_error():
    """ create a name error by using a variable that does not exist """
    return undefined


def module_error():
    """ create an import error by importing a non existence module """
    import nonsense

    return 0


def math_error():
    """ create a math error by using an expression that is not allowed: math domain error"""
    return math.sqrt(-4)


def recursion_error():
    """ recusion error: maximum recursion depth exceeded, no break prorammed"""
    return recursion_error()


def main(args):
    """ main function """
    # err = index_error()
    # err = zero_division_error()
    # err = type_error()
    # file_not_found_error('RTFM')
    # err = attribute_error()
    # err = module_error()
    # err = key_error()
    # err = name_error()
    # err = math_error()
    # err = recursion_error(a='what',b='duh')
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
