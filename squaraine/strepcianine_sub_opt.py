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
	'squaraine-H-H-H', 'squaraine-H-H-O', 'squaraine-H-H-OH', 'squaraine-H-NH2-H', 'squaraine-H-NH2-O', 'squaraine-H-NH2-OH',
	'squaraine-H-NMe2-H', 'squaraine-H-NMe2-O', 'squaraine-H-NMe2-OH', 'squaraine-H-OH-H', 'squaraine-H-OH-O', 'squaraine-H-OH-OH',
	'squaraine-H-OMe-H', 'squaraine-H-OMe-O', 'squaraine-H-OMe-OH', 'squaraine-NH2-NH2-H', 'squaraine-NH2-NH2-O', 'squaraine-NH2-NH2-OH',
	'squaraine-NH2-NMe2-H', 'squaraine-NH2-NMe2-O', 'squaraine-NH2-NMe2-OH', 'squaraine-NH2-OMe-H', 'squaraine-NH2-OMe-O', 'squaraine-NH2-OMe-OH',
	'squaraine-NMe2-NMe2-H', 'squaraine-NMe2-NMe2-O', 'squaraine-NMe2-NMe2-OH', 'squaraine-OH-NH2-H', 'squaraine-OH-NH2-O', 'squaraine-OH-NH2-OH',
	'squaraine-OH-NMe2-H', 'squaraine-OH-NMe2-O', 'squaraine-OH-NMe2-OH', 'squaraine-OH-OH-H', 'squaraine-OH-OH-O', 'squaraine-OH-OH-OH',
	'squaraine-OH-OMe-H', 'squaraine-OH-OMe-O', 'squaraine-OH-OMe-OH', 'squaraine-OMe-NMe2-H', 'squaraine-OMe-NMe2-O', 'squaraine-OMe-NMe2-OH',
	'squaraine-OMe-OMe-H', 'squaraine-OMe-OMe-O', 'squaraine-OMe-OMe-OH', 'stilbene-NMe2-OMe-H', 'stilbene-NMe2-OMe-O', 'stilbene-NMe2-OMe-OH'
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
