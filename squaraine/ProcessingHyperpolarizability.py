#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Jan 04 of 2018"

# Description: Script to process Hyperpolarizability data of Squaraine moluecules

#########################################################################################

#########################################################################################
# Impoted Modules
import os, numpy, math
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

# Function Description: Pick up the value of a certain ONL property in G09 output file
def NLO(file_name, start_number, end_number):
	file_temp = [] 
	interval = range(start_number,end_number, 1)
	file = open(file_name, "r")
	for num, line in enumerate(file, 1):
		if num in interval:
			file_temp.append(line)
	file.close()
	for element in range(0, len(file_temp), 1):
		if " Dipole polarizability, Alpha (input orientation)." in file_temp[element]:
			alpha_number = element
		if " First dipole hyperpolarizability, Beta (input orientation)." in file_temp[element]:
			beta_number = element
		if " Second dipole hyperpolarizability, Gamma (input orientation)." in file_temp[element]:
			gama_number = element
	dipole_temp = (file_temp[4]).split()[2]
	dipole = dipole_temp.split('D')[0]+"E"+dipole_temp.split('D')[1]
	alpha_temp = (file_temp[alpha_number+6]).split()[2]
	alpha = alpha_temp.split('D')[0]+"E"+alpha_temp.split('D')[1]
	beta_temp = (file_temp[beta_number+12]).split()[2]
	beta = beta_temp.split('D')[0]+"E"+beta_temp.split('D')[1]
	gama_temp = (file_temp[gama_number+8]).split()[2]
	gama = gama_temp.split('D')[0]+"E"+gama_temp.split('D')[1]
	return float(dipole), float(alpha), float(beta), float(gama)

# Description Main function of the script
if (__name__ == "__main__"):
	directory = "/Users/thiagolopes/Google Drive/squaraine/polar/"
	molecules = [
		"squaraine-H-H", "squaraine-OMe-NMe2", "squaraine-H-NMe2", "squaraine-OMe-OMe", "squaraine-NMe2-NMe2",
		"stilbene_H-H",	"squaraine-OH-OH", "stilbene_O-OH", "squaraine-OMe-H", "stilbene_OH-OH"
	]
	file_target = open(directory+"polar_data.txt", "w")
	file_target.write(
		"{:>20} {:>22} {:>22} {:>22} {:>22}\n" .format(
			"Molecule", "Dipole Moment (D)", "Alpha (10**-24 esu)", "Beta (10**-30 esu)", "Gama (10**-36 esu)"
		)
	)
	for molecule in molecules:
		name_file = directory + "polar_" + molecule + ".log"
		start_number = number_of_a_lookup(name_file, " Electric dipole moment (input orientation):")[0]
		end_number = number_of_a_lookup(name_file, " Dipole orientation:")[0] - 3
		nlo_temp = NLO(name_file, start_number, end_number)
		file_target.write(
			"{:>20} {:>22.7f} {:>22.7f} {:>22.7f} {:>22.7f}\n" .format(
				molecule, nlo_temp[0], nlo_temp[1], nlo_temp[2], nlo_temp[3]
			)
		)

	file_target.close()