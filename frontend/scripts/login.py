

def login(loggedIn, accounts):
	
	if (loggedIn):
		print ("You are already logged in.")
		return False

	loginType = raw_input('> ')
		
	if (loginType != 'agent' and loginType != 'retail'):
		print ("Error, invalid login type.")
		return False
	
	if (readAccounts("../accounts/accounts.txt", accounts)):
		return loginType
	else:
		print("Error, invalid accounts list file")
		return False
		
def readAccounts(filename, accounts):
	file = open(filename, 'r')
	for line in file:
		accounts.append(line.strip())
	file.close()	
	return True