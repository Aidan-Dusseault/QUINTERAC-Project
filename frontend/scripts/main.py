
import sys

from login import *
from logout import *

from create import *
from delete import *

from deposit import *
from withdraw import *
from transfer import *

from util import *

#######
##	This function includes the infinite loop used while the program is running.
##  It processes the input commands.
#######
def main(argv):

	loginType = 0

	accounts = []	
	transactions = []
	withdrawals = {}
	
	if (not len(argv) == 2):
		return
	
	# Infinite loop for receiving input.
	while True:
		
		command = input()
		
		# Disallow any actions until login.
		if (not loginType and command != 'login'):
			print "Error, please login before entering other commands."
		
		# Disallow multiple logins.
		elif (loginType and command == 'login'):
			print "You are already logged in."

		# Execute login
		elif command == 'login':
			loginType = login(accounts, argv[0])
		
		# Execute logout
		elif command == 'logout':
			loginType = logout(transactions, argv[1])

		# Disallow create in retail mode
		elif loginType == 2 and command == 'create':
			print "Error, please use agent mode to create accounts."
			
		# Execute create
		elif command == 'create':
			create(accounts, transactions)
			
		# Disallow delete in retail mode
		elif loginType == 2 and command == 'delete':
			print "Error, please use agent mode to delete accounts."

		# Execute delete
		elif command == 'delete':
			delete(accounts, transactions)
			
		# Execute deposit
		elif command == 'deposit':
			deposit(loginType, accounts, transactions)

		# Execute withdraw
		elif command == 'withdraw':
			withdraw(loginType, accounts, transactions, withdrawals)
			
		# Execute transfer
		elif command == 'transfer':
			transfer(loginType, accounts, transactions)
			
		else:
			print "Error, command not recognized."
                if loginType == 0:
                        withdrawals = {}

# Call main
if __name__ == "__main__":
	main(sys.argv[1:])
