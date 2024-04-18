#!/bin/bash

# Specify the list of input files
input_files=["contig_1.txt" "contig_2.txt"]

# Loop over each input file and run Snakemake
for input_files in "${input_files[@]}"; do
    echo "Running Snakemake for $input_file"
    
    # Run Snakemake with the current input file
    snakemake --snakefile effector_prediction_new1 --config input_file="$input_file" --cores 30

    # Add any other Snakemake options or parameters as needed
    
    echo "Done with $input_file"
    echo "---------------------------------"
done
