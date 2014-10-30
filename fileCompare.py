import sys
import os

def compare(fileName1, fileName2):

	file1 = open(fileName1, 'r')
	text1 = file1.read()
	
	file2 = open(fileName2, 'r')
	text2 = file2.read()

	return text1 == text2
	
if (len(sys.argv) < 3):
	sys.exit(2)

testSection = sys.argv[1].split("_")[0]
outDirectory = sys.argv[2]

outputFileNameOriginal = "./tests/"+testSection+"/output/output_"+sys.argv[1]+".txt"
outputFileNameNew = outDirectory+"/"+testSection+"/output/output_"+sys.argv[1]+".txt"

summaryFileNameOriginal = "./tests/"+testSection+"/summary/summary_"+sys.argv[1]+".txt"
summaryFileNameNew = outDirectory+"/"+testSection+"/summary/summary_"+sys.argv[1]+".txt"

logFileName = outDirectory+"/"+testSection+"/logs/log_"+sys.argv[1]+".txt"
logFile = open(logFileName, 'w')

failed = False
if not compare(outputFileNameOriginal, outputFileNameNew) :
	failed = True

if os.path.isfile(summaryFileNameOriginal):
	if not compare(summaryFileNameOriginal, summaryFileNameNew):
		failed = True

	
if failed:
	print sys.argv[1] + " failed."
	logFile.write(sys.argv[1] + " failed.\n")
else :
	print sys.argv[1] + " suceeded.\n"
	logFile.write(sys.argv[1] + " suceeded.\n")
	
logFile.write("_______OUTPUT___FILE________\n")
outputFileOriginal = open(outputFileNameOriginal, 'r')
outputFileOriginalText = outputFileOriginal.read()
logFile.write("\n----------EXPECTED----------\n")
logFile.write(outputFileOriginalText)
outputFileNew = open(outputFileNameNew, 'r')
outputFileNewText = outputFileNew.read()	
logFile.write("\n----------OBSERVED----------\n")
logFile.write(outputFileNewText)
outputFileOriginal.close()
outputFileNew.close()

if os.path.isfile(summaryFileNameOriginal):
	logFile.write("\n_______SUMMARY__FILE________\n")
	summaryFileOriginal = open(summaryFileNameOriginal, 'r')
	summaryFileOriginalText = summaryFileOriginal.read()
	logFile.write("\n----------EXPECTED----------\n")
	logFile.write(summaryFileOriginalText)
	summaryFileNew = open(summaryFileNameNew, 'r')
	summaryFileNewText = summaryFileNew.read()	
	logFile.write("\n----------OBSERVED----------\n")
	logFile.write(summaryFileNewText)
	summaryFileOriginal.close()
	summaryFileNew.close()	

logFile.close()

sys.exit(0)
	
