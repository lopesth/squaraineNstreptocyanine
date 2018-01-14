#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Sunday, 14 January 2018"

''' Description: Class to bundle QTAIM data from AIMALL outputs'''
#########################################################################################

#########################################################################################
# Impoted Modules
from find_a_string_in_file import Find_a_String
from re import sub
#########################################################################################

class qtaimAIMALL (object):

    def __init__(self, fileName):
        self.fileName = fileName
        self.CPs = self.__catCPs()
        self.CPtypes = self.__catCPtype()
        self.Rhos = self.__catRho()
        self.HessMAt = self.__catHessMat()
        self.Laplacian = self.__catLaplacian()
        self.BondElip = self.__catBondElip()

    def __catCPs(self):
        linesCPs = Find_a_String(self.fileName, "CP#").return_numbers_of_line()
        fileString = []
        with open(self.fileName) as myFile:
            for line in myFile:
                fileString.append(line.split())
        resultList = []
        for origCP in linesCPs:
            startNumber = origCP - 1
            endNumber = startNumber + 35
            x = []
            for i in range(startNumber, endNumber):
                x.append(fileString[i])
            resultList.append(x)
        return resultList

    def __catCPtype(self):
        lines = [0, 1]
        bcpType = "(3,-1)"
        ccpType = "(3,+3)"
        rcpType = "(3,+1)"
        acpType = "(3,-3)"
        result = []
        for cp in self.CPs:
            v1 = "{} {}".format(cp[0][0], cp[0][1])
            v2 = "{:11.7f}, {:11.7f}, {:11.7f}" .format(float(cp[0][4]), float(cp[0][5]), float(cp[0][6]))
            posCP = "Positioning between atoms {} and {}" .format(", ".join(cp[1][4:-1]), cp[1][-1])
            if (cp[1][2] == bcpType):
                cptype = "{}: Bond Critical Point (BCP)".format(cp[1][2])
                posCP = "Positioning between atoms {}" .format(" and ".join(cp[1][4:]))
                atonsB = "" .format()
            elif (cp[1][2] == ccpType):
                cptype = "{}: Cage Critical Point (CCP)" .format(cp[1][2])
            elif (cp[1][2] == rcpType):
                cptype = "{}: Ring Critical Point (RCP)" .format(cp[1][2])
            elif (cp[1][2] == acpType):
                cptype = "{}: Non-Nuclear Attractor Critical Point (NNACP)" .format(cp[1][2])
                posCP = "Position of Atom {}" .format(cp[1][4])
            else:
                cptype = "{}: Critical point not found" .format(cp[1][2])
            result.append([v1, v2, cptype, posCP])
        return result

    def __catRho(self):
        result = []
        for cp in self.CPs:
            x = "{:.7f}" .format(float(cp[2][2]))
            result.append(x)
        return result
    
    def __catGradient(self):
        result = []
        for cp in self.CPs:
            x = "{:16.7e} {:16.7e} {:16.7e}" .format(float(cp[3][2]), float(cp[3][3]), float(cp[3][4]))
            result.append(x)
        return result

    def __catHessMat(self, type = 'vector'):
        result = []
        if type == "vector":
            for cp in self.CPs:
                x = "{:16.7e} {:16.7e} {:16.7e}" .format(float(cp[5][2]), float(cp[5][3]), float(cp[5][4]))
                y = "{:16.7e} {:16.7e} {:16.7e}" .format(float(cp[6][2]), float(cp[6][3]), float(cp[6][4]))
                z = "{:16.7e} {:16.7e} {:16.7e}" .format(float(cp[7][2]), float(cp[7][3]), float(cp[7][4]))
                result.append([x, y, z])
        else:
            for cp in self.CPs:
                x = "{:16.7e} {:16.7e} {:16.7e}" .format(float(cp[4][2]), float(cp[4][3]), float(cp[4][4]))
                result.append(x)
        return result

    def __catLaplacian(self):
        result = []
        for cp in self.CPs:
            x = "{:.7f}" .format(float(cp[8][2]))
            result.append(x)
        return result

    def __catBondElip(self):
        result = []
        for cp in self.CPs:
            try:
                x = "{:.7f}" .format(float(cp[9][3]))
            except:
                x = "{}" .format(cp[9][3])
            result.append(x)
        return result

    def returnBondElip(self, cpNumber):
        return self.BondElip[cpNumber-1]

    def returnLaplacian(self, cpNumber):
        return self.Laplacian[cpNumber-1]

    def returnRho(self, cpNumber):
        return self.Rhos[cpNumber-1]

    def searchCPbetweenAtons(self, atonsToLook):
        for cp in self.CPtypes:
            atons = [int(s) for s in sub("\D", " ", cp[3]).split()]
            if len(atons) == len(atonsToLook):
                number = 0
                continueWhile = True
                while continueWhile:
                    try:
                        if atonsToLook[number] in atons:
                            number+=1
                        else:
                            break
                    except:
                        return int(cp[0].split()[1])

    def searchAtomicCP(self, atom1):
        return self.CPtypes[cpNumber-1]

    def returnCPcoord(self, cpNumber):
        return self.CPtypes[cpNumber-1][1]

    def returnCPS(self, cpNumber):
        return self.CPtypes[cpNumber-1]

# Description: main function of the script
if (__name__ == "__main__"):
    filename = "/Users/thiagolopes/Google Drive/squaraine/opt/aimall_calc/opt_squaraine-H-H-H.mgp"
    x = qtaimAIMALL(filename)
    y = x.searchCPbetweenAtons([28, 18])
    w = x.returnCPcoord(y)
    print(w)