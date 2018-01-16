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
from createMoleculeFromG09Opt import CreateMolecule
from bondLength import BondLength
from bondOrderMultiwfn import BondOrder
from aimallQTAIM import QTAIMaimall
from processPolarizabities import PolarG09Process
#########################################################################################

# Function Description: Calculate Bond Length
def bdLength(fileName, bondGroup):
    moleculeBondLength = BondLength(fileName)
    bonds = []
    for bond in bondGroup:
        bondlgt = moleculeBondLength.returnBondLength(bond[0]-1, bond[1]-1)
        bonds.append(bondlgt)
    return (bonds)

# Function Description: Calculate Bond Order
def bdOrder(fileName, basis, bondGroup):
    moleculeBondOrder = BondOrder(fileName, basis)
    bonds = []
    for bond in bondGroup:
        bondOd = moleculeBondOrder.filter_BO_interest([bond[0], bond[1]])
        bonds.append(bondOd)
    return bonds

# Function Description: Isolates the bond pattern
def bonds(dictionary):
    bonds = []
    for element in list(dictionary.values()):
        x = [element[0][1], element[1][1]]
        bonds.append(x)
    return bonds

# Function Description: Function for processing QTAIM data
def aimallElipt(fileName, bondGroup):
    bondElpt = []
    for bond in bondGroup:
        molecule = QTAIMaimall(fileName)
        x = molecule.searchCPbetweenAtons(bond)
        bondElpt.append(molecule.returnBondElip(x))
    return bondElpt
        

# Description: main function of the script
if (__name__ == "__main__"):
    ring1 = {
        "b":[["C", 10], ["C", 9]], "c":[["C", 9],["C", 8]],
        "d":[["C", 8], ["C", 6]], "e":[["C", 6], ["C", 2]],
        "f":[["C", 2], ["C", 1]], "f'":[["C", 1], ["C", 4]]
    }
    ring2 = {
        "b":[["C", 15], ["C", 16]], "c":[["C", 16], ["C", 17]],
        "d":[["C", 17], ["C", 7]], "e":[["C", 7], ["C", 4]],
        "f":[["C", 1], ["C", 4]], "f'":[["C", 1], ["C", 2]]
    }
    dir = "/Users/thiagolopes/Google Drive/squaraine/"
    categorieOfMolecule1 = {
        'squaraine-H-H-H' : 28, 'squaraine-H-NH2-H' : 30, 'squaraine-H-NMe2-H' : 36, 'squaraine-H-OH-H' : 29, 'squaraine-NH2-OMe-H' : 34,
        'squaraine-H-OMe-H' : 32, 'squaraine-NH2-NH2-H' : 32, 'squaraine-NH2-NMe2-H' : 38, 'squaraine-NMe2-NMe2-H' : 44,
        'squaraine-OH-NH2-H' : 31, 'squaraine-OH-NMe2-H' : 37, 'squaraine-OH-OH-H' : 30, 'squaraine-OH-OMe-H' : 33,
        'squaraine-OMe-NMe2-H' : 40, 'squaraine-OMe-OMe-H' : 36, 'squaraine-NH2-OMe-H' : 34, 'stilbene-NMe2-OMe-H' : 54
    }
    categorieOfMolecule2 = {
        'squaraine-H-H-O' : 29, 'squaraine-H-NH2-O' : 31, 'squaraine-H-NMe2-O' : 37, 'squaraine-H-OH-O' : 30,
        'squaraine-H-OMe-O' : 33, 'squaraine-NH2-NH2-O' : 33, 'squaraine-NH2-NMe2-O' : 39, 'squaraine-NH2-OMe-O' : 33,
        'squaraine-NMe2-NMe2-O' : 45, 'squaraine-OH-NH2-O' : 32, 'squaraine-OH-NMe2-O' : 38, 'squaraine-OH-OH-O' : 31,
        'squaraine-OH-OMe-O' : 34, 'squaraine-OMe-NMe2-O' : 41, 'squaraine-OMe-OMe-O' : 37, 'stilbene-NMe2-OMe-O' : 55,
        'squaraine-NH2-H-O' : 31, 'squaraine-NH2-OH-O' : 32, 'squaraine-NH2-OMe-O' : 35, 'squaraine-NMe2-H-O' : 37,
        'squaraine-NMe2-OH-O' : 38, 'squaraine-NMe2-OMe-O' : 41, 'squaraine-OH-H-O' : 30, 'squaraine-OMe-H-O' : 33,
        'squaraine-OMe-NH2-O' : 35, 'squaraine-NMe2-NH2-O' : 39, 'squaraine-OMe-OH-O' : 34
    }
    categorieOfMolecule3 = {
        'squaraine-H-H-OH' : 29, 'squaraine-H-NH2-OH' : 31, 'squaraine-H-NMe2-OH' : 37, 'squaraine-H-OH-OH' : 30,
        'squaraine-H-OMe-OH' : 33, 'squaraine-NH2-NH2-OH' : 33, 'squaraine-NH2-NMe2-OH' : 39, 'squaraine-NH2-OMe-OH' : 33,
        'squaraine-NMe2-NMe2-OH' : 45, 'squaraine-OH-NH2-OH' : 32, 'squaraine-OH-NMe2-OH' : 38, 'squaraine-OH-OH-OH' : 31,
        'squaraine-OH-OMe-OH' : 34, 'squaraine-OMe-NMe2-OH' : 41, 'squaraine-OMe-OMe-OH' : 37, 'stilbene-NMe2-OMe-OH' : 55,
        'squaraine-NH2-H-OH' : 31, 'squaraine-OMe-OH-OH' : 34, 'squaraine-OMe-NH2-OH' : 35, 'squaraine-OH-H-OH' : 30,
        'squaraine-NMe2-OH-OH' : 41, 'squaraine-NMe2-OMe-OH' : 41, 'squaraine-OMe-H-OH' : 33, 'squaraine-NMe2-H-OH' : 37,
        'squaraine-NMe2-NH2-OH' : 39, 'squaraine-NH2-OMe-OH' : 35, 'squaraine-NH2-OH-OH' : 32
    }
    categories = [categorieOfMolecule1, categorieOfMolecule2, categorieOfMolecule3]
    for molecules in categories:
        for moleculeName in list(molecules.keys()):
            molecule = CreateMolecule(dir+"opt/opt_"+moleculeName+".log", molecules[moleculeName]).returnMolecule()
            bonds1 = bonds(ring1)
            bonds2 = bonds(ring2)
            bondL1 = bdLength(molecule, bonds1)
            bondL2 = bdLength(molecule, bonds2)
            bondE1 = aimallElipt(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds1)
            bondE2 = aimallElipt(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds2)
            for boType in ["mayer", "mulliken", "wiberg"]:
                bondO1 = bdOrder(dir+"opt/multiwfn_calc/opt_"+moleculeName+"_bndmat_"+boType+".txt", molecules[moleculeName], bonds1)
                bondO2 = bdOrder(dir+"opt/multiwfn_calc/opt_"+moleculeName+"_bndmat_"+boType+".txt", molecules[moleculeName], bonds2)
