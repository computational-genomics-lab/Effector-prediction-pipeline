import os
import pandas as pd
import sys
import csv
from  pyfaidx import Fasta

# Get a list of files ending with '_summary.fa' in the current working directory
arr_txt = [x for x in os.listdir() if x.endswith('_summary.fa')]

# Iterate through each file in the list
for i in arr_txt:
    # Open the Fasta file
    genes = Fasta(i)

# Create an empty list to store sequences
new_fasta = []

# Open the CSV file
with open("tmp3") as csv_file:
    # Iterate through each row in the CSV file
    for row in csv_file:
        # Retrieve the sequence corresponding to each entry in the CSV file from the Fasta file
        new_fasta.append(">%s\n%s" % (row.strip("\n"), (genes[row.strip("\n")])))

# Write the sequences to an output Fasta file
with open("output.fa", 'w') as f:
    f.write('\n'.join(new_fasta))
