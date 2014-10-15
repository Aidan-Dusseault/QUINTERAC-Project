
from util import *

def withdraw(loginType, accounts, transactions, withdrawals):

    if loginType == 1:
        validTotal = 100000
    else:
        validTotal = 999999999

	accountNumber = raw_input('> ')
	
	if (validAccountNumber(accountNumber, accounts)):

		if (accountExists(accountNumber, accounts)):
		
			amountNumber = raw_input('> ')
		
			if (validAmountNumber(loginType, amountNumber)):
                            
                            if(accountNumber not in withdrawals):
                                
                                withdrawals[accountNumber] = 0
                                
                            if(withdrawals[accountNumber] + int(amountNumber) <= validTotal):
		
                                transactions.append("02 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
                                                    " " + formatNumber(amountNumber, 8) + " 000000000000000")
                                withdrawals[accountNumber] += int(amountNumber)

					
		else:
			print "Error, account does not exist."
