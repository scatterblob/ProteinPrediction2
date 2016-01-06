#!/usr/bin/python2.7
# Compute Top 10 keys for the given Primary ACC 

import os
import sys
import time
import getopt

# To set
inputKeyFile = ""
outFileName = "countKeywordsDataFile"
homeDir = ""

try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:d:",["help=","ifile=","homeDirectory="])
except getopt.GetoptError:
	print "mapSnap2ToReference.py \n \
			-i <input file - mapped ids> \n \
			-d <homeDirectory>"
	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h","--help"):
		print "mapSnap2ToReference.py \n \
			-i <input file - mapped ids> \n \
			-d <homeDirectory>"
		sys.exit()
	elif opt in ("-i", "--ifile"):
		inputKeyFile = arg
	elif opt in ("-d", "--homeDir"):
		homeDir = arg

# Convert mappedIDToKeywords
out = inputKeyFile + str(time.time())
os.popen("cut -f 2- "+ inputKeyFile +" | tail -n +2 > " + out)

# Dictionary with keywords
keywordsDict = {}
countTotal = 0
file = open(out,'r')

for line in file:
	line = line.replace("\n","")
	lineArray = line.split(";")
	for k in lineArray:
		k = k.strip()
		if len(k) > 0:
			countTotal += 1
			if k in keywordsDict:
				keywordsDict[k] +=1
			else:
				keywordsDict[k] = 1
				

file.close()

# Save counted keys in file
outCountKeysFile  = homeDir +"/aux" + str(time.time()) 
writeFile = open(outCountKeysFile,'w')
for k in keywordsDict:
	a = float(keywordsDict[k])/countTotal
	# print str(len(k)) + " " + k
	writeFile.write(k + "\t" + str(keywordsDict[k]) + "\t" + str("%.6f" % a)+"\n")
writeFile.close()	

outFileName = homeDir + "/" + outFileName + str(time.time()) + ".out"
os.popen("cat "+outCountKeysFile+" | sort -k2 -n | tail -10 > " + outFileName)
os.popen("cat "+outCountKeysFile+" | awk '{s+=$2} END {print \"Others\t\"s\"\t\"s/" + str(countTotal) + "}' >> " + outFileName) 


