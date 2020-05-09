from functions import move,validate
import time

def dfs(puzzle, order):
    maxAcceptableDepth = 26

    start = time.perf_counter()
    visitedStates = 0
    procededStates = 0
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
            oldStates.append(nextState)
            procededStates += 1
            for operator in reversed(order):
                visitedStates += 1
                newState = move(nextState, operator)
                if isinstance(newState, list) and (depth < maxAcceptableDepth):                    
                    if validate(newState):
                        return nextInstructions + operator, procededStates, visitedStates, maxDepth, (time.perf_counter() - start) * 1000 
                    currentStates.append(newState)
                    currentInstructions.append(nextInstructions + operator)
                    currentDepths.append(depth + 1)

        else:
            return "Puzzle unsolved.", procededStates, visitedStates, maxDepth, (time.perf_counter() - start) * 1000 