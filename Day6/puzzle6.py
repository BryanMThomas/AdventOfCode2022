inputFilePath = "/home/bryanthomas/source/AdventOfCode2022/Day6/input.txt"
inputFileString = open(inputFilePath, "r").read()


def findMessageMarker(markerLength):
    rightPointer = 0
    leftPointer = 0
    messageMarker = []
    # 4 is the number of unique characters in the message marker
    while rightPointer < len(inputFileString) and len(messageMarker) < markerLength: 
        if inputFileString[rightPointer] in messageMarker: # found non unique character
            messageMarker = [] #reset message marker
            leftPointer += 1 #increment left pointer
            rightPointer = leftPointer #reset right pointer
        else:
            messageMarker.append(inputFileString[rightPointer]) # add unique character to message marker
            rightPointer += 1 #increment right pointer
    return rightPointer


print("PART1:", findMessageMarker(4))
print("PART2:", findMessageMarker(14))
    
