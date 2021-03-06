
#######
##	This function reads input and handles end of file errors.
#######
def input():
	try:
		return raw_input('')
	except EOFError:
		import sys
		sys.exit()

#######
##	This function checks to see if a given account is in the accounts list.
#######
def accountExists(account, deletions, accountList):

	accountId = int(account)

	for deletedAccount in deletions:
			
		if accountId == int(deletedAccount):
			return False
	
	for currentAccount in accountList:
			
		if accountId == int(currentAccount):
			return True
			
	return False

#######
##	This function checks to see if a given account is in the accounts list.
#######
def validAccountNumber(account, accountList):
	
	try:
		accountId = int(account)
		if (accountId > 999999 or accountId < 1):
			print 'Error, invalid account number.'
			return False
	except ValueError:
		print 'Error, invalid account number.'
		return False

		
	return True

#######
##	This function checks to see if an account name meets the requirements.
#######	
def validAccountName(accountName):
	
	if (len(accountName) > 15):
		print 'Error, invalid account name.'
		return False

	elif (len(accountName) == 0):
		print 'Error, invalid account name.'
		return False
		
	return True

#######
##	This function checks to see if an amount number is valid and within an acceptable range.
#######	
def validAmountNumber(loginType, amount):
	
	amountInt = 0
	
	try:
		amountInt = int(amount)
	except ValueError:
		print 'Error, invalid amount.'
		return False
	
	if (amountInt < 1):
		print 'Error, invalid amount.'
		return False		
	
	if (loginType == 1):
		if (amountInt > 99999999):
			print 'Error, amount over maximum.'
			return False
	elif (loginType == 2):
		if (amountInt > 100000):
			print 'Error, amount over maximum.'
			return False
			
	return True

#######
##	This function returns a string of a number of given length, padded by zeros on the left.
#######	
def formatNumber(number, length):

	outputString = number.strip()
	return outputString.rjust(length, '0')
	
#######
##	This function returns a string of a number of given length, padded by spaces on the right.
#######	
def formatAccountName(accountName):

	outputString = accountName.strip()
	return outputString.ljust(15, ' ')