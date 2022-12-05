from collections import deque
import pandas as pd

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
                stackMap[stackCounter].append(crateID[1]) #append to the bottom of the stack

#read rest of file 
for line in inputFile:
    if(line[0] != "m"): # continue until start of commands
        continue
    command = line.split(" ")
    quantity = int(command[1])
    fromStack = int(command[3])
    toStack = int(command[5])
    for i in range(quantity):
        stackMap[toStack].appendleft(stackMap[fromStack].popleft()) #move from top of fromStack to top of toStack

#get top item of each stack 
topItems = ""
for i in range(stackCounter):
    topItems += stackMap[i+1][0]
print("PART 1:",topItems)





















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



