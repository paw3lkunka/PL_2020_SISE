from functions import *
import time

def dfs(puzzle, order):
    start = time.perf_counter()

    createdStates = 1
    parsedStates = 0
    depth = 0
    oldStates = []

    currentStates = [puzzle]
    currentInstructions = [""]
    
    while True:
        if currentStates:
            nextState = currentStates.pop()
            nextInstructions = currentInstructions.pop()
            if isinstance(nextState, list):
                parsedStates += 1
                depth = len(nextInstructions)
                if depth < 10 and nextState not in oldStates:
                    oldStates.append(nextState)
                    if validate(nextState):
                        return nextInstructions, createdStates, parsedStates, depth, (time.perf_counter() - start) * 1000 
                    else:
                        for operator in reversed(order):
                            createdStates += 0
                            currentStates.append(move(nextState, operator))
                            currentInstructions.append(nextInstructions + operator)
        else:
            return "Puzzle unsolved.", createdStates, parsedStates, depth, (time.perf_counter() - start) * 1000 
