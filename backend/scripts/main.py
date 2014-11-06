
import sys

#######
##	This function reads input and handles end of file errors.
#######
def input():
	try:
		return raw_input('')
	except EOFError:
		import sys
		sys.exit()


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
def writeFile(filename, lines):
  file = open(filename, 'w+')
  for line in lines:
    file.write(line + "\n")
  file.write("00 000000 000000 00000000 000000000000000")
  file.close() 

def main(argv):
  accounts = []
  readFile(argv[0], accounts)
  

  while True:
		
    transactionFile = input()
    transactionLines = []
    readFile(transactionFile, transactionLines)
    for line in transactionLines:
      parsedLine = line.split(" ")
      
      if len(parsedLine) < 5 or len(parsedLine) > 5:
        break
      
      transactionType = parsedLine[0]
      accountNumber1 = parsedLine[1]
      accountNumber2 = parsedLine[2]
      amount = parsedLine[3]
      name = parsedLine[4]
      print transactionType
      if transactionType == "00":
        print "file end"
        break
      elif transactionType == "01":
        print "deposit"
      elif transactionType == "02":
        print "withdraw"
      elif transactionType == "03":
        print "transfer"
      elif transactionType == "04":
        print "create"
      elif transactionType == "05":
        print "delete"
 
    # Some sort of termination condition?
    
 
# Call main
if __name__ == "__main__":
  main(sys.argv[1:])