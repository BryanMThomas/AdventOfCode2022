from queue import PriorityQueue

inputFile = open("puzzle1Input.txt")
# Read the file into a list
inputList = inputFile.readlines()

currTotal = 0
maxCalories = 0
#priority queue to store the calories of each elf
pq = PriorityQueue()
for i in range(len(inputList)):
    if(inputList[i] == '\n'): #empty line found (new elf)
        maxCalories = max(currTotal, maxCalories) #update max calories
        pq.put(-currTotal) #add to priority queue (negative to make it a max heap)
        currTotal = 0 #reset
    else: #same elf continue to sum
        currTotal += int(inputList[i]) 

top3Sum = (pq.get() + pq.get() + pq.get())*-1 #get the top 3 sum of calories
print("PART1:", maxCalories)
print("PART2:",top3Sum)



