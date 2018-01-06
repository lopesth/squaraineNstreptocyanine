#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Jan 06 of 2018"

# Description: Prepare the squaraines optimization inputs for submission

########################################################################################

#########################################################################################
# Impoted Modules
import os
from shutil import copyfile
from find_xyz_from_a_log import Find_XYZ
#########################################################################################

dirMother = "/Users/thiagolopes/Google Drive/squaraine/"
dirOpt = dirMother+"opt/"
dirGeom = dirMother+"pre_opt/"

# List of molecules with number of atoms
molecules = {
    'squaraine-H-H-H' : 28, 'squaraine-H-H-O' : 29, 'squaraine-H-H-OH' : 29, 'squaraine-H-NH2-H' : 30, 'squaraine-H-NH2-O' : 31, 'squaraine-H-NH2-OH' : 31,
    'squaraine-H-NMe2-H' : 36, 'squaraine-H-NMe2-O' : 37, 'squaraine-H-NMe2-OH' : 37, 'squaraine-H-OH-H' : 29, 'squaraine-H-OH-O' : 30, 'squaraine-H-OH-OH' : 30,
    'squaraine-H-OMe-H' : 32, 'squaraine-H-OMe-O' : 33, 'squaraine-H-OMe-OH' : 33, 'squaraine-NH2-NH2-H' : 32, 'squaraine-NH2-NH2-O' : 33, 'squaraine-NH2-NH2-OH' : 33,
    'squaraine-NH2-NMe2-H' : 38, 'squaraine-NH2-NMe2-O' : 39, 'squaraine-NH2-NMe2-OH' : 39, 'squaraine-NH2-OMe-H' : 32, 'squaraine-NH2-OMe-O' : 33, 'squaraine-NH2-OMe-OH' : 33,
    'squaraine-NMe2-NMe2-H' : 44, 'squaraine-NMe2-NMe2-O' : 45, 'squaraine-NMe2-NMe2-OH' : 45, 'squaraine-OH-NH2-H' : 31, 'squaraine-OH-NH2-O' : 32, 'squaraine-OH-NH2-OH' : 32,
    'squaraine-OH-NMe2-H' : 37, 'squaraine-OH-NMe2-O' : 38, 'squaraine-OH-NMe2-OH' : 38, 'squaraine-OH-OH-H' : 30, 'squaraine-OH-OH-O' : 31, 'squaraine-OH-OH-OH' : 31,
    'squaraine-OH-OMe-H' : 33, 'squaraine-OH-OMe-O' : 34, 'squaraine-OH-OMe-OH' : 34, 'squaraine-OMe-NMe2-H' : 40, 'squaraine-OMe-NMe2-O' : 41, 'squaraine-OMe-NMe2-OH' : 41,
    'squaraine-OMe-OMe-H' : 36, 'squaraine-OMe-OMe-O' : 37, 'squaraine-OMe-OMe-OH' : 37, 'stilbene-NMe2-OMe-H' : 54, 'stilbene-NMe2-OMe-O' : 55, 'stilbene-NMe2-OMe-OH' : 55
}

# Description: main function of the script
if (__name__ == "__main__"):
    for molecule in list(molecules.keys()):
        geomFile = dirGeom+"pre_opt_" + molecule
        nameFile = dirOpt+"opt_"+ molecule
        geom = Find_XYZ(geomFile+".log", molecules[molecule]).gaussian_style()
        fileToWrite = open(nameFile+".com", "w")
        copyfile(geomFile+".chk", nameFile+".chk")
        fileToWrite.write('{}chk={}.chk \n{}nprocshared=6 \n{}mem=30000mb \n' .format("%", nameFile.split("/")[-1],"%", "%") )
        fileToWrite.write('#p opt=(ReadFC, gdiis) nosymm output=wfn wb97x/6-31++G**\n\nOptimization of the {}\n\n0 1\n' .format(nameFile))
        for atomCoord in geom:
            fileToWrite.write(atomCoord+"\n")
        fileToWrite.write("\n\n")