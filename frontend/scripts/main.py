
from login import *
from logout import *

from create import *
from delete import *

from deposit import *
from withdraw import *
from transfer import *

def main():

	loginType = 0

	accounts = []
	accountId = 0
	
	transactions = []

        withdrawals = {}

	while True:
		command = raw_input('> ')
		if (not loginType and command != 'login'):
			print "Error, please login before entering other commands."
		
		elif (loginType and command == 'login'):
			print "You are already logged in."

		elif command == 'login':
			loginType = login(accounts)
			
		elif command == 'logout':
			loginType = logout(transactions)

		elif loginType == 2 and command == 'create':
			print "Error, please use agent mode to create accounts."
			
		elif command == 'create':
			create(accounts, transactions)

		elif command == 'deposit':
			deposit(loginType, accounts, transactions)
			
		else:
			print "Error, command not recognized."
                if loginType == 0:
                        withdrawals = {}
	
if __name__ == "__main__":
	main()
