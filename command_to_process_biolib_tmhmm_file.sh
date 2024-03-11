#cat /home/sutripa/effector_pipe/biolib_results/TMRs* > mergedTMRs.gff3 | grep "Number of predicted TMRs: 0" mergedTMRs.gff3 | sed "s/ Number.*//g" | sed "s/# //g" > tmp3
grep "Number of predicted TMHs:  0" tmhmm_out.gff3 | sed "s/ Number.*//g" | sed "s/# //g" > tmp3
