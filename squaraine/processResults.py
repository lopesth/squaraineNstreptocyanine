#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Friday, 12 January 2018"

''' Description: Script to process squaraines results (B.X.A abd polarizabilities)'''
#########################################################################################

#########################################################################################
# Impoted Modules
import os
from atonsNmolecule import Molecule, Atom
#########################################################################################




# Description: main function of the script
if (__name__ == "__main__"):
    ring1 = {"b":["C10", "C9"], "c":["C9", "C8"], "d":["C8", "C6"], "e":["C6", "C2"], "f":["C2", "C1"], "f'":["C1", "C4"]}
    ring2 = {"b":["C15", "C16"], "c":["C16", "C17"], "d":["C17", "C7"], "e":["C7", "C4"], "f":["C1", "C4"], "f'":["C1", "C2"]}
    print(ring1)