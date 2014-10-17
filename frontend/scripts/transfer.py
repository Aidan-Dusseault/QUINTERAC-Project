
from util import *

#######
##	This function asks for user input for account numbers for account 1 and 2 
##	before asking for the transfer amount, stopping if the input is illegal. 
##  It appends the transfer transaction to the transaction list.
#######
def transfer(loginType, accounts, transactions):
    
    accountNumber = raw_input('> ')

    if(validAccountNumber(accountNumber, account)):
        
        if(accountExists(accountNumber, accounts)):
            
            accountNumber2 = raw_input('> ')
            
            if(validAccountNumber(accountNumber2, account)):
        
                if(accountExists(accountNumber2, accounts)):

                    amountNumber = raw_input('> ')
                        
                    if(validAmountNumber(loginType, amountNumber)):
                        
						transactions.append("01 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) + " " + formatNumber(amountNumber, 8) + " 000000000000000")
        else:
            print "Error, account does not exist."
