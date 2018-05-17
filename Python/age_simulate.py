# Do not delete this line. :)
# Do not execute this using the shebang style i.e.:
#!/usr/bin/python
from age_config import *

# Trace Name , Executable and arguments.
tejas_input = {}

import csv
with open(input_file_location, 'r') as document:
	for line in document:
		name, executable_with_args = line.split(', ')
		if name.strip()[0] == '#':
			continue
		tejas_input[name.strip()] = executable_with_args.strip()

import subprocess
import xml.etree.ElementTree as ET

tree = ET.parse(global_config)
root = tree.getroot()


import sys
for input_name in tejas_input:
	# Trace generation mode
	root[0][0].text = 'pin'
	root[0][1].text = 'sharedMemory'
	root[0][2].text = 'false'

	# Incase you want to develop for file method, here's a headstart
	#trace_file = trace_root + '/' + input_name
	#root[0][3].text = trace_file
	# print 'The trace for ' + input_name + ' will be saved as ' + trace_file

	config_file = base + '/Temp/' + input_name + '.xml'
	# This line does not matter for trace generation
	output_file = output_root + '/' + input_name + '.output'
	log_file = logs_root + '/' + input_name + '.log'
	# print 'The output for '+ input_name + ' will be saved as ' + output_file
	tree.write(config_file)

	# Create the Tejas command
	command = 'java -jar ' + tejas_jar + ' ' + config_file + ' ' + output_file + ' ' + tejas_input[input_name]

	# Print or execute it in its own terminal.
	log = open(log_file, 'w')
	print 'Executing: ' + input_name
	print "Realtime log: \033[4m" + log_file + "\033[0m"
	sys.stdout.flush()
	p = subprocess.Popen(command.split(), stdout=log)
	p.wait()
	# p.kill()
	# TODO: stop execution if simulation failed.

	print 'Finished execution.'
	subprocess.call('pkill -9 simd*', shell=True)
