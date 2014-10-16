
#######
##  This function calls writeFile and returns 0.
#######
def logout(transactions):
	# Write the transactions to the summary file.
	writeFile("../summaries/out.txt", transactions)
	return 0
	
#######
##  This function writes the list of strings to a new file.
#######
def writeFile(filename, lines):
	file = open(filename, 'w+')
	for line in lines:
		file.write(line + "\n")
	file.close()
