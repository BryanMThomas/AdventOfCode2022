inputFilePath = "/home/bryanthomas/source/AdventOfCode2022/Day3/input.txt"
inputFile = open(inputFilePath, "r")

def convertCharToPriority(char): # Convert a character to a priority value
    # a =1, b=2, c=3, etc. A=27, B=28, C=29, etc.
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


sum = 0
for line in inputFile.readlines():
    #divide content of line in half
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    for char in compartment1:
        if char in compartment2:
            sum += convertCharToPriority(char)
            break
print("PART1:",sum)

#reset file pointer and sum
inputFile.seek(0)
sum =0 

lines = inputFile.readlines()
linePointer = 0

while linePointer < len(lines):   
    elf1 = lines[linePointer]
    elf2 = lines[linePointer+1]
    elf3 = lines[linePointer+2]
    #find char that is in all 3 lines
    for char in elf1:
        if char in elf2 and char in elf3:
            sum += convertCharToPriority(char)
            break
    linePointer += 3
print("PART2:", sum)
    





