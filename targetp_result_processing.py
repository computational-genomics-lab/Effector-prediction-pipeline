import os
import pandas as pd
import sys
import csv
from  pyfaidx import Fasta

# Retrieve command-line arguments
n = len(sys.argv)

# Extract the basename without extension
basename = (os.path.splitext(sys.argv[1])[0])

# Read signalp5 file and create a dictionary with ID as key and Prediction as value
with open(sys.argv[1], "r") as f:
    next(f)
    signalp_file = pd.read_csv(f, header=0, sep="\t")
    ID = (signalp_file.loc[:, '# ID'])
    Prediction = (signalp_file.loc[:, 'Prediction'])
    mydict = dict(zip(ID, Prediction))

    # Filter out signal peptide predictions and store them in 'data' list
    data = []
    for ID, Prediction in mydict.items():
        if Prediction == 'SP':
            lab = [ID]
            data.append(lab)

# Write the filtered data to a CSV file
outputFileName = basename + ".txt"
with open(outputFileName, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Find corresponding protein files ending with '.fa' and retrieve the signal peptide sequences
arr_txt = [x for x in os.listdir() if x.endswith('.fa')]
for i in arr_txt:
    b = (os.path.splitext(i)[0])
    b1 = b + "_summary"
    if b1 == basename:
        genes = Fasta(i)
        new_fasta = []

        # Combine ID from CSV file with corresponding sequence from protein file
        with open(outputFileName) as csv_file:
            for row in csv_file:
                new_fasta.append(">%s\n%s" % (row.strip("\n"), (genes[row.strip("\n")])))

# Write the combined sequences to an output file
output = basename + '_targetp.fa'
with open(output, 'w') as f:
    f.write('\n'.join(new_fasta))

