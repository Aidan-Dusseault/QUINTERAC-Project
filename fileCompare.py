import sys
import os

#######
##  This function compares two files.
##  returns True if their contents are identical.
##  returns False otherwise.
#######
def compare(fileName1, fileName2):

	file1 = open(fileName1, 'r')
	text1 = file1.read()
	
	file2 = open(fileName2, 'r')
	text2 = file2.read()

	return text1 == text2

# Exit if there aren't enough arguments.
if (len(sys.argv) < 3):
	sys.exit(2)

# Test section, eg. create, delete, etc.
testSection = sys.argv[1].split("_")[0]
# Output directory path.
outDirectory = sys.argv[2]

# Get the master test output file.
outputFileNameOriginal = "./tests/"+testSection+"/output/output_"+sys.argv[1]+".txt"
# Get the created test output file.
outputFileNameNew = outDirectory+"/"+testSection+"/output/output_"+sys.argv[1]+".log"

# Get the master summary test output file.
summaryFileNameOriginal = "./tests/"+testSection+"/summary/summary_"+sys.argv[1]+".txt"
# Get the created summary test output file.
summaryFileNameNew = outDirectory+"/"+testSection+"/summary/summary_"+sys.argv[1]+".log"

# Get the location of the test logs.
logFilename = outDirectory+"/"+testSection+"/logs/log_"+sys.argv[1]+".log"
logFile = open(logFilename, 'w')

# Get the location of the summary output file.
superTestlogFilename = outDirectory+"/test_log.log"
superTestlogFile = open(superTestlogFilename, 'a')

# Compare the output and summary files and determine if they failed.
failed = False
if not compare(outputFileNameOriginal, outputFileNameNew) :
	failed = True
if os.path.isfile(summaryFileNameOriginal):
	if not compare(summaryFileNameOriginal, summaryFileNameNew):
		failed = True

# If the test failed, print to console and write to the log file, as well as the master.
if failed:
	print sys.argv[1] + " failed.***************"
	logFile.write(sys.argv[1] + " failed.\n")
	superTestlogFile.write(sys.argv[1] + "\n")
else :
	# If the test passed, print to console and write to log file.
	print sys.argv[1] + " succeeded."
	logFile.write(sys.argv[1] + " succeeded.\n")

superTestlogFile.close()

# Write both output files to the test log.
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

# Write both summary files to the test log.
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

# Return success or failure.
if failed:
	sys.exit(1)
else:
	sys.exit(0)
	
