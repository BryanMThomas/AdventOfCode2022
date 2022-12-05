from collections import deque
import copy

inputFilePath = "/home/bryanthomas/source/AdventOfCode2022/Day5/input.txt"
inputFile = open(inputFilePath, "r").readlines()

#dictionary of deques for each column
stackMap = {}

#create deques from the diagram input
for line in inputFile:
    if(line[1].isnumeric()):
        break # end of diagram

    lineIterator = 0
    stackCounter = 0
    while lineIterator < len(line):
        crateID = line[lineIterator:lineIterator+4] #every crate ID takes 4 characters
        lineIterator += 4 
        stackCounter+=1 #stack counter is the column number
        if crateID[0] != " ": #not an empty space
            if stackCounter not in stackMap: #new stack
                stackMap[stackCounter] = deque(crateID[1])
            else: #append to stack 
                stackMap[stackCounter].appendleft(crateID[1]) #append to the bottom of the stack

stackMapPart2 = copy.deepcopy(stackMap) #deep copy for part 2 to modify independently

#read rest of file for commands 
for line in inputFile:
    if(line[0] != "m"): # continue until start of commands
        continue
    command = line.split(" ")
    quantity = int(command[1])
    fromStack = int(command[3])
    toStack = int(command[5])

    ## PART 1
    for i in range(quantity):
        crate = stackMap[fromStack].pop()  #move from top of fromStack
        stackMap[toStack].append(crate) #move to top of toStack
    ## PART 2
    loadingZone = deque()
    for i in range(quantity):
        crate = stackMapPart2[fromStack].pop() #move from top of fromStack 
        loadingZone.append(crate) #move to top of loadingZone
    for i in range(quantity):
        crate = loadingZone.pop() #move from top of loadingZone
        stackMapPart2[toStack].append(crate) #move to top of toStack

#get top item of each stack 
topItems1 = ""
topItems2 = ""
for i in range(stackCounter):
    topItems1 += stackMap[i+1].pop()
    topItems2 += stackMapPart2[i+1].pop()
print("PART 1:",topItems1)
print("PART 2:",topItems2)































# #get crate diagram height
# inputFile = open(inputFilePath, "r")
# diagramHeight = 0
# for line in inputFile.readlines():
#     if(line[1].isnumeric()):
#         break
#     diagramHeight+=1
# #read in diagramHeight number of lines into dataframe using whitespace as delimiter
# inputFile.seek(0)

# #delimeter is any amount of whitepace
# df = pd.read_table(inputFile, sep=, nrows=diagramHeight, header=None, columns = 9)

# #delete all [ and ] from dataframe
# # df = df.replace(to_replace = "[\[\]]", value = "", regex = True)
# print(df)
# deques = []



