
from util import *

#######
##	This function asks for user input for account number and amount, stopping if the input is illegal.
##  It appends the withdraw transaction to the transaction list.
#######
def withdraw(loginType, accounts, transactions, withdrawals):

	# Set the acceptable limits for withdrawing.
    if loginType == 1:
        validTotal = 100000
    else:
        validTotal = 999999999

	# Get the account number
	accountNumber = raw_input('')
	
	# Check to see if the number is legal
	if (validAccountNumber(accountNumber, accounts)):

		# Check to see if the account exists
		if (accountExists(accountNumber, accounts)):
		
			# Get the withdraw amount
			amountNumber = raw_input('')
		
			# Check to see the amount is legal
			if (validAmountNumber(loginType, amountNumber)):
                            
							# If the account number has not made any withdrawals, add it to the dictionary
                            if(accountNumber not in withdrawals):
                                withdrawals[accountNumber] = 0
                                
							# Check if the sum total of withdrawals is legal
                            if(withdrawals[accountNumber] + int(amountNumber) <= validTotal):
		
								# Add the transaction and update the dictionary
                                transactions.append("02 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
                                                    " " + formatNumber(amountNumber, 8) + " 000000000000000")
                                withdrawals[accountNumber] += int(amountNumber)
		
		else:
			print "Error, account does not exist."
