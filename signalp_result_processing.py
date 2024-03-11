import os
import pandas as pd
import sys
import csv
from  pyfaidx import Fasta

"""
This script processes data from a SignalP analysis and retrieves sequences from corresponding protein files.
"""

# Retrieve the total number of command-line arguments passed
n = len(sys.argv)

# Retrieve the basename of the Python script
# print("Name of the python script", sys.argv[0])

# Search for corresponding protein file with the ending of _translated.fna
# arr_txt = [x for x in os.listdir() if x.endswith("_translated.fna")]

data = []
data1 = []

# Extract the basename without the extension .signalp5 from the first argument
basename = (os.path.splitext(sys.argv[1])[0])

# Open and read the SignalP file specified in the first argument,
# create a dictionary with ID as key and Prediction as value
with open(sys.argv[1], "r") as f:
    next(f)
    signalp_file = pd.read_csv(f, header=0, sep="\t")

    ID = (signalp_file.loc[:, '# ID'])
    Prediction = (signalp_file.loc[:, 'Prediction'])

    mydict = dict(zip(ID, Prediction))
    for ID, Prediction in mydict.items():
        if Prediction == 'SP(Sec/SPI)':
            lab = [ID]
            data.append(lab)

# Set the output CSV filename as the input filename without extension
outputFileName = basename + ".csv"
with open(outputFileName, 'w') as f:
    writer = csv.writer(f)

    # Write the data
    writer.writerows(data)

# Retrieve files whose names end with '_translated.fna' in the current working directory
arr_txt = [x for x in os.listdir() if x.endswith('_translated.fna')]
for i in arr_txt:
    b = (os.path.splitext(i)[0])

    # Check if the basename with '_summary' matches the previously extracted basename
    b1 = b + "_summary"
    if b1 == basename:
        genes = Fasta(i)

new_fasta = []
with open(outputFileName) as csv_file:
    for row in csv_file:
        new_fasta.append(">%s\n%s" % (row.strip("\n"), (genes[row.strip("\n")])))
output = basename + '.fa'
with open(output, 'w') as f:
    f.write('\n'.join(new_fasta))
