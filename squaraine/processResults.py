#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Friday, 12 January 2018"

'''Description: Script to process squaraines results (B.X.A abd polarizabilities)'''
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
        bondElpt.append(float(molecule.returnBondElip(x)))
    return bondElpt

# Function Description: Function to find polarizability data
def findPolarizabilities(fileName, components):
    molecule = PolarG09Process(fileName, 2)
    dipole = list(molecule.returnDipole(components[0]).values())[0]
    alpha = list(molecule.returnAlpha(components[1]).values())[0]
    beta = list(molecule.returnBeta(components[2]).values())[0]
    gamma = list(molecule.returnGamma(components[3]).values())[0]
    return [dipole, alpha, beta, gamma]

# Function Description: Function to compute the Δr of Meyers Paper (DOI: 10.1002/chem.19970030408)
def delta_r(b, c, d):
    return 1/2*(abs(b -c) + abs(d-c))

# Function Description: Function to compute the ΔR of Meyers Paper (DOI: 10.1002/chem.19970030408)
def delta_R(ringValue1, ringValue2, typeR):
    if typeR == 1:
        return (ringValue1 + ringValue2)/2
    return 0

# Function Description: 
def alternance(seqListValues):
    anchor1 =  seqListValues[0] 
    result = 0
    for i in range(1, len(seqListValues)):
        anchor2 = seqListValues[i]
        result = result + abs(anchor1 - anchor2)
        anchor1 =  seqListValues[i]
    return (result/i)

# Function Description: Function for processing QTAIM data
def aimallLapl(fileName, bondGroup):
    bondElpt = []
    for bond in bondGroup:
        molecule = QTAIMaimall(fileName)
        x = molecule.searchCPbetweenAtons(bond)
        bondElpt.append(float(molecule.returnLaplacian(x)))
    return bondElpt

# Function Description: Function for processing QTAIM data
def aimallRho(fileName, bondGroup):
    bondElpt = []
    for bond in bondGroup:
        molecule = QTAIMaimall(fileName)
        x = molecule.searchCPbetweenAtons(bond)
        bondElpt.append(float(molecule.returnRho(x)))
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
        'squaraine-H-H-H' : 28, 'squaraine-H-NH2-H' : 30, 'squaraine-H-NMe2-H' : 36, 'squaraine-H-OH-H' : 29, 'squaraine-H-OMe-H' : 32,
        'squaraine-NH2-OMe-H' : 34, 'squaraine-NH2-NH2-H' : 32, 'squaraine-NH2-NMe2-H' : 38, 'squaraine-NMe2-NMe2-H' : 44,
        'squaraine-OH-NH2-H' : 31, 'squaraine-OH-NMe2-H' : 37, 'squaraine-OH-OH-H' : 30, 'squaraine-OH-OMe-H' : 33,
        'squaraine-OMe-NMe2-H' : 40, 'squaraine-OMe-OMe-H' : 36, 'squaraine-NH2-OMe-H' : 34
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
    categories = [categorieOfMolecule1]
    for molecules in categories:
        typeMol = "H"
        fileToWName = "meyersAlternationFile_"+typeMol+".dat"
        filetoWrite = open(dir+"/"+fileToWName, "w")
        filetoWrite.write("{:>23s} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15} {:>15}\n" .format("Molecule", "BLA", "BOA", "BEA", "BLPA", "BDA", "Dipole*", "Alpha*", "Beta*", "Gamma*"))
        for moleculeName in list(molecules.keys()):
            molecule = CreateMolecule(dir+"opt/opt_"+moleculeName+".log", molecules[moleculeName]).returnMolecule()
            bonds1 = bonds(ring1)
            bonds2 = bonds(ring2)
            bondL1 = bdLength(molecule, bonds1)
            bondL2 = bdLength(molecule, bonds2)
            delta_r_BL1 = delta_r(bondL1[0], bondL1[1], bondL1[2])
            delta_r_BL2 = delta_r(bondL2[0], bondL2[1], bondL2[2])
            bondE1 = aimallElipt(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds1)
            bondE2 = aimallElipt(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds2)
            bondLapl1 = aimallLapl(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds1)
            bondLapl2 = aimallLapl(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds2)
            bondRho1 = aimallRho(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds1)
            bondRho2 = aimallRho(dir+"opt/aimall_calc/opt_"+moleculeName+".mgp", bonds2)
            delta_r_E1 = delta_r(bondE1[0], bondE1[1], bondE1[2])
            delta_r_E2 = delta_r(bondE2[0], bondE2[1], bondE2[2])
            delta_r_Lap1 = delta_r(bondLapl1[0], bondLapl1[1], bondLapl1[2])
            delta_r_Lap2 = delta_r(bondLapl2[0], bondLapl2[1], bondLapl2[2])
            delta_r_Rho1 = delta_r(bondRho1[0], bondRho1[1], bondRho1[2])
            delta_r_Rho2 = delta_r(bondRho2[0], bondRho2[1], bondRho2[2])
            polarizabilities = findPolarizabilities(
                dir+"polar/polar_"+moleculeName+".log", ['Tot', 'iso', '||', '||']
            )
            dipole = polarizabilities[0]
            alpha = polarizabilities[1]
            beta = polarizabilities[2]
            gamma = polarizabilities[3]
            bondO1Mayer = bdOrder(dir+"opt/multiwfn_calc/opt_"+moleculeName+"_bndmat_mayer.txt", molecules[moleculeName], bonds1)
            bondO2Mayer = bdOrder(dir+"opt/multiwfn_calc/opt_"+moleculeName+"_bndmat_mayer.txt", molecules[moleculeName], bonds2)
            delta_r_BO1 = delta_r(bondO1Mayer[0], bondO1Mayer[1], bondO1Mayer[2])
            delta_r_BO2 = delta_r(bondO2Mayer[0], bondO2Mayer[1], bondO2Mayer[2])
            delta_R_BO = delta_R(delta_r_BO1, delta_r_BO2, 1)
            delta_R_BE = delta_R(delta_r_E1, delta_r_E2, 1)
            delta_R_BL = delta_R(delta_r_BL1, delta_r_BL2, 1)
            delta_R_Lap = delta_R(delta_r_Lap1, delta_r_Lap2, 1)
            delta_R_Rho = delta_R(delta_r_Rho1, delta_r_Rho2, 1)

            filetoWrite.write("{:>23s} {:>15.7f} {:>15.7f} {:>15.7f} {:>15.7f} {:>15.7f} {:>15.7f} {:>15.7f} {:>15.7f} {:>15.7f}\n" .format(
                moleculeName, delta_R_BL, delta_R_BO, delta_R_BE, delta_R_Lap, delta_R_Rho, dipole, alpha, beta, gamma
            ))
        filetoWrite.write("\nBLA -> Bond Lenght Alternation\nBOA -> Mayer Bond Order Alternation\nBEA -> Bond Ellipticity Alternation\nBLPA -> Bond Laplacian Alternation\nBDA -> Bond Density Alternation\n* All polarization properties are invariant with respect to the orientation of the molecule")
        filetoWrite.close