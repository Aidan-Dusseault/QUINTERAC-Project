import sys
import os
writeFile = open(sys.argv[1], 'w')
for summary in os.listdir(sys.argv[0]):
    readFile = open(summary, 'r')
    for line in file:
        if line.strip() != "00 000000 000000 00000000 000000000000000":
            writeFile.write(line)
        else:
            readFile.close()
writeFile.write("00 000000 000000 00000000 000000000000000")
