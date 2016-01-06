#!/usr/bin/Python
# Get all keys from .fasta files
import os
import re
import sys
import time
import getopt

# To set
homeDir = ""
inFileName = ""

try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:d:",["help=","ifile=","homeDirectory="])
except getopt.GetoptError:
	print "getKeys.py \n \
			-i <input file - fasta header> \n \
			-d <homeDirectory>"
	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h","--help"):
		print "getKeys.py \n \
			-i <input file - fasta header> \n \
			-d <homeDirectory>"
		sys.exit()
	elif opt in ("-i", "--ifile"):
		inFileName = arg
	elif opt in ("-d", "--homeDir"):
		homeDir = arg

target = open(homeDir+"/keys"+str(time.time())+".fasta",'w')
infile = open(inFileName,'r')
for header in infile:
	if len(header)>0:
		header = header.replace("\n","")
		key = header.split("|")[1]
		target.write(key+" ")
target.close()
infile.close()




 
    



	

