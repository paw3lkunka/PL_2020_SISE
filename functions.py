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

    x0, y0 = find0(result)
    xLast = len(puzzle) - 1
    yLast = len(puzzle[0]) - 1

    if direction == 'D':
        if x0 == xLast:
            return "Operation imposable."
        else:
            for i in reversed(range(0,x0)):
                result[i+1][y0] = result[i][y0]
            result[0][y0] = 0
            return result

    elif direction == 'U':
        if x0 == 0:
            return "Operation imposable."
        else:
            for i in range(x0,xLast):
                result[i][y0] = result[i+1][y0]
            result[xLast][y0] = 0
            return result

    elif direction == 'L':
        if y0 == yLast:
            return "Operation imposable."
        else:
            for i in range(x0,yLast):
                result[x0][i] = result[x0][i+1]
            result[x0][yLast] = 0
            return result

    elif direction == 'R':
        if y0 == 0:
            return "Operation imposable."
        else:
            for i in reversed(range(0,y0)):
                result[x0][i+1] = result[x0][i]
            result[x0][0] = 0
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
