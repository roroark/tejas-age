#!/usr/bin/python
import sys
import re
from age_config import *
print 'Plotting Graphs.'

#
# Copyright (C) 2000-2005 by Yasushi Saito (yasushi.saito@gmail.com)
#
# Pychart is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any
# later version.
#
# Pychart is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
from pychart import *
from math import log, floor

theme.get_options()

def plot_single_variable(plot_file, y_label, data):
	
	# data = [("a", 24), ("b", 65)]
	maximum_y=0
	scaled_data = data
	for label, value in data:
		maximum_y=max(maximum_y,value)
	global mode
	if mode == 'Relative/':
		tic_interval = 0.2
		regex = r"[^\(]*"
		y_label = 'Normalized ' + re.findall(regex, y_label, re.MULTILINE)[0].strip()
	else:
		tic_interval= int(10 ** floor(log(maximum_y, 10)))

	theme.output_format = "pdf"
	theme.output_file = plot_file
	theme.reinitialize()

	y_min = 0
	y_max = maximum_y * 1.2

	if  mode != 'Relative/' and y_label in ['BP Accuracy (%)', 'Dynamic Coverage (%)', 'L1 Hit Rate (%)']:
		y_min = 80
		y_max = 100
		tic_interval = 5
	# if  mode != 'Relative/' and y_label in ['L2 Hit Rate (%)']:
	# 	y_min = 0
	# 	y_max = 20
	# 	tic_interval = 5



	chart_object.set_defaults(area.T, size = (50 * len(data), 150), y_range = (y_min, y_max),
	                          x_coord = category_coord.T(data, 0))
	chart_object.set_defaults(bar_plot.T, data = data)

	# Draw the 1st graph. The Y upper bound is calculated automatically.
	ar = area.T(x_axis=axis.X(label="Inputs", format="/a-30{}%s"),
            y_axis=axis.Y(label=str(y_label), tic_interval=tic_interval))
	ar.add_plot(bar_plot.T(label=legend_label, cluster=(0, 1)))
	ar.draw()


firstline = True

for mode in ['Absolute/', 'Relative/']:
	with open(extracted_file_path, 'r') as extracted_values:
		for line in extracted_values:
			split_line = line.split(', ')
			header = split_line[0].strip()
			if firstline:
				x_labels =  [x.strip() for x in split_line[1:]]
				firstline = False
			else:
				if header in plot_variables_with_labels.keys():
					row = [float(x.strip()) for x in split_line[1:]]
					y_label = plot_variables_with_labels[header]
					
					scale = 1
					
					# Relative normalized to first entry in row 
					if mode == 'Relative/':
						scale /= row[0]
					elif y_label in ['L1 Hit Rate (%)', 'L2 Hit Rate (%)']:
						scale = 100

					scaled_row = []
					for val in row:
						scaled_row.append(val * scale)
						

					plot_data = zip(x_labels, scaled_row)
					
					plot_file = plots_root + '/' + mode + header   + '.pdf'
					plot_single_variable(plot_file, y_label, plot_data)
					print 'Plotted: ' + mode + header + '.pdf'