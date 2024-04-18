import os
import pandas as pd
import sys
import csv
from  pyfaidx import Fasta
'''
#command line a kotogulo argumnets pass kora holo
n=len(sys.argv)
#print("total no of arguments passed :", n)

#print("\nName of the python script", sys.argv[0])

#search for corresponding protein file with ending of _translated.fna
#arr_txt = [x for x in os.listdir() if x.endswith("_translated.fna")]

data=[]
data1=[]

#take the basename without extension .signalp5
basename= (os.path.splitext(sys.argv[1])[0])

#1st argument e je signalp file ta deoa holo seta open kore read kora holo; then ID, Prediction coloumn duto dia dictionary create kora holo jekhane ID key ar Prediction value
with open(sys.argv[1],"r") as f:
	#next(f)
	signalp_file=pd.read_csv(f,header=None)
	print(signalp_file.head())
	
	ID=(signalp_file.loc[:,0])
	Prediction=(signalp_file.loc[:,4])
	#print(ID)
	mydict=dict(zip(ID,Prediction))
	for ID,Prediction in mydict.items():
		if Prediction == 'PredHel=0':
			lab=[]
			lab=[ID]
			data.append(lab)
#making the output csv name as the input file name without extension
outputFileName= basename + ".txt"
with open(outputFileName,'w') as f:
	writer=csv.writer(f)
	
	#write the data
	writer.writerows(data)
'''
#current work directory te file gulo jader end '_translated.fna' dia end sei file gulo neoa; singnalp file r corresponding protein file theke
#signal peptide sequence gulo retrieve kora

arr_txt= [ x for x in os.listdir() if x.endswith('_summary.fa')]

for i in arr_txt :
	#b=(os.path.splitext(i)[0])
	#print(b)
	#b1=b + "_tmhmm_result"
	#print(b1)
	#if (b1==basename):
        #print(i)
        genes=Fasta(i)

new_fasta=[]
with open("tmp3") as csv_file:
	#csv_reader=csv.reader(csv_file,delimiter=',')
	for row in csv_file:
		#print(row)
		#print(">%s\n%s" % (row.strip("\n"),(genes[row.strip("\n")])))
		new_fasta.append(">%s\n%s" % (row.strip("\n"),(genes[row.strip("\n")])))
#output=basename + '.fa'
with open("output.fa",'w') as f:
	f.write('\n'.join(new_fasta))
        
        
