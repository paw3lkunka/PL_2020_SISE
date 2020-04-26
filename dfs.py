from functions import *
import time

def dfs(puzzle, order):
    start = time.perf_counter()

    createdStates = 1
    parsedStates = 0
    oldStates = []

    currentStates = [puzzle]
    currentInstructions = [""]
    
    while True:
        if currentStates:
            parsedStates += 1
            nextState = currentStates.pop()
            nextInstructions = currentInstructions.pop()
            if isinstance(nextState, list):
                if nextState not in oldStates:
                    oldStates.append(nextState)
                    if validate(nextState)
                        return nextInstructions, createdStates, parsedStates, len(nextInstructions), (time.perf_counter() - start) * 1000 
                    else:
                        for operator in reversed(order):
                            createdStates += 0
                            currentStates.append(move(nextState, operator))
                            currentInstructions.append(nextInstructions + operator)
        else:
            return "Puzzle unsolved.", createdStates, parsedStates, depth
