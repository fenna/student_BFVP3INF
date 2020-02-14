#!/usr/bin/env python3

"""
This is a program that calculates
- Phredscore (Ascii value - 33)
- Accuracy: (exponent =(-1*numscore/10); Q = 1 - (10**exponent))
input: a file with reads from a sequencer (default reads.fq)
Each read constists of:
A first line describing the machine it was run on, the chip identifier and
-the actual coordinates from the chip where the base was read :@M01785:20:0...
-The actual read sequence                    :NTCATGTACGGTCAGGATGG...
-The plus sign                               :+
-The predicted read base quality ASCII value :#>>1A1B3B11BAEFFBECA...
The purpose is to read the line with the quality ASCII values (line after +)
and calculates Phredscore and quality base
The outcome of the test string #>>1A1B3B1 should be:
Quality score: #>>1A1B3B1
Phredscore   :    2    |   29   |   29   |   16   |   32   |   16   |   33   |   18   |   33   |   16   |
Accuracy     :  36.90% | 99.87% | 99.87% | 97.49% | 99.94% | 97.49% | 99.95% | 98.42% | 99.95% | 97.49% |
"""

__author__ = "Fenna Feenstra"
__version__ = "0.2"

# imports
import sys

# functions
def phred_score(char):
    """ this function scores the base by converting the ascii value to a
    number and substract this with the offset """
    # correct this line
    num_score = ord(char) - 33
    return num_score


def base_call_accuracy(numscore):
    """ this function calculates the quality percentage"""
    # correct this with the correct formula
    exponent = -1 * numscore / 10
    quality = 1 - (10 ** exponent)
    return quality


def fetch_read(file):
    """ reead the file and fetch the line"""
    flag = False
    with open(file) as reads:
        for line in reads:
            if flag:
                return line.strip()
            if line.startswith("+"):
                flag = True
    return 0


def calc_phred_accur(sequence):
    """ for each character in sequence calculate PhredScore and accuracy """
    # create empty lists
    phreds = ""
    accurs = ""
    for character in sequence:
        quality_score = base_call_accuracy(phred_score(character))
        # append to list
        length = len(" {:.2%}".format(quality_score)) - 1
        phreds += " {:^{length}} |".format(phred_score(character), length=length)
        accurs += " {:.2%} |".format(quality_score)
    return [phreds, accurs]


# main
def main(args):
    """ this is the main function which calls other functions"""
    if len(args) > 1:
        sequence = fetch_read(args[1])
    else:
        sequence = "#>>1A1B3B1"
    [phreds, accurs] = calc_phred_accur(sequence)
    # finish
    print("Quality score: {}".format(sequence))
    print("Phredscore   : {}".format(phreds))
    print("Accuracy     : {}".format(accurs))
    return 0


# entryppoint
if __name__ == "__main__":
    sys.exit(main(sys.argv))
