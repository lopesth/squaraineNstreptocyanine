#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Friday, 12 January 2018"

'''Description: Creates a molecule of an optimization output of G09'''
#########################################################################################

#########################################################################################
# Impoted Modules
from find_xyz_from_a_log import Find_XYZ
from atonsNmolecule import Atom, Molecule
#########################################################################################

class CreateMolecule(object):
    def __init__(self, targetFile, base):
        self.targetFile = targetFile
        self.base = base
        self.molecule = Molecule()

    def returnMolecule(self):
        lisPos = Find_XYZ(self.targetFile, self.base).gaussian_style()
        for elementPos in lisPos:
            rawAtom = elementPos.split()
            atomType = rawAtom[0]
            atomX = float(rawAtom[1])
            atomY = float(rawAtom[2])
            atomZ = float(rawAtom[3])
            self.molecule.addAtom(Atom(atomType, atomX, atomY, atomZ))
        return self.molecule
