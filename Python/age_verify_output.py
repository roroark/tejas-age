#!/usr/bin/python
from age_config import *
from of import TejasOutputFile

# Trace Name , Executable and arguments.
tejas_output_files = []

import csv
with open(input_file_location, 'r') as document:
	for line in document:
		name, executable_with_args = line.split(', ')
		if name.strip()[0] == '#':
			continue
		tejas_output_files.append(output_root + '/' + name.strip() + '.output');


# Extraction of variables to be plotted.

# Read to.py to see what parameters can be extracted.

verify_report = open(verication_report_path, 'w')
errors = False




def lowerbound_check(name, quantity, lower_bound):
	global errors
	if quantity >= lower_bound: 
		verify_report.write(name + ": " + str(quantity) + " [OK]\n")
	else: 
		if errors == False:
			errors = True
			print " [NOT IDEAL]"
		verify_report.write(name + ": " + str(quantity) + " [NON IDEAL]\n")
		print '\033[93m' + 'Warning: ' + '\033[0m' + name + " is " + str(quantity) + " (less than " + str(lower_bound) + ")."

verify_report.write("START OF REPORT\n\n")

for output_file_path in tejas_output_files:
	errors = False;
	output_file = TejasOutputFile(output_file_path)
	print ("Analysing " + output_file_path.split('/')[-1]),

	verify_report.write('File: ' + output_file_path.split('/')[-1] + "\n")
	# Static Coverage Check
	lowerbound_check("Static Coverage", output_file.staticCoverage(), 90)
	lowerbound_check("Dynamic Coverage", output_file.dynamicCoverage(), 95)
	lowerbound_check("BP Accuracy", output_file.dynamicCoverage(), 90)

	verify_report.write("\n");
	if errors == False:
		print " [ALL OK]"

verify_report.write("END OF REPORT")