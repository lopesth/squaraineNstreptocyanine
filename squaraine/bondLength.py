#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Friday, 12 January 2018"

''' Description: Calculate the bond length'''
#########################################################################################

#########################################################################################
# Impoted Modules
from twoPoints import TwoPoints
#########################################################################################

class bondLength(object):
    def __init__(self, molecule):
        self.molecule = molecule

    def returnBondLength(self, atomNumber1, atomNumber2):
        atom1 = self.molecule.returnAtom(atomNumber1)
        atom2 = self.molecule.returnAtom(atomNumber2)
        bondLength = self.calculeBondLenght(atom1, atom2)
        return bondLength

    def calculeBondLenght(self, atom1, atom2):
        x1 = atom1.returnXPos()
        x2 = atom2.returnXPos()
        y1 = atom1.returnYPos()
        y2 = atom2.returnYPos()
        z1 = atom1.returnZPos()
        z2 = atom2.returnZPos()
        bondLength = TwoPoints([x1, y1, z1], [x2, y2, z2]).distanceBetween()
        return bondLength


    
