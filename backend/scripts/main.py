
import sys

#######
##  This function takes in the filename for the master accounts file and the transaction
##  file as well as the filename for the output master file and the valid accounts list.
##
##  It reads the input files and performs modifications on the account information before
##  writing a new master accounts list and valid accounts list.
#######
def main(argv):

  # Populate the accounts list from the master file.
  accounts = {}
  accountsFile = argv[0]
  readAccountsList(accountsFile, accounts)
  
  # Read the specified transaction file
  transactionFile = argv[1]
  transactionLines = []
  readFile(transactionFile, transactionLines)
  
  # Loop through the lines in the transaction file
  for line in transactionLines:
    parsedLine = line.split(" ")
      
    # stop is line is not properly formated
    if len(parsedLine) < 5 or len(parsedLine) > 5:
      break
    
    # break the line into component information
    transactionType = parsedLine[0]
    accountNumber1 = parsedLine[1]
    accountNumber2 = parsedLine[2]
    amount = int(parsedLine[3])
    accountName = parsedLine[4]
    
  # end of file
    if transactionType == "00":
      break
  
    # depost command detected
    elif transactionType == "01":
      deposit(accountNumber1, amount, accounts)

    # withdraw command detected
    elif transactionType == "02":
      withdraw(accountNumber1, amount, accounts)

    # transfer command detected
    elif transactionType == "03":
      transfer(accountNumber1, accountNumber2, amount, accounts)
    
    # create command detected
    elif transactionType == "04":
      create(accountNumber1, accountName, accounts)
    elif transactionType == "05":
      delete(accountNumber1, accountName, accounts)

  # write the new master accounts file
  outputMasterAccountsFilename = argv[2]
  writeNewMasterFile(outputMasterAccountsFile, accounts)

  # write the new valid accounts file
  outputValidAccountsFilename = argv[3]
  writeValidAccountsList(outputValidAccountsFilename, accounts)

  
#######
##  This function reads the designated file and populates the list of lines.
#######
def readFile(filename, lines):
  try:
    file = open(filename, 'r')
    for line in file:
      lines.append(line.strip())
    file.close()
  except IOError:
    return False

  return True

  
#######
##  This function reads the designated accounts file and and populates the accounts dictionary.
#######
def readAccountsList(filename, accounts):
  
  lines = []
  readFile(filename, lines)
  
  for line in lines:
    parsedLine = line.split(" ")
    if len(parsedLine) < 3 or len(parsedLine) > 3: 
      print "Error: Invalid number of arguments in transaction file."
    else:
      accountNumber = parsedLine[0]
      accountAmount = int(parsedLine[1])
      accountName = parsedLine[2]
      accounts[accountNumber] = [accountAmount, accountName]

    
#######
##  This function adds a new account to the account dictionary if it doesn't already exist.
#######
def create(accountNumber, accountName, accounts):
  
  # check to make sure the account doesn't exist
  if (not accountNumber in accounts):
  
    # create the account
    accountList[accountNumber] = [0, accountName]
    return True

  return False

  
#######
##  This function removes an account from the account dictionary if it exists and has a balance of
##  zero.
#######
def delete(accountNumber, accountName, accounts):
  
  # check to make sure the account exists
  if (accountNumber in accounts):
    
    # check to make sure the balance is zero
    if (accountList[accountNumber][0] == 0):
  
      # remove the account from the dictionary
      del accountList[accountNumber]
      return True
    
  return False

  
#######
##  This function adds a specified amount to an account if it exists.
#######
def deposit(accountNumber, amount, accounts):
 
  # check if account exists
  if (accountNumber in accounts):
    accounts[accountNumber][0] += amount

  
#######
##  This function removes a specified amount from an account if it exists.
#######
def withdraw(accountNumber, amount, accounts):
  
  # check if account exists
  if (accountNumber in accounts):
    accounts[accountNumber][0] -= amount

  
#######
##  This function removes a specified amount from an one account and adds it to a second if
##  both accounts exist.
#######
def transfer(accountNumber1, accountNumber2, amount, accounts):
  
  # check if accounts exist
  if (accountNumber1 in accounts and accountNumber1 in accounts):
    accounts[accountNumber1][0] -= amount
    accounts[accountNumber2][0] += amount

  
#######
##  This function creates the new master accounts file using the currently stored dictionary.
#######
def writeNewMasterFile(filename, accounts):

  file = open(filename, 'w+')
  
  # Sort the accounts by account number
  accountList = accounts.keys()
  accountList.sort()
  
  # Loop through all of the accounts.
  for key in accountList:
  
    # format the output
    accountNumber = key
    accountBalance = str(accounts[key][0])
    accountBalance.rjust(8, '0')
    accountName = accounts[key][1]
  
    # write formatted output to file
    file.write(key + " " + accountBalance + " " + accountName + "\n")
    
  file.close() 

  
#######
##  This function creates the new valid accounts list.
#######
def writeValidAccountsList(filename, accounts):

  file = open(filename, 'w+')
  
  # write all account numbers to the file
  for key in accounts.keys():
    file.write(key + "\n")
  
  file.write("000000")
  file.close()   
  
# Call main
if __name__ == "__main__":
  main(sys.argv[1:])