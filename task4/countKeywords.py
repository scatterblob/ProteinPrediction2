#!/usr/bin/Python
# Compute Top 10 keys for the given Primary ACC 

import os
import sys
import time

# To set
inputKeyFile = "mappedIDToKeywords.tab"
outFileName = "countKeywordsDataFile.out"

try:
 	opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile=","help="])
except getopt.GetoptError:
 	print 'getKeys.py -i <keysFile> -o <outTop10File>'
 	sys.exit(2)
for opt, arg in opts:
	if opt in ("-h","--help"):
    	print 'test.py -i <keysFile> -o <outTop10File>'
    	sys.exit()
	elif opt in ("-i", "--ifile"):
    	inputKeysFile = arg
	elif opt in ("-o", "--ofile"):
		outFileName = arg

# Convert mappedIDToKeywords
out = inputKeyFile + str(time.time())
os.popen("cut -f 2- "+ inputKeyFile +" | tail -n +2 > " + out)

# Dictionary with keywords
keywordsDict = {}

file = open(out,'r')

for line in file:
	lineArray = line.split(";")
	for k in lineArray:
		print k
		if len(k) > 0:
			if k in keywordsDict:
				keywordsDict[k] +=1
			else:
				keywordsDict[k] = 1

file.close()

# Save counted keys in file
outCountKeysFile  = inputKeyFile + str(time.time()) 
writeFile = open(outCountKeysFile,'w')
for k in keywordsDict:
	writeFile.write(k+"\t"+str(keywordsDict[k])+"\n")

writeFile.close()	

os.system("cat "+outCountKeysFile+" | sort -k2 -n | tail -10 > " + outFileName)
os.system("cat"+outCountKeysFile+" | awk '{s+=$2} END {print \"Others\t\"s}' >>" + outFileName) 



