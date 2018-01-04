#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Jan 04 of 2018"

# Description: Script to process the BLA and BOA data of the squaraine molecules

########################################################################################

#########################################################################################
# Impoted Modules
import numpy, os, math

#########################################################################################

# Function Description: Find the number of the line in which a certain pardron appears
def number_of_a_lookup(file_name, lookup):
	positions = []
	file = open(file_name, "r")
	for num, line in enumerate(file, 1):
		if lookup in line:
			positions.append(int(num))
	file.close()
	return positions

# Function Description: Returns the type of the atom and the geometric descriptors of a given atom in the molecule
def take_position(file_name):
	atomic_number = []
	atom_order = []
	atom_x = []
	atom_y = []
	atom_z = []
	lookup1 = 'Input orientation:'
	lookup2 = '---------------------------------------------------------------------'
	file_number = interval_number_of_a_lookup(file_name, lookup1, lookup2)

	file = open(file_name, "rb")
	for num, line in enumerate(file, 1):
		if (num in file_number):
			list_take = line.split()
			atom_order.append(int(list_take[0]))
			atomic_number.append(int(list_take[2]))
			atom_x.append(float(list_take[3]))
			atom_y.append(float(list_take[4]))
			atom_z.append(float(list_take[5]))
	file.close()
    return atom_order, atomic_number, atom_x, atom_y, atom_z

# Function Description: Returns the distance between two points in a Cartesian space
def distance_between_2_points (x1, x2, y1, y2, z1, z2):
	distance = math.sqrt( math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2) + math.pow((z2 - z1), 2) )
	return distance

# Function Description: Returns the bond length between two atoms
def bond_distance(bond_list):
	Bonds_length = {}
	for bond in bond_list:
		atom1 = int(bond.split("-")[0])-1
		atom2 = int(bond.split("-")[1])-1
		distance = distance_between_2_points((atom_coord[2])[atom1], (atom_coord[2])[atom2], (atom_coord[3])[atom1], (atom_coord[3])[atom2], (atom_coord[4])[atom1], (atom_coord[4])[atom2])
		Bonds_length.update({bond : distance})
	return Bonds_length

# Function Description: Calculates the BLA
def BLA_calc(single_bonds, double_bonds):
	value_single = 0
	value_double = 0
	for number in range(0,len(single_bonds), 1):
		value_single = value_single + single_bonds.values()[number]
	for number in range(0,len(double_bonds), 1):
		value_double = value_double + double_bonds.values()[number]
	bla_result = (value_single / len(single_bonds)) - (value_double / len(double_bonds))
	return bla_result

# Function Description: Get the bond orders in the AIMALL output file
def take_bond_order(basis, file_name):
	list_of_bo = []
	rouded_basis = basis
	counter = 0
	while ((rouded_basis + counter) % 5) != 0:
		counter = counter + 1
	rouded_basis = rouded_basis + counter
	for turn in range (0, basis, 1):
		file = open(file_name, "r")
		temp_list = []
		positions = range(4+turn, (rouded_basis/5)*(basis+1)+3 ,basis + 1)
		for num, line in enumerate(file, 1):
			if num in positions:
				temp = line.split()
				for x in range(1, len(temp), 1):
					try:
						temp_list.append(temp[x])
					except Exception as e:
						pass
		list_of_bo.append(temp_list)
		file.close()
	return list_of_bo

# Function Description: Filter the bond orders of interest
def filter_BO_interest(list_bo, bonds):
	bond_orders = []
	for bonds in bonds:
		atom1 = int(bonds.split("-")[0])
		atom2 = int(bonds.split("-")[1])
		bond_orders.append((list_bo[atom1-1])[atom2-1])
	return bond_orders

# Function Description: Take the average of the bond orders in each group
def media_of_bond_goups(list_bo):
	number_of_bonds = len(list_bo)
	bond = 0
	for turn in range(0, number_of_bonds, 1):
		bond = bond + float(list_bo[turn])
	mean = bond / number_of_bonds
	return mean

# Description: Main function of the script
if (__name__ == "__main__"):
    doubleBondIndex = []
    singleBondIndex = []
    directory = "/Users/thiagolopes/Google Drive/squaraine/opt/"
	molecules = [
		"squaraine-H-H", "squaraine-OMe-NMe2", "squaraine-H-NMe2", "squaraine-OMe-OMe", "squaraine-NMe2-NMe2",
		"stilbene_H-H",	"squaraine-OH-OH", "stilbene_O-OH", "squaraine-OMe-H", "stilbene_OH-OH"
	]
    fileTarget = open(directory+"bla_N_boa_data.txt", "w")
    for molecule in molecules:
        fileSourceName = "opt_"+molecule+".log"
        BLA_single_length = bond_distance(BLA_double_index)
		BLA_double_length = bond_distance(BLA_single_index)
