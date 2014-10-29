
def compare(fileName1, fileName2):

	file1 = open(fileName1, 'r')
	text1 = file1.read()
	
	file2 = open(fileName2, 'r')
	text2 = file2.read()

	return text1 == text2

import sys
if (len(sys.argv) < 3):
	sys.exit(2)

testSection = sys.argv[1].split("_")[0]
outDirectory = sys.argv[2]

outputFileNameOriginal = "./tests/"+testSection+"/output/output_"+sys.argv[1]+".txt"
outputFileNameNew = outDirectory+"/"+testSection+"/output/output_"+sys.argv[1]+".txt"

if not compare(outputFileNameOriginal, outputFileNameNew):
	sys.exit(1)

summaryFileNameOriginal = "./tests/"+testSection+"/summary/summary_"+sys.argv[1]+".txt"
summaryFileNameNew = outDirectory+"/"+testSection+"/summary/summary_"+sys.argv[1]+".txt"

if not compare(summaryFileNameOriginal, summaryFileNameNew):
	sys.exit(1)

sys.exit(0)
	
