
from util import *

#######
##	This function asks for user input for account numbers for account 1 and 2 
##	before asking for the transfer amount, stopping if the input is illegal. 
##  It appends the transfer transaction to the transaction list.
#######
def transfer(loginType, accounts, deletions, transactions):
    
    accountNumber = raw_input('')

    if(validAccountNumber(accountNumber, accounts)):
        
        if(accountExists(accountNumber, deletions, accounts)):
            
            accountNumber2 = raw_input('')
            
            if(validAccountNumber(accountNumber2, accounts)):
        
				if(accountExists(accountNumber2, deletions, accounts)):

					if (not int(accountNumber) == int(accountNumber2)):

						amountNumber = raw_input('')
						if(validAmountNumber(loginType, amountNumber)):
							transactions.append("03 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber2, 6) + " " + formatNumber(amountNumber, 8) + " 000000000000000")

					else:
						print "Error, both accounts identical."
				else:
					print "Error, account does not exist."
        else:
			print "Error, account does not exist."
