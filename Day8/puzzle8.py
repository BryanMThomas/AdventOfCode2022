inputFilePath = "/home/bryanthomas/source/AdventOfCode2022/Day8/input.txt"

# parse input file into 2d array
inputArr = []
for line in open(inputFilePath, "r").readlines():
    tempArr = []
    for number in line:
        if number != "\n":
            tempArr.append(int(number))
    inputArr.append(tempArr)

# Part 1
visibleCount = 0


def traverseUp(x, y, currHeight):
    # traverse up until we hit a number that is greater than or equal to the current height
    # decrement x until we hit the beginning of the column traversing up
    for i in range(x-1, -1, -1):
        if inputArr[i][y] >= currHeight:
            return False
    return True


def traverseDown(x, y, currHeight):
    # traverse down until we hit a number that is greater than or equal to the current height
    for i in range(x+1, len(inputArr)):  # increment x until we hit the end of the column
        if inputArr[i][y] >= currHeight:
            return False
    return True


def traverseLeft(x, y, currHeight):
    # traverse left until we hit a number that is greater than or equal to the current height
    for i in range(y-1, -1, -1):  # decrement y until we hit the beginning of the row traversing left
        if inputArr[x][i] >= currHeight:
            return False
    return True


def traverseRight(x, y, currHeight):
    # traverse right until we hit a number that is greater than or equal to the current height
    # increment y until we hit the end of the row
    for i in range(y+1, len(inputArr[x])):
        if inputArr[x][i] >= currHeight:
            return False
    return True


# traverse each item in 2d array
for x in range(len(inputArr)):  # O(n)
    if x == 0 or x == len(inputArr)-1:
        continue
    for y in range(len(inputArr[x])):
        if y == 0 or y == len(inputArr)-1:
            continue
        # check if item is visible
        currHeight = inputArr[x][y]
        # traverse up, down, left, right
        if (traverseUp(x, y, currHeight)):  # O(x) where n is the length of the row
            visibleCount += 1
        elif (traverseDown(x, y, currHeight)):  # O(x) where n is the length of the row
            visibleCount += 1
        elif (traverseLeft(x, y, currHeight)):  # O(y) where n is the length of the column
            visibleCount += 1
        elif (traverseRight(x, y, currHeight)):  # O(y) where n is the length of the column
            visibleCount += 1
# add permiter as visible
visibleCount += (2*len(inputArr[0]))  # add top and bottom row length
# add left and right row length
visibleCount += (2*len(inputArr[len(inputArr)-1]))
visibleCount -= 4  # subtract 4 because we counted the corners twice
print("PART1: ", visibleCount)

# PART 2


def scoreTop(x, y, currHeight):
    currentScore = 0
    # traverse up until we hit a number that is greater than or equal to the current height
    # decrement x until we hit the beginning of the column traversing up
    for i in range(x-1, -1, -1):
        val = inputArr[i][y]
        if val >= currHeight:  # hit tree we can not see beyond
            currentScore += 1
            return currentScore
        currentScore += 1
    return currentScore  # hit end of grid


def scoreBottom(x, y, currHeight):
    currentScore = 0
    # traverse down until we hit a number that is greater than or equal to the current height
    for i in range(x+1, len(inputArr)):  # increment x until we hit the end of the column
        val = inputArr[i][y]
        if val >= currHeight:  # hit tree we can not see beyond
            currentScore += 1
            return currentScore
        currentScore += 1
    return currentScore  # hit end of grid


def scoreLeft(x, y, currHeight):
    currentScore = 0
    # traverse left until we hit a number that is greater than or equal to the current height
    for i in range(y-1, -1, -1):  # decrement y until we hit the beginning of the row traversing left
        val = inputArr[x][i]
        if val >= currHeight:  # hit tree we can not see beyond
            currentScore += 1
            return currentScore
        currentScore += 1
    return currentScore  # hit end of grid


def scoreRight(x, y, currHeight):
    currentScore = 0
    # traverse right until we hit a number that is greater than or equal to the current height
    # increment y until we hit the end of the row
    for i in range(y+1, len(inputArr[x])):
        val = inputArr[x][i]
        if val >= currHeight:  # hit tree we can not see beyond
            currentScore += 1
            return currentScore
        currentScore += 1
    return currentScore  # hit end of grid


maxScenicScore = 0
for x in range(len(inputArr)):
    if x == 0 or x == len(inputArr)-1:
        continue
    for y in range(len(inputArr[x])):
        if y == 0 or y == len(inputArr)-1:
            continue
        currHeight = inputArr[x][y]
        currScenicScore = scoreTop(x, y, currHeight) * scoreLeft(
            x, y, currHeight) * scoreRight(x, y, currHeight) * scoreBottom(x, y, currHeight)
        maxScenicScore = max(maxScenicScore, currScenicScore)

print("PART2: ", maxScenicScore)
