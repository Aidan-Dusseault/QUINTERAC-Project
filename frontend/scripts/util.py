
def accountExists(account, accountList):

	accountId = int(account)
	
	for currentAccount in accountList:
			
		if account == currentAccount:
			return True
			
	return False

def validAccountNumber(account, accountList):
	
	try:
		accountId = int(account)
	except ValueError:
		return False
		print 'Error, invalid account number.'
		
	return True

def validAccountName(accountName):
	
	if (len(accountName) > 15):
		print 'Error, invalid account name.'
		return False

	elif (len(accountName) == 0):
		print 'Error, invalid account name.'
		return False
		
	return True

def validAmountNumber(loginType, amount):
	
	amountInt = 0
	
	try:
		amountInt = int(amount)
	except ValueError:
		print 'Error, invalid amount.'
		return False
	
	if (amountInt < 0):
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

def formatNumber(number, length):

	outputString = number.strip()
	outputString.rjust(length, '0')
	return outputString
	

def formatAccountName(accountName):

	outputString = accountName.strip()
	outputString.ljust(15, ' ')
	return outputString