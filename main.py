#!python

import sys
from functions import * 

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

size, puzzle = readPuzzleFile(puzzleFile)

l = move(puzzle,'L')
r = move(puzzle,'R')
u = move(puzzle,'U')
p = move(puzzle,'P')
a = move(puzzle,'A')

print(size)
printPuzzle(puzzle)

print("L")
printPuzzle(l)
print("R")
printPuzzle(r)
print("U")
printPuzzle(u)
print("P")
printPuzzle(p)
print("A")
printPuzzle(a)
