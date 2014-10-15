
from login import *

def main():

	accounts = []
	accountId = 0
	loggedIn = False

	while True:
		command = raw_input('> ')
		if command == 'logout':
			break

		elif command == 'login':
			loggedIn = login(loggedIn, accounts)
			
		else:
			print("Error, command not recognized.")
			

	

def getValidAccount(accounts):
	inputAccount = raw_input('> ')
	
	try:
		accountId = int(inputAccount)
	except ValueError:
		print 'Error, invalid account number.'
	
	for currentAccount in accounts:
			
		if inputAccount == currentAccount:
			return accountId
			
	return False
	

			
def writeFile(filename, contents):
	file = open(filename, 'w+')
	file.write(contents)
	file.close()

def readFile(filename):
	file = open(filename, 'r')
	contents = file.read()
	file.close()
	return contents

def compare(inputFileName, outputFileName):
	return readFile(inputFileName) == readFile(inputFileName)
	
if __name__ == "__main__":
	main()