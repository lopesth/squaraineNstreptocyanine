#########################################################################################
# Python file header
__author__ = "Thiago Lopes"
__GitHubPage__ = "https://github.com/lopesth"
__email__ = "lopes.th.o@gmail.com"
__date__ = "Jan 05 of 2018"

# Description: Python script for pre-optimization of molecules

########################################################################################

import numpy

# List of molecules
molecules = [
	'squaraine-NH2-H-O', 'squaraine-NH2-H-OH', 'squaraine-NH2-OH-O', 'squaraine-NH2-OH-OH', 'squaraine-NH2-OMe-H',
	'squaraine-NH2-OMe-O', 'squaraine-NH2-OMe-OH', 'squaraine-NMe2-H-O', 'squaraine-NMe2-H-OH', 'squaraine-NMe2-NH2-O',
	'squaraine-NMe2-NH2-OH', 'squaraine-NMe2-OH-O', 'squaraine-NMe2-OH-OH', 'squaraine-NMe2-OMe-O', 'squaraine-NMe2-OMe-OH',
	'squaraine-OH-H-O', 'squaraine-OH-H-OH', 'squaraine-OMe-H-O', 'squaraine-OMe-H-OH', 'squaraine-OMe-NH2-O',
	'squaraine-OMe-NH2-OH', 'squaraine-OMe-OH-O', 'squaraine-OMe-OH-OH'
	]

# Work directory
directory = '/Users/thiagolopes/Google Drive/squaraine/'

for molecule in molecules:
	name_file = directory+"pre_opt/pre_opt_" + molecule
	file_com = open(name_file + '.com', 'w')
	file_com.write('%schk=%s.chk \n%snprocshared=6 \n%smem=30000mb \n' %("%", molecule,"%", "%") )
	file_com.write('#p opt nosymm b3lyp/3-21G\n\nPre-Optimization of the %s \n\n0 1\n' %(molecule))
	with open(directory+"pre_opt/geomFiles/"+molecule+'.geom') as geom_file:
		for line in geom_file:
			file_com.write(line)
		geom_file.close()
		file_com.write("\n\n\n")
	file_com.close()
