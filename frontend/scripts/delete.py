
from util import *

#######
##	This function asks for user input for account number and account name, stopping if the input is illegal.
##  It appends the delete transaction to the transaction list.
#######
def delete(accounts, transactions):
	
	# Get the account number
	accountNumber = raw_input('> ')
	
	# Check to see if the account number is legal
	if (validAccountNumber(accountNumber, accounts)):
		
		# Check to see if the account exists
		if (accountExists(accountNumber, accounts)):
			
			# Get the account name
			accountName = raw_input('> ')
			
			# Check to see if the account name is legal
			if (validAccountName(accountName)):

				# Add the delete transaction to the transaction list
				transactions.append("05 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
									" 00000000 " + formatAccountName(accountName, 15))

		else:
			print "Error, account does not exist."