from functions import *
import time

def bfs(puzzle,order):
    start = time.perf_counter()
    createdStates = 1
    parsedStates = 0
    depth = 0
    oldStates = []

    currentStates = [puzzle]
    currentInstructions = [""]

    newStates = []
    newInstructions = []
    
    while True:
        newStatesCount = len(currentStates)
        if newStatesCount > 0:
            for i in range(newStatesCount):
                parsedStates += 1
                if isinstance(currentStates[i],list):    
                    if currentStates[i] not in oldStates:
                        oldStates.append(currentStates[i])
                        if validate(currentStates[i]):
                            return currentInstructions[i], createdStates, parsedStates, depth, (time.perf_counter() - start) * 1000
                        else:
                            for operator in order:
                                createdStates += 0
                                newStates.append(move(currentStates[i],operator))
                                newInstructions.append(currentInstructions[i]+operator)
        else:
            return "Puzzle unsolved.", createdStates, parsedStates, depth
        currentStates = newStates
        currentInstructions = newInstructions
        newStates = []
        newInstructions = []
        depth += 1