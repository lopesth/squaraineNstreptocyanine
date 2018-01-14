#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Saturday, 13 January 2018"

''' Description: Multiwfn Output Bond Orders'''
#########################################################################################

class BondOrder(object):
	def __init__(self, fileName, basis):
		self.basis = basis
		self.fileName = fileName
		self.bondOrders = self.takeBondOrders()
	
	def takeBondOrders(self):
		bondOrdersMAP = {}
		fileString = []
		with open(self.fileName) as myFile:
			for num, line in enumerate(myFile):
				fileString.append(line.split())
			numberBlock = int(num / self.basis)
			initRange = 3
			endRange = 3+self.basis
			startPoint = 1
			endPoint = 6
			for block in range(0, numberBlock):
				el1 = 1
				for element in range(initRange, endRange):
					count = 1
					for el2 in range(startPoint, endPoint):
						bondOrdersMAP.update({ str(el1) + " - " + str(el2) : float(fileString[element][count])})
						count += 1
					el1 +=1
				initRange = endRange +1
				endRange = initRange + self.basis
				startPoint = endPoint
				endPoint = startPoint +5
				if endPoint < self.basis+1:
					pass
				else:
					endPoint = self.basis+1
			return bondOrdersMAP
	
	def filter_BO_interest(self, bond):
		bondName = str(bond[0]) + " - " + str(bond[1])
		return self.bondOrders[bondName]
