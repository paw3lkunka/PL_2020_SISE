from functions import *
import time

def dfs(puzzle, order):
    start = time.perf_counter()

    createdStates = 1
    parsedStates = 0
    maxDepth = 0
    oldStates = []

    currentStates = [puzzle]
    currentInstructions = [""]
    currentDepths = [0]
    
    while True:
        if currentStates:
            nextState = currentStates.pop()
            nextInstructions = currentInstructions.pop()
            depth = currentDepths.pop()
            maxDepth = max(depth, maxDepth)
            if isinstance(nextState, list) and (nextState not in oldStates) and (depth < 16):
                oldStates.append(nextState)
                parsedStates += 1
                if validate(nextState):
                    return nextInstructions, createdStates, parsedStates, maxDepth, (time.perf_counter() - start) * 1000 
                else:
                    for operator in reversed(order):
                        createdStates += 0
                        currentStates.append(move(nextState, operator))
                        currentInstructions.append(nextInstructions + operator)
                        currentDepths.append(depth + 1)
        else:
            return "Puzzle unsolved.", createdStates, parsedStates, maxDepth, (time.perf_counter() - start) * 1000 
