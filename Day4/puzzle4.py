inputFilePath = "/home/bryanthomas/source/AdventOfCode2022/Day4/input.txt"
inputFile = open(inputFilePath, "r")



def getSectionRanges(line):
    elf1,elf2 = line.split(",")
    elf1Start,elf1End = elf1.split("-")
    elf2Start,elf2End = elf2.split("-")
    elf1Start = int(elf1Start)
    elf1End = int(elf1End)
    elf2Start = int(elf2Start)
    elf2End = int(elf2End)
    return elf1Start,elf1End,elf2Start,elf2End

containedWithinCount = 0
for line in inputFile.readlines():
    elf1Start, elf1End, elf2Start, elf2End = getSectionRanges(line)
    #check if either elf1 or elf2 is contained within the other
    if elf1Start >= elf2Start and elf1End <= elf2End: #elf1 is contained within elf2
        containedWithinCount += 1
    elif elf2Start >= elf1Start and elf2End <= elf1End: #elf2 is contained within elf1
        containedWithinCount += 1
    
print("PART1:", containedWithinCount)

#reset file pointer
inputFile.seek(0)
overlapCount = 0
for line in inputFile.readlines():
    elf1Start, elf1End, elf2Start, elf2End = getSectionRanges(line)
    #check if either elf1 or elf2 has any overlaps with the other
    if elf1Start <= elf2Start and elf1End >= elf2Start: #elf1 overlaps elf2
        overlapCount += 1
    elif elf2Start <= elf1Start and elf2End >= elf1Start: #elf2 overlaps elf1
        overlapCount += 1
print("PART2:", overlapCount)
