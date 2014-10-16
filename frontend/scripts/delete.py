
from util import *

def delete(accounts, transactions):
	
	accountNumber = raw_input('> ')
	
	if (validAccountNumber(accountNumber, accounts)):
		
		if (accountExists(accountNumber, accounts)):
			
			accountName = raw_input('> ')
			
			if (validAccountName(accountName)):

				transactions.append("05 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
									" 00000000 " + formatNumber(accountName, 6))

		else:
			print "Error, account does not exist."