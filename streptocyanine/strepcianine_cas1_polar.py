#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Python 2.7

Created on Mar 21 21:29 BRST 2017

Author: @thiago_o_lopes / lopes.th.o@gmail.com

Optimization of the streptocianine

"""

import numpy, os

molecules = ["13C"]
home = os.popen('pwd').read().split()[0]

for molecule in molecules:
	fields = []
	if molecule == "5C":
		field_temp = numpy.arange(0,146,9.12)
	if molecule == "9C":
		field_temp = numpy.arange(0,88,5.48)
	if molecule == "13C":
		field_temp = numpy.arange(0,91,3)
	for field_elem in range(0, len(field_temp)):
		fields.append(str(round(field_temp[field_elem], 0)).split('.')[0])

	for field in fields:
		name_file = "polar_case1_" + molecule + "_" + field
		file_com = open(home+"/"+name_file + '.com', 'w')
		file_com.write('%schk=%s.chk \n%snprocshared=2 \n%smem=2000mb \n' %("%", name_file,"%", "%") )
		file_com.write('#p polar=(cubic,dcshg) Field=X+%s wb97x/6-31++G** NoSymm\n\nSingle Point (Polar) of the streptocianine_%s molecule in field %s in the X direction\n\n1 1\n' %(field, molecule, field))

		geom_file_name = "opt_case1_"+molecule+"_"+field+".geom"

		with open(home+"/"+molecule+"/geom/"+geom_file_name) as geom_file:
			for line in geom_file:
				file_com.write(line)
			geom_file.close()
		file_com.write('\n\n%s\n\n\n' %("0.0"))
		file_com.close()
