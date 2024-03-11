#!/bin/bash

# Iterate through all .fna files in the directory
for fna_file in *.fna; do
    # Extract the basename of the fna file
    basename=$(basename "$fna_file" .fna)

    # Write to io_config.yaml
    echo "input_file: [$basename.fna]" > io_config.yaml
    echo "output_file: [$basename.predicted_effector.fasta]" >> io_config.yaml

    #remove pre-existing files, if they exist
    rm "$basename.predicted_effector.fasta" seq_translated.* seq_translated_summary.* tmhmm_out* output.*    
# Run Snakemake
    snakemake --snakefile effector_prediction --core 40
    
    rm -rf $basename    
    mkdir $basename 
    mv "$basename.predicted_effector.fasta" seq_translated.* seq_translated_summary.* tmhmm_out* output.* $basename 

done

