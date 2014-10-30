
#######
##  This function asks the user for the login type ('agent' or'retail') before calling readAccounts.
##  The function returns 0 for failure, 1 for agent login and 2 for retail login.
#######
def login(accounts, filename):

	accountType = 0

	# Get login input
	loginType = raw_input('')

	# Set the login flag
	if (loginType == 'agent'):
		accountType = 1
	elif (loginType == 'retail'):
		accountType = 2
	else:
		print "Error, invalid login type."
		return 0

	# Read the accounts file and return the login type
	if (readAccounts(filename, accounts)):
		return accountType
	else:
		print "Error, invalid accounts list file."
		return 0

#######
##  This function reads the designated accounts file and populates the accounts list.
#######
def readAccounts(filename, accounts):
	try:
		file = open(filename, 'r')
		for line in file:
			accounts.append(line.strip())
		file.close()
	except IOError:
		return False

	return True
