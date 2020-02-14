#!/usr/bin/env python3 #01 wrong shebang

"""
A program with errors.
The program should extract the sequence from a PDB file
Usage:
    fixme.py pdbfile
When corrected, the program will produce output like:
MET GLN ILE PHE VAL LYS THR LEU THR GLY LYS THR ILE THR LEU GLU VAL GLU PRO SER ASP THR ILE GLU ...
2013 - Tsjerk A. Wassenaar
"""  # 02 quotes

import sys  # 04 Sys -> sys

# Extracting the sequence from a PDB file
#
# The first six characters of each line in a PDB file show the kind of content
# At this point only the lines starting with 'ATOM' count.
# The ATOM lines have the following structure:
#
# ATOM    493  CA  LYS A  63      21.656  26.847   5.240  1.00 11.97           C
#
# 012345678901234567890123456789012345678901234567890123456789012345678901234567890
#              ||  +++
#
# The residue is in line[17:20]. Each residue has one c-alpha atom,
# which has ' CA ' in line[12:16]. If we select only those lines and
# get the residue, were done.

def get_pdb_sequence(filename):
    """Extract the sequence from a PDB file"""
    pdb = open(filename)
    seq = []
    for line in pdb:
        # 03 startswith #04 needs : at and of line
        if (line.startswith("ATOM") and line[12:16] == " CA "):  
            seq.append(line[17:20])
    pdb.close()
    return seq  # 09 funtion need to return seq


def main(args):
    """ main function that calls the other functions"""
    if len(args) == 1:  # 06: argv -> args
        print(__doc__)
        # We step out of the main function here
        return 0
    sequence = get_pdb_sequence(
        sys.argv[1]
    )  # 07 getPDBSequence -> getPdbSequence, 08:argv -> argv[1]
    print(len(sequence))
    print(" ".join(sequence))
    # The end of the main function, stepping out
    return 0


if __name__ == "__main__":
    # Execute the main function if this is run as program
    sys.exit(main(sys.argv))  # 05 args -> argv
