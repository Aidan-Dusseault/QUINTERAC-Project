
def login(accounts):

	accountType = 0

	loginType = raw_input('> ')

	if (loginType == 'agent'):
		accountType = 1
	elif (loginType == 'retail'):
		accountType = 2
	else:
		print "Error, invalid login type."
		return 0

	if (readAccounts("../accounts/accounts.txt", accounts)):
		return accountType
	else:
		print "Error, invalid accounts list file"
		return 0

def readAccounts(filename, accounts):
	file = open(filename, 'r')
	for line in file:
		accounts.append(line.strip())
	file.close()	
	return True