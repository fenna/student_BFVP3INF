#!/usr/bin/env python3
"""this programme reads fasta file(s) and reports number of nucleotides/amino acids"""
# METADATA VARIABLES
__author__ = "WERD"
__version__ = "2019.1"
# IMPORTS
import sys

# LOGICA
def count_ATCG(sequence):
    A = 0
    C = 0
    T = 0
    G = 0
    A = sequence.count("A")
    C = sequence.count("C")
    T = sequence.count("T")
    G = sequence.count("G")
    return A, C, T, G


def count_cg(sequence):
    """count cg percentage"""
    gc = sequence.count("G") + sequence.count("C")
    return gc * 100 / len(sequence)


def count_aminoc_acids(sequence):
    """count the amino acids and print the results """
    amino_acids = 0
    # write your code here
    amino_acids = len(sequence)
    return amino_acids


def determine_type(sequence):
    """distinghuis file types"""
    file_type = ""
    # here you have to come up with a solution to distinguish file types.
    if sequence.count("U") > 0:
        file_type = "mRNA_fasta"
    elif sequence.count("M") > 0:
        file_type = "protein_fasta"
    elif sequence.count("U") == 0 and sequence.count("M") == 0:
        file_type = "nucleotide_fasta"
    return file_type


def fetch_sequence(f):
    sequence = ""
    for line in f:
        if not line.startswith(">"):
            sequence += line
    return sequence


def main(args):
    # preperation
    filenames = args[1:]
    for file in filenames:
        f = open(file)
        sequence = fetch_sequence(f)
        file_type = determine_type(sequence)
        if file_type == "protein_fasta":
            print(count_aminoc_acids(sequence))
        if file_type == "nucleotide_fasta":
            A, C, T, G = count_ATCG(sequence)
            print(A, C, T, G)
            print(count_cg(sequence))
        f.close()
    return 0


if __name__ == "__main__":
    print(sys.argv)
    exitcode = main(sys.argv)
    sys.exit(exitcode)
