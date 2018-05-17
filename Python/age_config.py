# Please make sure no spaces in directories or file names!

base = '/home/dell/tejas-age'
global_config = base + '/config.xml'
input_file_location = base + '/input.csv'

# Note we are setting Tejas
tejas_base = base + '/Tejas'

# Since we use ant to build
tejas_jar = tejas_base + '/jars/tejas.jar'

# File not supported
comm = 'sharedMemory'

# age_simulate.py
output_root = base + '/Reports/ExecutionLogs'
logs_root = base + '/Reports/OutputFiles'

# age_verify_output.py
verication_report_path = base + '/Reports/OutputVerification.txt'

# age_extract.py, age_plot.py and age_plot.py need:
extracted_file_path = base + '/Reports/ExtractedOutput.csv'


# age_plot.py config
plots_root = base + '/Plots'
legend_label="Tejas"

# make sure the labels correspond to the printed values in tb_extract.py
plot_variables_with_labels = {
"IPC": "IPC (s-1)", 
"DynamicCoverage":"Dynamic Coverage (%)",
"ExecutionTimes":"Execution Times (ms)",
"KIPS":"Performance (KIPS)",
"LeakageEnergy":"Leakage Energy (uW)",
"DynamicEnergy":"Dynamic Energy (uW)",
"TotalEnergy":"Total Energy (uW)",
"BranchPredictorAccuracy":"BP Accuracy (%)",
"L1HitRate": 'L1 Hit Rate (%)',
"L2HitRate": 'L2 Hit Rate (%)',
}