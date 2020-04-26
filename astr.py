from functions import move, validate
import time

def astr(puzzle, heuristic):    
    start = time.perf_counter()
    visitedStates = 0
    proceededStates = 0
    depth = 0
    
    if heuristic == "hamm":
        distance = hamming
    
    elif heuristic == "manh":
        distance = manhattan

    def f(state):
        return g(state) + h(state)

    def g(state):
        return distance(puzzle, state)

    def h(state):
        return distance(state,solvedState)


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