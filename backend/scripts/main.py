
import sys

def main(argv):
  accounts = {}
  readAccountsList(argv[0], accounts)
  
  transactionFile = argv[1]
  transactionLines = []
  readFile(transactionFile, transactionLines)
  for line in transactionLines:
    parsedLine = line.split(" ")
      
    if len(parsedLine) < 5 or len(parsedLine) > 5:
      break
      
    transactionType = parsedLine[0]
    accountNumber1 = parsedLine[1]
    accountNumber2 = parsedLine[2]
    amount = int(parsedLine[3])
    accountName = parsedLine[4]
    
    if transactionType == "00":
      break
    elif transactionType == "01":
      deposit(accountNumber1, amount, accounts)
    elif transactionType == "02":
      withdraw(accountNumber1, amount, accounts)
    elif transactionType == "03":
      transfer(accountNumber1, accountNumber2, amount, accounts)
    elif transactionType == "04":
      create(accountNumber1, accountName, accounts)
    elif transactionType == "05":
      delete(accountNumber1, accountName, accounts)

  writeNewMasterFile(argv[2], accounts)
  writeValidAccountsList(argv[3], accounts)


def readAccountsList(filename, accounts):
  
  lines = []
  readFile(filename, lines)
  
  for line in lines:
    parsedLine = line.split(" ")
    if len(parsedLine) < 3 or len(parsedLine) > 3: 
      print "Error: Invalid number of arguments in transaction file."
    else:
      accounts[parsedLine[0]] = [int(parsedLine[1]), parsedLine[2]]
  
#######
##  This function reads the designated file and populates the list.
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
##  This function writes the list of strings to a new file.
#######
def writeNewMasterFile(filename, accounts):

  file = open(filename, 'w+')
  
  temp = accounts.keys()
  temp.sort()
  for key in temp:
  
    accountNumber = key
    accountBalance = str(accounts[key][0])
    accountBalance.rjust(8, '0')
    accountName = accounts[key][1]
  
    file.write(key + " " + accountBalance + " " + accountName + "\n")
    
  file.close() 

def writeValidAccountsList(filename, accounts):

  file = open(filename, 'w+')
  
  for key in accounts.keys():
  
    file.write(key + "\n")
  file.write("000000")
  file.close()   
  
def create(accountNumber, accountName, accounts):
  
  if (not accountNumber in accounts):
    accountList[accountNumber] = [0, accountName]
    return True
    
  return False

def delete(accountNumber, accountName, accounts):
  
  if (accountNumber in accounts):
    
    if (accountList[accountNumber][0] == 0):
      del accountList[accountNumber]
      return True
    
  return False
  
def deposit(accountNumber, amount, accounts):
 
  if (accountNumber in accounts):
    accounts[accountNumber][0] += amount

def withdraw(accountNumber, amount, accounts):
  
  if (accountNumber in accounts):
    accounts[accountNumber][0] -= amount

def transfer(accountNumber1, accountNumber2, amount, accounts):
  
  if (accountNumber1 in accounts and accountNumber1 in accounts):
    
    accounts[accountNumber1][0] -= amount
    accounts[accountNumber2][0] += amount
    
# Call main
if __name__ == "__main__":
  main(sys.argv[1:])