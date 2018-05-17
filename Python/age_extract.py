#!/usr/bin/python
from age_config import *
from of import TejasOutputFile

print 'Extracting Quantities:'

# Trace Name , Executable and arguments.
tejas_output_files = []
header = ['Quantity']


import csv
with open(input_file_location, 'r') as document:
	for line in document:
		name, executable_with_args = line.split(', ')
		if name.strip()[0] == '#':
			continue
		tejas_output_files.append(output_root + '/' + name.strip() + '.output')
		header.append(name.strip())


# Extraction of variables to be plotted.

# Read to.py to see what parameters can be extracted.

print 'Static Coverage, Dynamic Coverage, IPC, Execution Times, Leakage Energy, Dynamic Energy, Total Energy, BPAccuracy, L1HR, L2HR'

staticCoverages = ['StaticCoverage']
dynamicCoverages = ['DynamicCoverage']
IPCs = ['IPC']
executionTimes = ['ExecutionTimes']
KIPSs = ['KIPS']
leakageEnergys = ['LeakageEnergy']
dynamicEnergys = ['DynamicEnergy']
totalEnergys = ['TotalEnergy']
BPAs = ['BranchPredictorAccuracy']
L1HRs = ['L1HitRate']
L2HRs = ['L2HitRate']

for output_file_path in tejas_output_files:
	output_file = TejasOutputFile(output_file_path)
	
	staticCoverages.append(str(output_file.staticCoverage()))
	dynamicCoverages.append(str(output_file.dynamicCoverage()))
	IPCs.append(str(output_file.IPC()))
	executionTimes.append(str(output_file.timeTaken()))
	KIPSs.append(str(output_file.KIPS()))
	leakageEnergys.append(str(output_file.leakageEnergy()))
	dynamicEnergys.append(str(output_file.dynamicEnergy()))
	totalEnergys.append(str(output_file.totalEnergy()))
	BPAs.append(str(output_file.BPAccuracy()))
	L1HRs.append(str(output_file.L1HR()))
	L2HRs.append(str(output_file.L2HR()))

# Save extracted parameters in extracted.csv
extracted_params = open(extracted_file_path, 'w')
extracted_params.write(", ".join(header) + "\n")
line = ", ".join(staticCoverages)
extracted_params.write(line + "\n")
line = ", ".join(dynamicCoverages)
extracted_params.write(line + "\n")
line = ", ".join(IPCs)
extracted_params.write(line + "\n")
line = ", ".join(executionTimes)
extracted_params.write(line + "\n")
line = ", ".join(KIPSs)
extracted_params.write(line + "\n")
line = ", ".join(leakageEnergys)
extracted_params.write(line + "\n")
line = ", ".join(dynamicEnergys)
extracted_params.write(line + "\n")
line = ", ".join(totalEnergys)
extracted_params.write(line + "\n")
line = ", ".join(BPAs)
extracted_params.write(line + "\n")
line = ", ".join(L1HRs)
extracted_params.write(line + "\n")
line = ", ".join(L2HRs)
extracted_params.write(line + "\n")

print "Extracted CSV Location: " + '\033[4m' + extracted_file_path + '\033[0m'
extracted_params.close()
# call('rm -rf Temp', shell=True)
