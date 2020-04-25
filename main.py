#!python

import sys
from functions import * 
from bfs import bfs

strategy = sys.argv[1]
param = sys.argv[2]
puzzleFile = sys.argv[3]
solutionFile = sys.argv[4]
statsFile = sys.argv[5]

print("Hello world!")
print(strategy)
print(param)
print(puzzleFile)
print(solutionFile)
print(statsFile)

puzzle = readPuzzleFile(puzzleFile)

print(bfs(puzzle,"LRUD"))