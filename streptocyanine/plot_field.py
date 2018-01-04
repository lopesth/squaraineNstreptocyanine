#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Python 2.7

Created on 09:27 BRST 01 May 2017

Author: @thiago_o_lopes / lopes.th.o@gmail.com

Resumo
"""

import os, numpy

def transfer_data_from_file_to_list(file, column, pass_or_not):
	list_temp = []
	with open(file) as myFile:
		for num, line in enumerate(myFile, 1):
			if num == 1:
				if pass_or_not == True:
					pass
				else:
					list_temp.append(line.split()[column])
			else:
				list_temp.append(line.split()[column])
	return list_temp

def symmetrize_the_list(list_input, type):
	list_temp = []
	range_num = range(0,len(list_input))
	list_len = 2*len(list_input)-1
	for num in range_num:
		if num == 0:
			pass
		else:
			if type == "inverse":
				list_temp.append((-1)*float(list_input[-num]))
			elif type == "mirror":
				list_temp.append(float(list_input[-num]))
			else:
				text = "The list symmetrization function is not working properly, the type ("+type+") is not recognized"
				raise Exception(text)	
	for num in range_num:
		list_temp.append(float(list_input[num]))
	return list_temp

def print_column_list(file, list_temp, x_type):
	file_to_write = open(file, "w")
	if x_type == "BEA":
		file_to_write.write("%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s\n" %("\'"+x_type+" cs1\'", "\'"+x_type+" cs2\'", "\'"+x_type+" cs3\'", "\'Dipole cs1\'", "\'Dipole cs2\'", "\'Dipole cs3\'", "\'Alpha cs1\'", "\'Alpha cs2\'", "\'Alpha cs3\'", "\'Beta cs1\'", "\'Beta cs2\'", "\'Beta cs3\'", "\'Gamma cs1\'", "\'Gamma cs2\'", "\'Gamma cs3\'"))
	else:
		file_to_write.write("%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s%14s\n" %("\'"+x_type+" cs1\'", "\'"+x_type+" cs2\'", "\'"+x_type+" cs3\'", "\'Dipole cs1\'", "\'Dipole cs2\'", "\'Dipole cs3\'", "\'Alpha cs1\'", "\'Alpha cs2\'", "\'Alpha cs3\'", "\'Beta cs1\'", "\'Beta cs2\'", "\'Beta cs3\'", "\'Gamma cs1\'", "\'Gamma cs2\'", "\'Gamma cs3\'", "\'BEA cs1\'", "\'BEA cs2\'", "\'BEA cs3\'"))
	for line in list_temp:
		for column in line:
			file_to_write.write("%14.6f" %column)
		file_to_write.write("\n")

def plot(file_to_plot, columns_to_plot, colors, key_name, point_type, y_axis, x_axis, name_file_plot, key_position, limits):
	gnuplot_command = "gnuplot -e \'set terminal png transparent size 3300,2500; set tmargin 5; set output \""+name_file_plot+"\"; set ylabel \" \" font \"Arial,65\" offset -10,0,0; set xlabel font \",65\" offset 0,-7,0; set xtics nomirror font \",45\" offset 0,-3,0; set ytics nomirror  offset -1,0,0; set lmargin screen 0.08; set rmargin screen 0.98; set pointsize 10; set border lw 5 lc rgb \"#000000\"; unset key; "
	if limits["limite_x"] == False:
		pass
	else:
		gnuplot_command = gnuplot_command + "set xrange ["+str((limits["limite_x"])[0])+":"+str((limits["limite_x"])[1])+"];"
	if limits["limite_y"] == False:
		pass
	else:
		gnuplot_command = gnuplot_command + "set yrange ["+str((limits["limite_y"])[0])+":"+str((limits["limite_y"])[1])+"];"
	for x in range(0, len(columns_to_plot),1 ):
		if x == 0:
			gnuplot_command = gnuplot_command + "plot"
		else:
			gnuplot_command = gnuplot_command + ","
		gnuplot_command = gnuplot_command +"\""+file_to_plot+"\" using "+str(columns_to_plot.keys()[x])+":"+str(columns_to_plot[columns_to_plot.keys()[x]])+" with points lt rgb \""+colors[x]+"\" "+ str(point_type[x]) +" title \""+key_name[x]+"\""
	gnuplot_command = gnuplot_command + "\'"
	os.popen(gnuplot_command)

level_list = ["level4", "level3", "level2", "level1"]
molecules_list = ["9C", "5C"]
case_list = ["case1", "case2", "case3"]

for molecule in molecules_list:
	for level in level_list:
		dir_home = os.popen("pwd").read().split()[0] + '/' + level
		boa_mulliken_file = dir_home+"/"+level+"_boa_mulliken_file_vs_polar_"+molecule+".txt"
		boa_mayer_file = dir_home+"/"+level+"_boa_mayer_file_vs_polar_"+molecule+".txt"
		boa_wiberg_file = dir_home+"/"+level+"_boa_wiberg_file_vs_polar_"+molecule+".txt"
		bea_file = dir_home+"/"+level+"_bea_vs_polar_"+molecule+".txt"
		bla_file = dir_home+"/"+level+"_bla_vs_polar_"+molecule+".txt"
		beda_file = dir_home+"/"+level+"_beda_vs_polar_"+molecule+".txt"
		bela_file = dir_home+"/"+level+"_bela_vs_polar_"+molecule+".txt"
		boa_mulliken = []
		boa_wiberg = []
		boa_mayer = []
		bla = []
		bea = []
		bela = []
		beda = []
		dipolo= []
		alpha = []
		beta = []
		gamma = []
		field = arange ()
		for case in case_list:
			boa_mulliken_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/BOA/" + case + "/boa_"+case+"_"+molecule+"_mulliken.txt", 1, False), "inverse")
			boa_mulliken.append(boa_mulliken_temp)
			boa_wiberg_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/BOA/" + case + "/boa_"+case+"_"+molecule+"_wiberg.txt", 1, False), "inverse")
			boa_wiberg.append(boa_wiberg_temp)
			boa_mayer_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/BOA/" + case + "/boa_"+case+"_"+molecule+"_mayer.txt", 1, False), "inverse")
			boa_mayer.append(boa_mayer_temp)
			if case == "case1":
				pass
			else:
				bla_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/BOA/" + case + "/"+case+"_"+molecule+"_bla.txt", 1, False), "inverse")
				bla.append(bla_temp)
			bea_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/BOA/" + case + "/qtaim_"+case+"_"+molecule+"_BondEllipticity.txt", 1, False), "inverse")
			bea.append(bea_temp)
			beda_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/BOA/" + case + "/qtaim_"+case+"_"+molecule+"_Rho.txt", 1, False), "inverse")
			beda.append(beda_temp)
			bela_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/BOA/" + case + "/qtaim_"+case+"_"+molecule+"_DelSqRho.txt", 1, False), "inverse")
			bela.append(bela_temp) 
			dipolo_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/polarizabilidades/" + case + "/"+case+"_"+molecule+"_polar.txt", 1 , True), "inverse")
			alpha_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/polarizabilidades/" + case + "/"+case+"_"+molecule+"_polar.txt", 2 , True), "mirror")
			beta_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/polarizabilidades/" + case + "/"+case+"_"+molecule+"_polar.txt", 3 , True), "inverse")
			gamma_temp = symmetrize_the_list(transfer_data_from_file_to_list(dir_home + "/polarizabilidades/" + case + "/"+case+"_"+molecule+"_polar.txt", 4 , True), "mirror")
			dipolo.append(dipolo_temp)
			alpha.append(alpha_temp)
			beta.append(beta_temp)
			gamma.append(gamma_temp)
		print_column_list(boa_mulliken_file, zip(boa_mulliken[0], boa_mulliken[1], boa_mulliken[2], dipolo[0], dipolo[1], dipolo[2], alpha[0], alpha[1], alpha[2], beta[0], beta[1], beta[2], gamma[0], gamma[1], gamma[2], bea[0], bea[1], bea[2]), "BOA")
		print_column_list(boa_mayer_file, zip(boa_mayer[0], boa_mayer[1], boa_mayer[2], dipolo[0], dipolo[1], dipolo[2], alpha[0], alpha[1], alpha[2], beta[0], beta[1], beta[2], gamma[0], gamma[1], gamma[2], bea[0], bea[1], bea[2]), "BOA")
		print_column_list(boa_wiberg_file, zip(boa_wiberg[0], boa_wiberg[1], boa_wiberg[2], dipolo[0], dipolo[1], dipolo[2], alpha[0], alpha[1], alpha[2], beta[0], beta[1], beta[2], gamma[0], gamma[1], gamma[2], bea[0], bea[1], bea[2]), "BOA")
		print_column_list(bea_file, zip(bea[0], bea[1], bea[2], dipolo[0], dipolo[1], dipolo[2], alpha[0], alpha[1], alpha[2], beta[0], beta[1], beta[2], gamma[0], gamma[1], gamma[2]), "BEA")
		print_column_list(bla_file, zip(bla[1], bla[0], bla[1], dipolo[0], dipolo[1], dipolo[2], alpha[0], alpha[1], alpha[2], beta[0], beta[1], beta[2], gamma[0], gamma[1], gamma[2], bea[0], bea[1], bea[2]), "BLA")
		print_column_list(bela_file, zip(bela[0], bela[1], bela[2], dipolo[0], dipolo[1], dipolo[2], alpha[0], alpha[1], alpha[2], beta[0], beta[1], beta[2], gamma[0], gamma[1], gamma[2]), "BELA")
		print_column_list(beda_file, zip(beda[0], beda[1], beda[2], dipolo[0], dipolo[1], dipolo[2], alpha[0], alpha[1], alpha[2], beta[0], beta[1], beta[2], gamma[0], gamma[1], gamma[2]), "BEDA")

		#Plots do BLA
		plot(bla_file, {1:"4", 2:"5", 3:"6"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " (D)", "BLA ( )", bla_file.split('.')[0]+"_dip.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bla_file, {1:"7", 2:"8", 3:"9"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BLA ( )", bla_file.split('.')[0]+"_alfa.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bla_file, {1:"10", 2:"11", 3:"12"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BLA ( )", bla_file.split('.')[0]+"_beta.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bla_file, {1:"13", 2:"14", 3:"15"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BLA ( )", bla_file.split('.')[0]+"_gama.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bla_file, {1:"16", 2:"17", 3:"18"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], "BEA", "BLA ( )", bla_file.split('.')[0]+"_bea.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		#Plots do BOA-Mayer
		plot(boa_mayer_file, {1:"4", 2:"5", 3:"6"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " (D)", "BOA Mayer", boa_mayer_file.split('.')[0]+"_dip.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mayer_file, {1:"7", 2:"8", 3:"9"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Mayer", boa_mayer_file.split('.')[0]+"_alfa.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mayer_file, {1:"10", 2:"11", 3:"12"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Mayer", boa_mayer_file.split('.')[0]+"_beta.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mayer_file, {1:"13", 2:"14", 3:"15"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Mayer", boa_mayer_file.split('.')[0]+"_gama.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mayer_file, {1:"16", 2:"17", 3:"18"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], "BEA", "BOA Mayer", boa_mayer_file.split('.')[0]+"_bea.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		#Plots do BOA-Widberg
		plot(boa_wiberg_file, {1:"4", 2:"5", 3:"6"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " (D)", "BOA Wiberg", boa_wiberg_file.split('.')[0]+"_dip.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_wiberg_file, {1:"7", 2:"8", 3:"9"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Wiberg", boa_wiberg_file.split('.')[0]+"_alfa.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_wiberg_file, {1:"10", 2:"11", 3:"12"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Wiberg", boa_wiberg_file.split('.')[0]+"_beta.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_wiberg_file, {1:"13", 2:"14", 3:"15"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Wiberg", boa_wiberg_file.split('.')[0]+"_gama.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_wiberg_file, {1:"16", 2:"17", 3:"18"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], "BEA", "BOA Wiberg", boa_wiberg_file.split('.')[0]+"_bea.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		#Plots do BOA-Mulliken
		plot(boa_mulliken_file, {1:"4", 2:"5", 3:"6"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " (D)", "BOA Mulliken", boa_mulliken_file.split('.')[0]+"_dip.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mulliken_file, {1:"7", 2:"8", 3:"9"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Mulliken", boa_mulliken_file.split('.')[0]+"_alfa.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mulliken_file, {1:"10", 2:"11", 3:"12"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Mulliken", boa_mulliken_file.split('.')[0]+"_beta.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mulliken_file, {1:"13", 2:"14", 3:"15"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BOA Mulliken", boa_mulliken_file.split('.')[0]+"_gama.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(boa_mulliken_file, {1:"16", 2:"17", 3:"18"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], "BEA", "BOA Mulliken", boa_mulliken_file.split('.')[0]+"_bea.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		#Plots do BEA
		plot(bea_file, {1:"4", 2:"5", 3:"6"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BEA", bea_file.split('.')[0]+"_dip.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bea_file, {1:"7", 2:"8", 3:"9"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], "", "BEA", bea_file.split('.')[0]+"_alfa.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bea_file, {1:"10", 2:"11", 3:"12"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BEA", bea_file.split('.')[0]+"_beta.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bea_file, {1:"13", 2:"14", 3:"15"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BEA", bea_file.split('.')[0]+"_gama.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})

		#Plots do BELA
		plot(bela_file, {1:"4", 2:"5", 3:"6"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BELA", bela_file.split('.')[0]+"_dip.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bela_file, {1:"7", 2:"8", 3:"9"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BELA", bela_file.split('.')[0]+"_alfa.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bela_file, {1:"10", 2:"11", 3:"12"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BELA", bela_file.split('.')[0]+"_beta.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(bela_file, {1:"13", 2:"14", 3:"15"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], "", "BELA", bela_file.split('.')[0]+"_gama.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})

		#Plots do BEDA
		plot(beda_file, {1:"4", 2:"5", 3:"6"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BEDA", beda_file.split('.')[0]+"_dip.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(beda_file, {1:"7", 2:"8", 3:"9"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BEDA", beda_file.split('.')[0]+"_alfa.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(beda_file, {1:"10", 2:"11", 3:"12"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BEDA", beda_file.split('.')[0]+"_beta.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})
		plot(beda_file, {1:"13", 2:"14", 3:"15"}, ["#2E00FF", "#F0000B", "#319500"], ("Series 1", "Series 2", "Series 3"), ["pt 5", "pt 7", "pt 9"], " ", "BEDA", beda_file.split('.')[0]+"_gama.png","horizontal outside center top", {"limite_x":False, "limite_y" : False})


