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

puzzle = readPuzzleFile(puzzleFile)

l = move(puzzle,'L')
r = move(puzzle,'R')
u = move(puzzle,'U')
d = move(puzzle,'D')
a = move(puzzle,'A')

print("{}x{}".format(len(puzzle),len(puzzle[0])))
printPuzzle(puzzle)
print()

print("L")
printPuzzle(l)
print()
print("R")
printPuzzle(r)
print()
print("U")
printPuzzle(u)
print()
print("D")
printPuzzle(d)
print()
print("A")
printPuzzle(a)
print()

print(validate(puzzle))