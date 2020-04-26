def readPuzzleFile(filename):

    puzzle = []
    f = open(filename)
    
    size = f.readline()
    rows = int(size[0])
    columns = int(size[2])

    for i in range(rows):
        line = f.readline().split()
        puzzle.append([])
        for j in range(columns):
            puzzle[i].append(int(line[j]))

    return puzzle

def saveSolution(filename, solution, depth):
    f = open(filename, mode='wt')
    length = solutionLength(solution)
    if length != -1:
        print(length)
        f.write(str(length)+"\n")
        f.write(solution)
    else:        
        f.write(str(-1))
    f.close()

def saveExtra(filename, solution, visitedStates, proceededStates, maxRecursionDepth, executionTime):
    f = open(filename, mode='wt')
    f.write("{}\n{}\n{}\n{}\n{:.2f}".format
    (
        solutionLength(solution),
        visitedStates,
        proceededStates,
        maxRecursionDepth,
        executionTime
    ))
    f.close()

def solutionLength(solution):    
    if solution == "Puzzle unsolved.":
        length = -1
        
    else:
        length = len(solution)

    return length

def find0(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return i, j
    return -1

def move(puzzle, direction):
    result = []
    for column in puzzle:
        result.append(column.copy())

    row0, col0 = find0(result)
    xLast = len(puzzle) - 1
    yLast = len(puzzle[0]) - 1

    if direction == 'D':
        if row0 == 0:
            return "Operation imposable."
        else:
            result[row0][col0], result[row0-1][col0] = result[row0-1][col0], result[row0][col0] 
            return result

    elif direction == 'U':
        if row0 == xLast:
            return "Operation imposable."
        else:
            result[row0][col0], result[row0+1][col0] = result[row0+1][col0], result[row0][col0] 
            return result

    elif direction == 'L':
        if col0 == yLast:
            return "Operation imposable."
        else:
            result[row0][col0], result[row0][col0+1] = result[row0][col0+1], result[row0][col0] 
            return result

    elif direction == 'R':
        if col0 == 0:
            return "Operation imposable."
        else:
            result[row0][col0], result[row0][col0-1] = result[row0][col0-1], result[row0][col0] 
            return result
    else:
        return "Direction: " + direction + " is invalid."

def printPuzzle(puzzle):

    if not isinstance(puzzle,list) and not isinstance(puzzle[0],list):
        print(puzzle)

    else:
        for row in puzzle:
            for cell in row:
                print(str(cell).zfill(2) + "  ", end='')
            print()

def validate(puzzle):
    rows = len(puzzle)
    columns = len(puzzle[0])
    for i in range(rows):
        for j in range(columns):
            if puzzle[i][j] != ( 0 if i == rows-1 and j == columns-1 else i * columns + j + 1):
                return False
    return True
