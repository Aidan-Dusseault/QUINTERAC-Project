
from util import *

#######
##	This function asks for user input for account number and amount, stopping if the input is illegal.
##  It appends the deposit transaction to the transaction list.
#######
def deposit(loginType, accounts, transactions):

	# Get the account number
	accountNumber = raw_input('')
	
	# Check to see if the account number is legal
	if (validAccountNumber(accountNumber, accounts)):

		# Check to see if the account exists
		if (accountExists(accountNumber, accounts)):
		
			# Get the amount number
			amountNumber = raw_input('')
		
			# Check to see if the acmount is legal
			if (validAmountNumber(loginType, amountNumber)):
		
				# Add the deposit transaction to the transaction list
				transactions.append("01 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
					" " + formatNumber(amountNumber, 8) + " 000000000000000")
					
		else:
			print "Error, account does not exist."