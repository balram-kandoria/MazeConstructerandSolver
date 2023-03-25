import random

mazeWidth = 75
mazeLength = 75
defaultWall = 3


def output_image(filename, Puzzle):
    from PIL import Image, ImageDraw
    cell_size = 40

    # Create a blank canvas
    img = Image.new(
        "RGBA",
        (mazeWidth * cell_size, mazeLength * cell_size),
        "black"
    )
    draw = ImageDraw.Draw(img)

    # solution = self.solution[1] if self.solution is not None else None
    for i in range(mazeWidth):
        # input("Prompt")
        for j in range(mazeLength):

            # Set Border Visual
            if Puzzle[i][j][0] == 1:
                fill = (40, 40, 40)

            # Set Path Visual
            elif Puzzle[i][j][0] == 0:
                fill = (255, 255, 255)

            # Set Starting Point Visual
            elif Puzzle[i][j][0] == 2:
                fill = (124, 252, 0)

            # Set Path Visual
            elif Puzzle[i][j][0] == 3:
                fill = (0, 0, 255)

            # Set Path Visual
            elif Puzzle[i][j][0] == 4:
                fill = (255, 191, 0)

            # Set Ending Point Visual
            elif Puzzle[i][j][0] == 5:
                fill = (255, 0, 0)

            # Empty cell

            # Draw cell
            # if i != mazeWidth-1 or j != mazeLength-1:
            topBorder = Puzzle[i][j][1]
            bottomBorder = Puzzle[i][j][2]
            rightBorder = Puzzle[i][j][4]
            leftBorder = Puzzle[i][j][3]
            draw.rectangle(([(i * cell_size + rightBorder, j * cell_size + topBorder), ((
                i + 1) * cell_size - leftBorder, (j + 1) * cell_size - bottomBorder)]), fill=fill)

    img.save(filename)


def findCycle(Puzzle, x, y):
    if (Puzzle[x][y+1][0] == 3) and (Puzzle[x+1][y+1][0] == 3) and (Puzzle[x+1][y][0] == 3):
        cycle = True
    elif (Puzzle[x][y+1][0] == 3) and (Puzzle[x-1][y+1][0] == 3) and (Puzzle[x-1][y][0] == 3):
        cycle = True
    elif (Puzzle[x][y-1][0] == 3) and (Puzzle[x-1][y-1][0] == 3) and (Puzzle[x-1][y][0] == 3):
        cycle = True
    elif (Puzzle[x][y-1][0] == 3) and (Puzzle[x+1][y-1][0] == 3) and (Puzzle[x+1][y][0] == 3):
        cycle = True
    else:
        cycle = False
    return cycle


def pickAWall(x, y, Puzzle):
    Direction = ['up', 'down', 'left', 'right']
    validPathChosen = False
    checkUP = False
    checkDN = False
    checkLT = False
    checkRT = False
    dir = 0
    noValid = False
    while not validPathChosen:
        step = random.choice(Direction)
        if step == 'up':
            # and findCycle(Puzzle, x, y+1) == False:
            if (Puzzle[x][y+1][0] == 0):
                y += 1
                validPathChosen = True
                dir = 1
            else:
                checkUP = True
        elif step == 'down':
            # and findCycle(Puzzle, x, y-1) == False:
            if (Puzzle[x][y-1][0] == 0):
                y -= 1
                validPathChosen = True
                dir = 2
            else:
                checkDN = True
        elif step == 'left':
            # and findCycle(Puzzle, x-1, y) == False:
            if (Puzzle[x-1][y][0] == 0):
                x -= 1
                validPathChosen = True
                dir = 3
            else:
                checkLT = True
        elif step == 'right':
            # and findCycle(Puzzle, x+1, y) == False:
            if (Puzzle[x+1][y][0] == 0):
                x += 1
                validPathChosen = True
                dir = 4
            else:
                checkRT = True

        if checkRT and checkLT and checkDN and checkUP:
            noValid = True
            break

    return x, y, dir, noValid


def IterativeImplementation(mazeWidth, mazeLength, defaultWall):
    ''' 0 = Init, 1 = Border, 2 = Start,, 3 = Visited, 4 = Path with NO Valid Next Move, 5 = End'''
    # Init Maze
    noWallValue = (defaultWall * -1)
    Puzzle = []
    Stack = []
    for i in range(mazeWidth):
        temp = []
        for j in range(mazeLength):
            # Path, Path Wall Thickness (up, down, left, right)
            temp.append([0, defaultWall, defaultWall,
                        defaultWall, defaultWall])
        Puzzle.append(temp)

    # Create Maze Border
    for i in range(mazeWidth):
        # input("Prompt")
        for j in range(mazeLength):
            if (i == 0) or (i == mazeWidth - 1) or (j == 0) or (j == mazeLength-1):
                # [Border, Border Wall Thickness (up, down, left, right)]
                Puzzle[i][j] = [1, defaultWall,
                                defaultWall, defaultWall, defaultWall]

    # Choose the initial cell, mark it as visited and push it to the stack
    startChosen = False
    while not startChosen:
        rnd_indxX = random.randrange(len(Puzzle))
        rnd_indxY = random.randrange(len(Puzzle[0]))

        if Puzzle[rnd_indxX][rnd_indxY][0] != 1:
            Puzzle[rnd_indxX][rnd_indxY][0] = 3
            Stack.append([rnd_indxX, rnd_indxY])
            startChosen = True

    PuzzleComplete = False

    while not PuzzleComplete:
        # While the stack is not empty
        if len(Stack) != 0:
            # Pop a cell from the stack and make it a current cell
            choice = random.randrange(len(Stack))
            currentCellx = Stack[choice][0]
            currentCelly = Stack[choice][1]
            Stack.pop(choice)

            neighbourX, neighbourY, dir, noValid = pickAWall(
                currentCellx, currentCelly, Puzzle)
            # If the current cell has any neighbours which have not been visited
            if not noValid:
                # Push the current cell to the stack
                Stack.append([currentCellx, currentCelly])

                # Choose one of the unvisited neighbours
                Puzzle[currentCellx][currentCelly][0] = 3

                # Remove the wall between the current cell and the chosen cell
                Puzzle[neighbourX][neighbourY][dir] = noWallValue

                # Mark the chosen cell as visited and push it to the stack
                Puzzle[neighbourX][neighbourY][0] = 3
                Stack.append([neighbourX, neighbourY])
        else:
            PuzzleComplete = True
    return Puzzle


Puzzle = IterativeImplementation(mazeWidth, mazeLength, defaultWall)

output_image('Iterative.png', Puzzle)
