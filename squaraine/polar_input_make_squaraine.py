__author__ = "Thiago Lopes"
__email__ = "lopes.th.o@gmail.com"
__date__ = "2017-12-21 09:38:03"

import os
from find_xyz_from_a_log import Find_XYZ
dirMother = "".join([ "/"+x for x in os.getcwd().split("/")[0:-1] if len(x) >0])
dirOpt = dirMother+"/opt"
dirPolar = dirMother+"/polar"
polarFreqs = "0.0  0.0239 0.04282"

molecules = {
    "squaraine-H-NMe2" : 36, "squaraine-NMe2-NMe2" : 44, "squaraine-OMe-H" : 32,
    "squaraine-OMe-NMe2" : 37, "squaraine-OMe-OMe" : 36, "squaraine_H-H" : 28,
    "squaraine_OH-OH" : 30, "stilbene_H-H" : 54, "stilbene_O-OH" : 56, "stilbene_OH-OH" : 56
}

for molecule in list(molecules.keys()):
    geomFile = dirOpt+"/opt_" + molecule
    nameFile = dirPolar+"/polar_"+ molecule
    geom = Find_XYZ(geomFile+".log", molecules[molecule]).gaussian_style()
    fileToWrite = open(nameFile+".com", "w")
    fileToWrite.write('{}chk={}.chk \n{}nprocshared=4 \n{}mem=2000mb \n' .format("%", nameFile.split("/")[-1],"%", "%") )
    fileToWrite.write('#p nosymm output=wfn wb97x/6-31++G** polar=(cubic,dcshg) density=current pop=chelpg\n\nPolar calculation of the {}\n\n0 1\n' .format("polar_"+ molecule))
    for atomCoord in geom:
        fileToWrite.write(atomCoord+"\n")
    fileToWrite.write("\n")
    fileToWrite.write("{}\n" .format(polarFreqs))
    fileToWrite.write("\n\n")