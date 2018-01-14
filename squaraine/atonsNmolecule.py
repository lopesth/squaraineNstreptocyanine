#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Friday, 12 January 2018"

''' Description: Creates a molecule as an object'''
#########################################################################################

class Atom(object):
    def __init__(self, atomType, xPos, yPos, ZPos):
        self.atomType =atomType 
        self.xPos = xPos
        self.yPos = yPos
        self.zPos = ZPos

    def returnAtomType(self):
        return self.atomType
    
    def returnXPos(self):
        return self.xPos

    def returnYPos(self):
        return self.yPos

    def returnZPos(self):
        return self.zPos

    def returnPos(self):
        return [self.xPos, self.yPos, self.zPos]
    
    def returnAtom(self):
        return [self.atomType, self.xPos, self.yPos, self.zPos]

    def moveAtom(self, newX, newY, newZ):
        self.xPos = newX
        self.yPos = newY
        self.zPos = newZ

class Molecule(object):
    def __init__(self):
        self.atons = []

    def addAtom(self, atom):
        self.atons.append(atom)

    def returnAtom(self, number):
        return self.atons[number]

    def moveAtom(self, numer, newPOS):
        newX = newPOS[0]
        newY = newPOS[1]
        newZ = newPOS[2]
        self.atons[number].moveAtom(newX, newY, newZ)

    def returnAllAtons(self):
        return self.atons