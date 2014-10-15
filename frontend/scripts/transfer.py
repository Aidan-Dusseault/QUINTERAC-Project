
from util import *

def transfer(loginType, accounts, transactions):
    
    accountNumber = raw_input('> ')

    if(validAccountNumber(accountNumber, account)):
        
        if(accountExists(accountNumber, accounts)):
            
            accountNumber2 = raw_input('> ')
            
                if(validAccountNumber(accountNumber2, account)):
        
                    if(accountExists(accountNumber2, accounts)):

                        amountNumber = raw_input('> ')
                        
                        if(validAmountNumber(loginType, amountNumber)):
                        
				transactions.append("01 " + formatNumber(accountNumber, 6) + " " + formatNumber(accountNumber, 6) +
                                            " " + formatNumber(amountNumber, 8) + " 000000000000000")
        else:
            print "Error, account does not exist."
