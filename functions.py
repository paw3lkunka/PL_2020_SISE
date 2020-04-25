def readPuzzleFile(filename):
    puzzle = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    f = open(filename)

    size = f.readline().rstrip()

    for i in range(4):
        line = f.readline().split()
        for j in range(4):
            puzzle[i][j] = int(line[j])

    return size, puzzle