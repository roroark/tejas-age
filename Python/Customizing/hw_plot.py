#!/usr/bin/python
import sys
from tb_config import *



from_hw_profiling = {
'simd_sqrt': 10021, 
'simd_xor': 6130, 
'simd_mul': 7577, 
'simd_div': 7519, 
'simd_addsub': 7682, 
'simd_mov': 10183, 
'simd_cmp': 3418, 
'simd_permute': 5818,
}

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



# from_hw_profiling = {
# 'simd_sqrt': 7155, 
# 'sisd_sqrt': 23162,
# }


firstline = True
with open(extracted_file_path, 'r') as extracted_values:
	for line in extracted_values:
		split_line = line.split(', ')
		header = split_line[0].strip()
		if firstline:
			x_labels= [x.strip() for x in split_line[1:]]
			firstline = False
		else:
			if header in 'ExecutionTimes':
				# Normalised later
				sim_data = [float(x.strip()) for x in split_line[1:]]
				# norm_sim_data = [sim_data[x]/sim_data[0] for x in xrange(0, len(sim_data))]
				hw_data = [float(from_hw_profiling[x_label]) for x_label in x_labels]
				# norm_hw_data = [hw_data[x]/hw_data[0] for x in xrange(0, len(hw_data))]
				# data = zip(x_labels, norm_sim_data, norm_hw_data)
				data = zip(x_labels, sim_data, hw_data)


# x_labels = [
# 'sisd_sqrt',
# 'simd_sqrt',
# ]
x_labels = [
'simd_sqrt',
'simd_xor',
'simd_div',
'simd_mul',
'simd_addsub',
'simd_mov',
'simd_cmp',
'simd_permute',
]

ordered_data = []
first = True
for x1 in x_labels:
	for x2, sw, hw in data:
		if x1 == x2:
			if first:
				sw_norm = sw
				hw_norm = hw				
				first = False;
			ordered_data.append((x2, sw/sw_norm, hw/hw_norm))

data = ordered_data

from pychart import *
from math import log, floor
theme.get_options()
theme.output_format = "pdf"
theme.output_file =  plots_root + '/hw.pdf'
theme.reinitialize()

chart_object.set_defaults(area.T, size = (40 * len(data), 150), y_range = (0, 1.2),
                          x_coord = category_coord.T(data, 0))
chart_object.set_defaults(bar_plot.T, data = data)

# Draw the 1st graph. The Y upper bound is calculated automatically.
ar = area.T(x_axis=axis.X(label="Inputs", format="/a-30{}%s"),
        y_axis=axis.Y(label=str("Normalized Execution Time"), tic_interval=0.1))
ar.add_plot(bar_plot.T(label="Tejas-SIMD", cluster=(0, 2)),
            bar_plot.T(label="Sandy Bridge", hcol=2, cluster=(1, 2)),)
ar.draw()

print 'Plotted: hw.pdf'