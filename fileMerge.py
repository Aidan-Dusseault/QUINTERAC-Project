import sys
import os
writeFile = open(sys.argv[2], 'w')
for summary in os.listdir(sys.argv[1]):
  readFile = open(sys.argv[1] + "/" + summary, 'r')
  for line in readFile:
    if line.strip() != "00 000000 000000 00000000 000000000000000":
      writeFile.write(line)

  readFile.close()
writeFile.write("00 000000 000000 00000000 000000000000000")
writeFile.close()