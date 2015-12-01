#!/usr/bin/Python

# Map SNAP2 Predictions to a given reference proteome
import os
import re
import sys
import time
import getopt

filePath = ""
flagWget = False
homeDir = "~/"
snapFileDir = ""

try:
	opts, args = getopt.getopt(sys.argv[1:],"hwi:d:s:",["help=","ifile=","wget=","directory=","snap2directory="])
except getopt.GetoptError:
	print "mapSnap2ToReference.py \n \
			-i <input file with absolute path> -w[option - file should have .gz extension] \n \
			-d <homeDirectory> \n \
			-s <SNAP2Directory>"
	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h","--help"):
		print 'mapSnap2ToReference.py \n \
			-i <input file with absolute path> -w[option - file should have .gz extension] \n \
			-d <homeDirectory> \n \
			-s <SNAP2Directory>'
		sys.exit()
	elif opt in ("-w", "--wget"):
		flagWget = True
	elif opt in ("-i", "--ifile"):
		filePath = arg
	elif opt in ("-d", "--directory"):
		homeDir = arg
	elif opt in ("-s", "--snap2directory"):
		snapFileDir = arg

# Get Reference Proteome file
fileRefArray = []
if flagWget == True:
	filesRef = os.popen("wget -qO- "+hostDir+" | gunzip").read()
	fileRefArray = filesRef.split('>')
else:
	inFile = open(filePath,'r')
	

dict = {}

# Build Dictionary for the Reference Proteome file

if flagWget == True: # File downloaded via ftp
	for i in fileRefArray:
		myhash = i.split('\n',1)
		if(len(myhash) == 2 and len(myhash[0])>0):
			dict['>'+myhash[0]]=[myhash[1].replace("\n",""),0] 
else: # File read via absolute path
	id = ""
	seq = ""
	for aux in inFile:
		if '>' in aux:
			if len(seq) > 0:
				dict[id]=[seq,0]
			id = aux.replace("\n","")
			seq = ""
		else:
			seq += aux.replace("\n","") 

inFile.close()	
########################## Get .snap2 Files ############################

filesSnap = os.popen("ls -1 "+snapFileDir+" | awk '$1 ~ /snap2/ && $1 ~ /UP0/ {print}'").read()
fileSnapArray = filesSnap.split('\n')

# Map snap2 over Reference Proteome
print "start match"
for i,item in enumerate(fileSnapArray):
	if len(item)>0:
		print i
		myseq = os.popen("cat "+ snapFileDir + "/" + item +" | awk '{print $1}' | uniq |awk '{print substr($1,0,length($1)-1)}' | uniq |awk '{print substr($1,0,1)}' | paste -s -d \"\"").read()
		myseq = myseq.replace("\n","")
		for keySeq in dict:
			if myseq in dict[keySeq][0]:
				dict[keySeq][1] += 1 

######## Print how many sequence matching for .SNAP2 ########

dimRefProteome = len(dict)

# Filter Ref Proteome dict - only the matches will remain

fastaIDArray = filter(lambda x:dict[x][1]>0, dict) # Fasta IDs for the already gemapped sequences
print "Total mapped sequnces: " + str(len(fastaIDArray))
print "Not mapped: " + str(dimRefProteome - len(fastaIDArray))

#### Print into File the mapped reference proteome (only for .SNAP2)#####

target = open(homeDir + '/mappedRefProteome'+str(time.time())+'.fasta','w')
for key in fastaIDArray:
	if dict[key][1]>0:
		target.write(key)
		target.write("\n")
		target.write(dict[key][0])
		target.write("\n")

target.close()


target = open(homeDir + '/mappedRefProteome_headers'+str(time.time())+'.fasta','w')
for key in fastaIDArray:
	target.write(key)
	target.write("\n")

target.close()
print "finally done"


 
    



	

