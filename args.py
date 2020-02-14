#!/usr/bin/env python


"""fetches the argument from the command line and print them reverse with index"""

__author__ = "Akastia Christo"

import sys

def make_args(*args):
	for index, value in enumerate(*args):
		print(index + 1, value)

def main(args):
	make_args(args[::-1])
	return 0

if __name__ == "__main__":
	exitcode = main(sys.argv)
	sys.exit(exitcode)