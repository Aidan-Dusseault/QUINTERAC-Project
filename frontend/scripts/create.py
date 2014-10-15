
from util import *

def create(accounts, transactions):
	
	accountNumber = raw_input('> ')
	
	if (validAccountNumber(accountNumber, accounts)):
		
		if (not accountExists(accountNumber, accounts)):
			
			accountName = raw_input('> ')
			
			if (validAccountName(accountName)):

				transactions.append("04 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
									" 00000000 " + formatNumber(accountName, 6))

		else:
			print "Error, account already exists."