#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Friday, 12 January 2018"

''' Description: Calculate the distance between two points'''
#########################################################################################

#########################################################################################
# Impoted Modules
from math import sqrt
from math import pow
#########################################################################################

class TwoPoints(object):
    def __init__(self, point1, point2):
        self.x1 = point1[0]
        self.x2 = point2[0]
        self.y1 = point1[1]
        self.y2 = point2[1]
        self.z1 = point1[2]
        self.z2 = point2[2]

    def distanceBetween(self):
        xDif = pow((self.x1 - self.x2), 2)
        yDif = pow((self.y1 - self.y2), 2)
        zDif = pow((self.z1 - self.z2), 2)
        return sqrt(xDif + yDif + zDif)
