#!/usr/bin/env python3
"""
This program takes a pdb file and calculates the atomweigth
"""
__author__ = "F.Feenstra, M.Kempenaar, T. Wassenaar"
# IMPORTS
import sys

# CONSTANTS
# Atom masses don't change...
ATOMMASS = {"C": 12.011, "N": 14.007, "O": 15.998, "P": 30.974, "S": 32.065, "H": 1.008}
# FUNCTIONS
def calc_weight(atom):
    """ function that fetches the atom weight from the atom """
    for element in atom:
        if element in ATOMMASS:
            return ATOMMASS[element]
    print("Element not in mass table:", element)
    return 0


def processfile(input_fiile):
    """ fetch all the atom lines and calculate the weight """
    inpf = open(input_fiile)
    count = 0
    for line in inpf:
        if line.startswith("ATOM"):  # or line.startswith('HETATM'):
            atom = line[13:14]
            count += calc_weight(atom)
    inpf.close()
    return count


def store_atomweight(weight, output_file):
    """ function that stores the atomweight in a file """
    out = open(output_file, "w")
    print("atomweight: " + str(weight))
    out.write("atomweight:" + str(weight) + "\n")
    out.close()


# MAIN
def main(args):
    """ main function that calls the other functions """
    # Preparation
    if len(args) < 3:
        print("please provide the name of an input and an output file")
        print("Program stopping...")
        return 0
    input_file = args[1]
    output_file = args[2]
    # Work
    results = processfile(input_file)
    # Finalize
    store_atomweight(results, output_file)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
