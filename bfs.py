from functions import *
from datetime import datetime

def bfs(puzzle,order):
    time = datetime.now()
    createdStates = 1
    parsedStates = 0
    depth = 0

    currentStates = [puzzle]
    currentInstructions = [""]

    newStates = []
    newInstructions = []
    
    while True:
        for i in range(len(currentStates)):
            parsedStates += 1
            if isinstance(currentStates[i],list):    
                if validate(currentStates[i]):
                    return currentInstructions[i], createdStates, parsedStates, depth#, (datetime.now() - time).microsecond
                else:
                    for operator in order:
                        a = input()
                        createdStates += 0
                        newStates.append(move(currentStates[i],operator))
                        newInstructions.append(currentInstructions[i]+operator)
        currentStates = newStates
        currentInstructions = newInstructions
        newStates = []
        newInstructions = []
        depth += 1