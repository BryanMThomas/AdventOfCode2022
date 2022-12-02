inputFile = open("input.txt", "r")

###PART 1 ###
score = 0
#lookup dictionaries
opponentDict = {'A':'rock','B':'paper','C':'scissors'}
myDict = {'X':'rock','Y':'paper','Z':'scissors'}
pointsDict = {'rock':1,'paper':2,'scissors':3}

for line in inputFile.readlines(): #each line is one round
    #Map the round input to the rock paper scissors moves
    opponentMove = opponentDict.get(line[0])
    myMove = myDict.get(line[2])

    #score for the shape I selected 
    score += pointsDict.get(myMove)

    #determine outcome of the round
    if opponentMove == myMove: # draw 
        score += 3
    elif (myMove == 'rock' and opponentMove == 'scissors') or (myMove == 'scissors' and opponentMove == 'paper') or (myMove == 'paper' and opponentMove == 'rock'):
    #I win the round
        score += 6
    else: #I lose the round
        score += 0 #Do nothing

print("PART 1:",score) 

###RESET###
#reset the file pointer to the beginning of the file
inputFile.seek(0)
score = 0

###PART 2 ###
outcomeDict = {'X':'Lose','Y':'Draw','Z':'Win'}
outcomePointsDict = {'Win':6,'Draw':3,'Lose':0}
winningMovesDict = {'rock':'paper','scissors':'rock','paper':'scissors'} #{opponentMove:myMove}
losingMovesDict = {'rock':'scissors','scissors':'paper','paper':'rock'} #{opponentMove:myMove}

for line in inputFile.readlines(): #each line is one round
    opponentMove = opponentDict.get(line[0])
    roundOutcome = outcomeDict.get(line[2])

    #score for the outcome of the round
    score += outcomePointsDict.get(roundOutcome) 

    #score for the shape I selected
    if roundOutcome == 'Draw':
        score += pointsDict.get(opponentMove) #Same move as opponent
    elif roundOutcome == 'Win':
        score += pointsDict.get(winningMovesDict.get(opponentMove)) 
    else: #Lose
        score += pointsDict.get(losingMovesDict.get(opponentMove))

print("PART 2:",score)

###END###
inputFile.close()