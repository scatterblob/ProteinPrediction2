#!/usr/bin/Python

# Get all keys from .fasta files
import os
import re

######################################################## Get .fasta Files ##################################################################################################
file = open('/home/g/giurgiu/Dokumente/sem3/protein_prediction/ProteinPrediction2/strong_high_ids','r')
target = open('/home/g/giurgiu/Dokumente/sem3/protein_prediction/ProteinPrediction2/task4/extremeStrongKeyWords/fastaIDs_strong_high.out','w')

for l in file:
	key = (l.split("|"))[1]
	target.write(key+" ")
target.close()