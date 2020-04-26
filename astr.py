from functions import move, validate
from functions import printPuzzle
import time

def astr(puzzle, heuristic):        
    if heuristic == "hamm":
        distance = hamming
    
    elif heuristic == "manh":
        distance = manhattan

    else:
        print("Heuristic {} is unknown.".format(heuristic))
        exit()

    def f(state):
        return g(state) + h(state)

    def g(state):
        return distance(puzzle, state)

    def h(state):
        return distance(state,solvedState)
            
    start = time.perf_counter()
    #TODO implement after Nowak's response
    visitedStates = 0
    proceededStates = 0
    maxDepth = 0
    
    oldStates = []

    currentStates = [puzzle]
    currentInstructions = [""]
    currentDistences = [f(puzzle)]
    currentDepths = [0]

    while True:
        
        bestIndex = 0
        for i in range(len(currentStates)):
            if currentDistences[i] < currentDistences[bestIndex]:
                bestIndex = i
        
        if validate(currentStates[bestIndex]):
            return currentInstructions[bestIndex], "unimplemented", "unimplemented", maxDepth, (time.perf_counter() - start) * 1000

        for operator in "LRUD":
            new = move(currentStates[bestIndex], operator)
            if isinstance(new[0], list) and (new not in oldStates):
                currentStates.append(new)
                currentInstructions.append(currentInstructions[bestIndex] + operator)
                currentDistences.append(f(new))
                currentDepths.append(currentDepths[bestIndex]+1)
                maxDepth = max(maxDepth, currentDepths[-1])
        
        oldStates.append(currentStates.pop(bestIndex))
        currentDistences.pop(bestIndex)
        currentInstructions.pop(bestIndex)
        currentDepths.pop(bestIndex)

    return "Puzzle unsolved.", "unimplemented", "unimplemented", maxDepth, (time.perf_counter() - start) * 1000

def hamming(state1, state2):
    value = 0
    for i in range(len(state1)):
        for j in range(len(state1[0])):
            if state1[i][j] != state2[i][j]:
                value += 1
    return value

def manhattan(state1, state2):
    print("Manhattan distance not implemented")
    exit()


solvedState = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,0],
]