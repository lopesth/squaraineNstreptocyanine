#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Jan 08 of 2018"

''' Description: Script to prepare the inputs of squaraine polarizability
parameter calculations '''
#########################################################################################
#########################################################################################
# Impoted Modules
import os
from find_xyz_from_a_log import Find_XYZ
#########################################################################################

dirMother = "/Users/thiagolopes/Google Drive/squaraine/"
dirOpt = dirMother+"opt/"
dirPolar = dirMother+"polar/"
polarFreqs = "0.0  0.0239 0.04282"

# List of molecules with number of atoms
molecules = {
     'squaraine-NH2-H-O' : 31, 'squaraine-NH2-H-OH' : 31, 'squaraine-NH2-OH-O' : 32, 'squaraine-NH2-OH-OH' : 32,
    'squaraine-NH2-OMe-H' : 34, 'squaraine-NH2-OMe-O' : 35, 'squaraine-NH2-OMe-OH' : 35, 'squaraine-NMe2-H-O' : 37,
    'squaraine-NMe2-H-OH' : 37, 'squaraine-NMe2-NH2-O' : 39, 'squaraine-NMe2-NH2-OH' : 39, 'squaraine-NMe2-OH-O' : 38,
    'squaraine-NMe2-OH-OH' : 41, 'squaraine-NMe2-OMe-O' : 41, 'squaraine-NMe2-OMe-OH' : 41, 'squaraine-OH-H-O' : 30,
    'squaraine-OH-H-OH' : 30, 'squaraine-OMe-H-O' : 33, 'squaraine-OMe-H-OH' : 33, 'squaraine-OMe-NH2-O' : 35,
    'squaraine-OMe-NH2-OH' : 35, 'squaraine-OMe-OH-O' : 34, 'squaraine-OMe-OH-OH' : 34
}

# Description: main function of the script
if (__name__ == "__main__"):
    for molecule in list(molecules.keys()):
        geomFile = dirOpt+"opt_" + molecule
        nameFile = dirPolar+"polar_"+ molecule
        geom = Find_XYZ(geomFile+".log", molecules[molecule]).gaussian_style()
        fileToWrite = open(nameFile+".com", "w")
        fileToWrite.write('{}chk={}.chk \n{}nprocshared=4 \n{}mem=2000mb \n' .format("%", nameFile.split("/")[-1],"%", "%") )
        fileToWrite.write('#p nosymm wb97x/6-31++G** polar=(cubic,dcshg) density=current pop=chelpg\n\nPolar calculation of the {}\n\n0 1\n' .format("polar_"+ molecule))
        for atomCoord in geom:
            fileToWrite.write(atomCoord+"\n")
        fileToWrite.write("\n")
        fileToWrite.write("{}\n" .format(polarFreqs))
        fileToWrite.write("\n\n")