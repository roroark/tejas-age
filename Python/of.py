#!/usr/bin/python


# Parameters of relavance:
# Static & Dynamic Coverage
# CISC IPC
# BP Accuracy
# iTLB hitrate
# dTLB hitrate
# I1 hitrate
# L1 hitrate
# L2 hitrate

import re

class TejasOutputFile():
	def __init__(self, output_file_name):
		self.output_file_name = output_file_name

	def extractFromOutput(self, line_identifier, in_line_id = 0, subset = None):
		with open(self.output_file_name) as output_file:
			for line in output_file:
				if line_identifier in line[0:subset]:
					return float(re.findall( r'\d+\.*\d*', line)[in_line_id]);
	

	def dynamicCoverage(self):
		return self.extractFromOutput("Dynamic Coverage	=")

	def staticCoverage(self):
		return self.extractFromOutput("Static coverage		=")

	def IPC(self):
		return self.extractFromOutput("in terms of CISC instructions");

	def clockCyclesTaken(self):
		return self.extractFromOutput("cycles taken	=");
	
	def KIPS(self):
		return self.extractFromOutput("KIPS		in terms of CISC instructions");
	
	def totalEnergy(self):
		# TODO
		return self.extractFromOutput("TotalEnergy", 2, 20);

	def leakageEnergy(self):
		# TODO
		return self.extractFromOutput("TotalEnergy", 0, 20);

	def dynamicEnergy(self):
		# TODO
		return self.extractFromOutput("TotalEnergy", 1, 20);

	def timeTaken(self):
		return self.extractFromOutput("time taken	=");

	def BPAccuracy(self):
		return self.extractFromOutput("branch predictor accuracy	=");

	def L1HR(self):
		return self.extractFromOutput("L1 Hit-Rate\t=", 1);

	def L2HR(self):
		return self.extractFromOutput("L2 Hit-Rate\t=", 1);