# Snakemake pipeline for effector protein prediction
This pipeline will predict the effector proteins in a whole genome sequence in following steps:

1. Provide the genome assembly filename (if the snakemake file and the assembly file are in different folder then mention the filepath along with the assembly filename)
2. Prediction of ORF in the given genome assembly using 'getorf' with option 3 which predicts ORF between START and STOP codons of the nucleotides sequences of the whole genome assembly
3. Translation of nucleic acid sequences of the predicted ORF in first frame, forward direction
4. Prediction of the presence of signal peptides in the translated sequences using signalP
5. Extraction of the sequence Ids and the corresponding sequences of the predicted signal peptides from the predicted translated product obtained in step 3
using the script'signalp_result_processing.py'
6. The file with the proteins with the signal peptide will be split in 3 files: xaa, xab and xac
7.
8. Prediction of the topology of both alpha-helical and beta-barrel transmembrane proteins for proteins with predicted signal peptide in 'xaa', 'xab' and 'xac' files
using DeepTMHMM of biolib
9. Merging of TMHMM result files of step 8 and retrieval of the sequence Ids that are without transmembrane region using the script 'command_to_process_biolib_tmhmm_file.sh'
10. Retrieval of the corresponding protein sequences that are without transmembrane region using the code 'tmhmm_result_processing.py' from the predicted translated product obtained in step 3
11. Prediction of the presence of N-terminal presequences: signal peptide (SP), mitochondrial transit peptide (mTP), chloroplast transit peptide (cTP) or thylakoid luminal transit peptide (lTP) using 'targetp' tool in the predicted proteins without transmembrane region found in step 10 and the output will be written with the flag '-mature'
12. Motif-independent prediction of the effector proteins will be performed on the file obtained from step 11 using oomycete-effector-prediction package with the program 'predict_effectors1.py' along with its pathname, for example: '/home/sutripa/software/oomycete-effector-prediction/machine_learning_classification/scripts/predict_effectors1.py'
13. The predicted effector proteins can be classified as RXLR/CRN/WYL effectors using Hidden Markov Model based search algorithm 

# Software/package/tool required to install

1. Python 3
2. Snakemake
3. Emboss
4. signalp
5. biolib/DeepTMHMM
6. targetp
7. signalp_result_processing.py
8. command_to_process_biolib_tmhmm_file.sh
9. tmhmm_result_processing.py
11. 'oomycete-effector-prediction' package
12. hmmsearch

# command to run the pipeline

snakemake --snakefile effector_prediction --core 40
