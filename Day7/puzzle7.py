inputFilePath = "/home/bryanthomas/source/AdventOfCode2022/Day7/input.txt"

stack = []
sizes = []


def goLevelUp(): #go up a level in directory
    sizes.append(stack.pop(-1)) #add size of current directory to sizes list
    if len(stack) != 0: #if stack is not empty
        stack[-1] += sizes[-1] #add size of current directory to size of parent directory



for line in open(inputFilePath, "r").readlines():
    inputArr = line.strip().split()

    if inputArr[0] == "$": #command
        if inputArr[1] == "cd": #change directory command
            if inputArr[2] == "..": #go up a level in directory
                goLevelUp()
            else:
                stack.append(0) #go down a level in directory and add a empty size as place holder
    elif inputArr[0] == "dir":
        pass #do nothing for dir command
    else: #file size is given
        fileSize=int(inputArr[0])
        stack[-1] += fileSize #add size of file to current directory size

while stack: #while stack is not empty
    goLevelUp()

#### PART 1 ####
sum1 = 0
for item in sizes:
    if item <= 100000: #if size is less than 100000 add to sum
        sum1+=item
print("PART1:", sum1) 
#### PART 2 ####

#sort sized
sizes.sort()
diskSpace = 70000000
empySpaceNeeded = 30000000
currentUnusedDisk = diskSpace - sizes[(len(sizes)-1)]
sizeToRemove = empySpaceNeeded - currentUnusedDisk

for item in sizes:
    if item >= sizeToRemove:
        print("PART2:", item)
        break