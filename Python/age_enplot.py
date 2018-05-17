#!/usr/bin/python
import sys
from age_config import *

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
with open(extracted_file_path, 'r') as extracted_values:
	for line in extracted_values:
		split_line = line.split(', ')
		header = split_line[0].strip()
		if firstline:
			x_labels= [x.strip() for x in split_line[1:]]
			firstline = False
		else:
			if header == 'LeakageEnergy':
				# Normalised later
				le_data = [float(x.strip()) for x in split_line[1:]]
			elif header == 'DynamicEnergy':
				de_data = [float(x.strip()) for x in split_line[1:]]
			elif header == 'TotalEnergy':
				te_data = [float(x.strip()) for x in split_line[1:]]


data = zip(x_labels, le_data, de_data, te_data)

norm = le_data[0]
max_te = 0
norm_data = []
for x, le, de, te in data:
	norm_data.append((x, le/norm, de/norm, te/norm))
	max_te = max(te/norm, max_te)
data = norm_data

from pychart import *
from math import log, floor
theme.get_options()
theme.output_format = "pdf"
theme.output_file =  plots_root + '/en.pdf'
theme.reinitialize()

chart_object.set_defaults(area.T, size = (40 * len(data), 150), y_range = (0, max_te * 1.2),
                          x_coord = category_coord.T(data, 0))
chart_object.set_defaults(bar_plot.T, data = data)

# Draw the 1st graph. The Y upper bound is calculated automatically.
ar = area.T(x_axis=axis.X(label="Inputs", format="/a-30{}%s"),
        y_axis=axis.Y(label=str("Normalized Energy"), tic_interval=0.2))
ar.add_plot(bar_plot.T(label="Leakage Energy", cluster=(0, 3)),
            bar_plot.T(label="Dynamic Energy", hcol=2, cluster=(1, 3)),
			bar_plot.T(label="Total Energy", hcol=3, cluster=(2, 3)),
            )
ar.draw()

print 'Plotted: en.pdf'