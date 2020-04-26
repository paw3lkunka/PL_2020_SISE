#!python

import sys
from functions import readPuzzleFile, saveSolution, saveExtra
from bfs import bfs
from dfs import dfs
from astr import astr

strategy = sys.argv[1]
param = sys.argv[2]
puzzleFile = sys.argv[3]
solutionFile = sys.argv[4]
statsFile = sys.argv[5]

if strategy == "bfs":
    function = bfs

elif strategy == "dfs":
    function = dfs

elif strategy == "astr":
    function = astr

else:
    print("Unknown strategy")
    exit()

puzzle = readPuzzleFile(puzzleFile)
solution, proceededStates, visitedStates, depth, time = function(puzzle,param)

print(solution, proceededStates, visitedStates, depth, time)

saveSolution(solutionFile, solution, depth)
saveExtra(statsFile, solution, visitedStates, proceededStates, depth, time)