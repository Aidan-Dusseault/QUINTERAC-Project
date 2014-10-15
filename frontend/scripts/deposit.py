
from util import *

def deposit(loginType, accounts, transactions):

	accountNumber = raw_input('> ')
	
	if (validAccountNumber(accountNumber, accounts)):

		if (accountExists(accountNumber, accounts)):
		
			amountNumber = raw_input('> ')
		
			if (validAmountNumber(loginType, amountNumber)):
		
				transactions.append("01 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
					" " + formatNumber(amountNumber, 8) + " 000000000000000")
					
		else:
			print "Error, account does not exist."