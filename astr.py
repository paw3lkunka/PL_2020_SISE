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
    visitedStates = 0
    proceededStates = 0
    depth = 0
    
    oldStates = []

    currentStates = [puzzle]
    currentInstructions = [""]
    currentDistences = [f(puzzle)]

    while True:
        
        bestIndex = 0
        for i in range(len(currentStates)):
            if currentDistences[i] < currentDistences[bestIndex]:
                bestIndex = i
        
        if validate(currentStates[bestIndex]):
            return currentInstructions[bestIndex], "unimplemented", "unimplemented", "unimplemented", (time.perf_counter() - start) * 1000

        for operator in "LRUD":
            new = move(currentStates[bestIndex], operator)
            if isinstance(new[0], list) and (new not in oldStates):
                currentStates.append(new)
                currentInstructions.append(currentInstructions[bestIndex] + operator)
                currentDistences.append(f(new))
        
        oldStates.append(currentStates.pop(bestIndex))
        currentDistences.pop(bestIndex)
        currentInstructions.pop(bestIndex)                


    print("A* not implemented")
    exit()
    #return instruction, visitedStates, proceededStates, depth, time = (time.perf_counter() - start) * 1000
    return "Puzzle unsolved.", visitedStates, proceededStates, depth, (time.perf_counter() - start) * 1000

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