#!python

import sys
from functions import * 
from bfs import bfs

strategy = sys.argv[1]
param = sys.argv[2]
puzzleFile = sys.argv[3]
solutionFile = sys.argv[4]
statsFile = sys.argv[5]

if strategy == "bfs":
    function = bfs

elif strategy == "dfs":
    print("depth-first search not implemented")
    #function = dfs

elif strategy == "astr":
    print("A* not implemented")
    #function = astr

else:
    print("Unknown strategy")
    exit()

puzzle = readPuzzleFile(puzzleFile)
solution, createdStates, parsedStates, depth, time = function(puzzle,param)

print(solution, createdStates, parsedStates, depth, time)

saveSolution(solutionFile, solution, depth)
saveExtra(statsFile, len(solution), parsedStates, createdStates, depth, time)