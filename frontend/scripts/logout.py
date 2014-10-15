
def logout(transactions):
	writeFile("../summaries/out.txt", transactions)
	return 0
	
def writeFile(filename, lines):
	file = open(filename, 'w+')
	for line in lines:
		file.write(line + "\n")
	file.close()
