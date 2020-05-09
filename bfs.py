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
                oldStates.append(currentStates[i])
                for operator in order:
                    visitedStates += 1
                    newState = move(currentStates[i], operator)
                    if isinstance(newState,list) and newState not in oldStates:
                        if validate(newState):
                            return currentInstructions[i] + operator, procededStates, visitedStates, depth, (time.perf_counter() - start) * 1000
                        newStates.append(newState)
                        newInstructions.append(currentInstructions[i] + operator)
        else:
            return "Puzzle unsolved.", procededStates, visitedStates, depth, (time.perf_counter() - start) * 1000
            
        currentStates = newStates
        currentInstructions = newInstructions
        newStates = []
        newInstructions = []
        depth += 1