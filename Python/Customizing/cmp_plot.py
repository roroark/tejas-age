#!/usr/bin/python
import sys

# Use this file to compare two Tejas versions.

simd_base = '/home/dell/tejas-age'
vanilla_base = '/home/dell/tejas-age-vanilla'

# tb_extract.py, tb_plot.py and hw_plot.py need:
simd_extracted_file_path = simd_base + '/extracted.csv'
vanilla_extracted_file_path = vanilla_base + '/extracted.csv'

quantity = 'LeakageEnergy'
opfile = 'le.pdf'
y_label = 'Leakage Energy (uW)'
y_min = 0
y_max = 800
y_tic = 200
scale = 1000

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




firstline = True
with open(vanilla_extracted_file_path, 'r') as extracted_values:
	for line in extracted_values:
		split_line = line.split(', ')
		header = split_line[0].strip()
		if firstline:
			x_labels= [x.strip() for x in split_line[1:]]
			firstline = False
		else:
			if header == quantity:
				vanilla_sim_data = [float(x.strip()) for x in split_line[1:]]

firstline = True
with open(simd_extracted_file_path, 'r') as extracted_values:
	for line in extracted_values:
		split_line = line.split(', ')
		header = split_line[0].strip()
		if firstline:
			x_labels= [x.strip() for x in split_line[1:]]
			firstline = False
		else:
			if header == quantity:
				simd_sim_data = [float(x.strip()) for x in split_line[1:]]
				


data = zip(x_labels, vanilla_sim_data, simd_sim_data)


x_labels = ['simd_sqrt',
'simd_xor',
'simd_div',
'simd_mul',
'simd_addsub',
'simd_mov',
'simd_cmp',
'simd_permute']

ordered_data = []
first = True
for x1 in x_labels:
	for x_label, vanilla_sim_time, simd_sim_time in data:
		if x1 == x_label:
			ordered_data.append((x_label, vanilla_sim_time/scale, simd_sim_time/scale))

data = ordered_data

from pychart import *
from math import log, floor
theme.get_options()
theme.output_format = "pdf"
theme.output_file =  opfile
theme.reinitialize()

chart_object.set_defaults(area.T, size = (40 * len(data), 150), y_range = (y_min, y_max),
                          x_coord = category_coord.T(data, 0))
chart_object.set_defaults(bar_plot.T, data = data)

# Draw the 1st graph. The Y upper bound is calculated automatically.
ar = area.T(x_axis=axis.X(label="Inputs", format="/a-30{}%s"),
        y_axis=axis.Y(label=str(y_label), tic_interval=y_tic))
ar.add_plot(bar_plot.T(label="Tejas v1.0", cluster=(0, 2)),
			bar_plot.T(label="Tejas-SIMD", hcol=2, cluster=(1, 2)))
ar.draw()

print 'Plotted: ' + opfile