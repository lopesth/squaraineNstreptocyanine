#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Sunday, 14 January 2018"

''' Description: Class to process the polarization results in an output of G09'''
#########################################################################################

#########################################################################################
# Impoted Modules
from find_a_string_in_file import Find_a_String 
#########################################################################################

class PolarG09Process(object):

    def __init__(self, fileName, numberOfFreqs):
        self.fileName = fileName
        self.numberOfFreqs = numberOfFreqs
        self.__catPolar()

    def __catPolar(self):
        fileString = []
        self.dipoles = {}
        self.alphas = [{}]
        self.betas = [{}]
        self.gammas = [{}]
        with open(self.fileName) as myFile:
            for line in myFile:
                fileString.append(line.split())
        singleAnchor = [0]
        dualAnchor = []
        for freqNumber in range(0, self.numberOfFreqs):
            dualAnchor.append(freqNumber)
        dipoleLines = self.__findLines("Electric dipole moment", singleAnchor, 2, 4)
        self.dipoleRaw = self.__toSeparate(fileString, dipoleLines)
        for i in range(0, len(self.dipoleRaw[0])):
            self.dipoles.update({self.dipoleRaw[0][i][0]:float(self.dipoleRaw[0][i][2].replace("D", "E"))})
        alpha1Lines = self.__findLines("Alpha(0;0)", singleAnchor, 1, 8)
        self.alpha1Raw = self.__toSeparate(fileString, alpha1Lines)
        for i in range(0, len(self.alpha1Raw[0])):
            self.alphas[0].update({self.alpha1Raw[0][i][0]:float(self.alpha1Raw[0][i][2].replace("D", "E"))})
        beta1Lines = self.__findLines("Beta(0;0,0)", singleAnchor, 1, 16)
        self.beta1Raw = self.__toSeparate(fileString, beta1Lines)
        for i in range(0, len(self.beta1Raw[0])):
            self.betas[0].update({self.beta1Raw[0][i][0]:float(self.beta1Raw[0][i][2].replace("D", "E"))})        
        gamma1Lines = self.__findLines("Gamma(0;0,0,0)", singleAnchor, 1, 17)  
        self.gamma1Raw = self.__toSeparate(fileString, gamma1Lines)
        for i in range(0, len(self.gamma1Raw[0])):
            self.gammas[0].update({self.gamma1Raw[0][i][0]:float(self.gamma1Raw[0][i][2].replace("D", "E"))}) 
        if self.numberOfFreqs > 0:
            alpha2Lines = self.__findLines("Alpha(-w;w)", dualAnchor, 1, 8)
            self.alpha2Raw = self.__toSeparate(fileString, alpha2Lines)
            self.alphas.append({})
            self.alphas.append({})
            for i in range(0, len(self.alpha2Raw[0])):
                self.alphas[1].update({self.alpha2Raw[0][i][0]:float(self.alpha2Raw[0][i][2].replace("D", "E"))})
                self.alphas[2].update({self.alpha2Raw[1][i][0]:float(self.alpha2Raw[1][i][2].replace("D", "E"))})
            beta2Lines = self.__findLines("Beta(-w;w,0)", dualAnchor, 1, 24)
            self.beta2Raw = self.__toSeparate(fileString, beta2Lines)
            self.betas.append({})
            self.betas.append({})
            for i in range(0, len(self.beta2Raw[0])):
                self.betas[1].update({self.beta2Raw[0][i][0]:float(self.beta2Raw[0][i][2].replace("D", "E"))})
                self.betas[2].update({self.beta2Raw[1][i][0]:float(self.beta2Raw[1][i][2].replace("D", "E"))})   
            gamma2Lines = self.__findLines("Gamma(-w;w,0,0)", dualAnchor, 1, 38)
            self.gamma2Raw = self.__toSeparate(fileString, gamma2Lines)
            self.gammas.append({})
            self.gammas.append({})
            for i in range(0, len(self.gamma2Raw[0])):
                self.gammas[1].update({self.gamma2Raw[0][i][0]:float(self.gamma2Raw[0][i][2].replace("D", "E"))})
                self.gammas[2].update({self.gamma2Raw[1][i][0]:float(self.gamma2Raw[1][i][2].replace("D", "E"))})
            if self.numberOfFreqs > 1:
                self.betas.append({})
                self.betas.append({})
                self.gammas.append({})
                self.gammas.append({})
                beta3Lines = self.__findLines("Beta(-2w;w,w)", dualAnchor, 1, 24)
                self.beta3Raw = self.__toSeparate(fileString, beta3Lines)
                for i in range(0, len(self.beta3Raw[0])):
                    self.betas[3].update({self.beta3Raw[0][i][0]:float(self.beta3Raw[0][i][2].replace("D", "E"))})
                    self.betas[4].update({self.beta3Raw[1][i][0]:float(self.beta3Raw[1][i][2].replace("D", "E"))}) 
                gamma3Lines = self.__findLines("Gamma(-2w;w,w,0)", dualAnchor, 1, 56)
                self.gamma3Raw = self.__toSeparate(fileString, gamma3Lines)
                for i in range(0, len(self.gamma3Raw[0])):
                    self.gammas[3].update({self.gamma3Raw[0][i][0]:float(self.gamma3Raw[0][i][2].replace("D", "E"))})
                    self.gammas[4].update({self.gamma3Raw[1][i][0]:float(self.gamma3Raw[1][i][2].replace("D", "E"))}) 

    def __toSeparate(self, listT, rangePos):
        listF = []
        for x in rangePos:
            listX = []
            for i in range(x[0], x[1]):
                listX.append(listT[i])
            listF.append(listX)
        return listF

    def __findLines(self, lookup, posList, addLines, finished):
        numberListTemp = Find_a_String(self.fileName, lookup).return_numbers_of_line()
        numberListFinal = []
        for number in posList:
            x = numberListTemp[number]+addLines
            listT = [x, x + finished]
            numberListFinal.append(listT)
        return numberListFinal

    def returnDipole(self, component):
        dipoles = {}
        dipoles.update({"Dipole Moment" : self.dipoles[component]})
        return dipoles

    def returnAlpha(self, component):
        alpha = {}
        text = ["Alpha(0;0)", "Alpha(-w;w) w= 1906.4nm", "Alpha(-w;w) w= 1064.1nm"]
        for i in range(0,len(self.alphas)):
            alpha.update({text[i] : self.alphas[i][component]})
        return alpha

    def returnBeta(self, component):
        beta = {}
        text = [
            "Beta(0;0,0)", "Beta(-w;w,0) w= 1906.4nm", "Beta(-w;w,0) w= 1064.1nm", 
            "Beta(-2w;w,w) w= 1906.4nm", "Beta(-2w;w,w) w= 1064.1nm"
        ]
        for i in range(0,len(self.betas)):
            beta.update({text[i] : self.betas[i][component]})
        return beta

    def returnGamma(self, component):
        gamma = {}
        text = [
            "Gamma(0;0,0,0)", "Gamma(-w;w,0,0) w= 1906.4nm", "Gamma(-w;w,0,0) w= 1064.1nm", 
            "Gamma(-2w;w,w,0) w= 1906.4nm", "Gamma(-2w;w,w,0) w= 1064.1nm"
        ]
        for i in range(0,len(self.gammas)):
            gamma.update({text[i] : self.gammas[i][component]})
        return gamma
