from functions import move, validate
import time

def bfs(puzzle,order):
    start = time.perf_counter()
    visitedStates = 0
    procededStates = 0
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
                procededStates += 1
                if isinstance(currentStates[i],list) and currentStates[i] not in oldStates:
                    oldStates.append(currentStates[i])
                    if validate(currentStates[i]):
                        return currentInstructions[i], procededStates, visitedStates, depth, (time.perf_counter() - start) * 1000
                    else:
                        for operator in order:
                            visitedStates += 1
                            newStates.append(move(currentStates[i], operator))
                            newInstructions.append(currentInstructions[i] + operator)
        else:
            return "Puzzle unsolved.", procededStates, visitedStates, depth, (time.perf_counter() - start) * 1000
            
        currentStates = newStates
        currentInstructions = newInstructions
        newStates = []
        newInstructions = []
        depth += 1