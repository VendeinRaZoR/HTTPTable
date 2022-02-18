import random
import string

MAX_ELEMENTS=1000000

def createTable():
    sequence = list(range(1,MAX_ELEMENTS))
    randomSequence = random.sample(sequence,MAX_ELEMENTS-1)
    with open("table.txt",'w') as tableFile:
        for i in range(1,MAX_ELEMENTS-1):
            tableFile.write('#' + str(randomSequence[i]) + ' ' + str(random.choice(range(1,1000000))) + ' ' + random.choice(string.ascii_letters) + '\n')

def getTableBlock(startRow,endRow):
    tableBlock = list()
    tableFile = open("table.txt", 'r')
    currentPointer = 0
    for n,line in enumerate(tableFile):
        if n+1 == startRow-1:
            currentPointer = n+1
            break
    if not currentPointer:
        tableFile.seek(0)
    for i in range(startRow,endRow):
        thisline = tableFile.readline()
        tableBlock.append(thisline)
    tableFile.close()
    return tableBlock
