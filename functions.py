def readPuzzleFile(filename):
    puzzle = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    f = open(filename)

    size = f.readline().rstrip()

    for i in range(4):
        line = f.readline().split()
        for j in range(4):
            puzzle[i][j] = int(line[j])

    return size, puzzle

def find0(puzzle):
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0:
                return i, j
    return -1

def move(puzzle, direction):
    result = []
    for column in puzzle:
        result.append(column.copy())

    x0, y0 = find0(result)

    if direction == 'D':
        if x0 == 3:
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
            for i in range(x0,3):
                result[i][y0] = result[i+1][y0]
            result[3][y0] = 0
            return result

    elif direction == 'L':
        if y0 == 0:
            return "Operation imposable."
        else:
            for i in range(x0,3):
                result[x0][i] = result[x0][i+1]
            result[x0][3] = 0
            return result

    elif direction == 'R':
        if y0 == 3:
            return "Operation imposable."
        else:
            for i in reversed(range(0,x0)):
                result[x0][i+1] = result[x0][i]
            result[x0][0] = 0
            return result
    else:
        return "Direction: " + direction + " is invalid."

def printPuzzle(puzzle):

    def cell(x,y):
        return str(puzzle[x][y]).zfill(2)

    if not isinstance(puzzle,list) and not isinstance(puzzle[0],list):
        print(puzzle)

    else:
        print("╔══╤══╤══╤══╗")
        print("║{}│{}│{}│{}║".format(cell(0,0),cell(0,1),cell(0,2),cell(0,3)))
        print("╟──┼──┼──┼──╢")
        print("║{}│{}│{}│{}║".format(cell(1,0),cell(1,1),cell(1,2),cell(1,3)))
        print("╟──┼──┼──┼──╢")
        print("║{}│{}│{}│{}║".format(cell(2,0),cell(2,1),cell(2,2),cell(2,3)))
        print("╟──┼──┼──┼──╢")
        print("║{}│{}│{}│{}║".format(cell(3,0),cell(3,1),cell(3,2),cell(3,3)))
        print("╚══╧══╧══╧══╝")
