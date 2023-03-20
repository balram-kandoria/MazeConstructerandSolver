import random

mazeWidth = 10
mazeLength = 10
defaultWall = 4


def output_image_Kruskals(filename, Puzzle, defaultWall):
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
            elif Puzzle[i][j][0] >= 3:
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
            topBorder = defaultWall
            bottomBorder = defaultWall
            rightBorder = defaultWall
            leftBorder = defaultWall
            draw.rectangle(([(i * cell_size + rightBorder, j * cell_size + topBorder), ((
                i + 1) * cell_size - leftBorder, (j + 1) * cell_size - bottomBorder)]), fill=fill)

    img.save(filename)


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
            try:
                # and findCycle(Puzzle, x, y+1) == False:
                if (Puzzle[x][y+2][0] != Puzzle[x][y][0]):
                    if Puzzle[x][y+2][0] != 1:
                        y += 2
                        validPathChosen = True
                        dir = 1
                else:
                    checkUP = True
            except:
                checkUP = True

        elif step == 'down':
            try:
                # and findCycle(Puzzle, x, y-1) == False:
                if (Puzzle[x][y-2][0] != Puzzle[x][y][0]):
                    if Puzzle[x][y-2][0] != 1:
                        y -= 2
                        validPathChosen = True
                        dir = 2
                else:
                    checkDN = True
            except:
                checkDN = True

        elif step == 'left':
            try:
                # and findCycle(Puzzle, x-1, y) == False:
                if (Puzzle[x-2][y][0] != Puzzle[x][y][0]):
                    if Puzzle[x-2][y][0] != 1:
                        x -= 2
                        validPathChosen = True
                        dir = 3
                else:
                    checkLT = True
            except:
                checkLT = True
        elif step == 'right':
            try:
                # and findCycle(Puzzle, x+1, y) == False:
                if (Puzzle[x+2][y] != Puzzle[x][y]):
                    if Puzzle[x+2][y][0] != 1:
                        x += 2
                        validPathChosen = True
                        dir = 4
                else:
                    checkRT = True
            except:
                checkRT = True

        if checkRT and checkLT and checkDN and checkUP:
            noValid = True
            break

    return x, y, dir, noValid


# 0 = Init, 1 = Border, 2 = Start,, 3 = Path with a Valid Next Move, 4 = Path with NO Valid Next Move, 5 = End
# Init Maze
noWallValue = (defaultWall * -1)
Puzzle = []
Wallset = []
for i in range(mazeWidth):
    temp = []
    for j in range(mazeLength):
        # Path, Path Wall Thickness (up, down, left, right)
        temp.append([0])
        Wallset.append([i, j])
    Puzzle.append(temp)

# Create Maze Border
for i in range(mazeWidth):
    # input("Prompt")
    for j in range(mazeLength):
        if (i == 0) or (i == mazeWidth - 1) or (j == 0) or (j == mazeLength-1):
            # [Border, Border Wall Thickness (up, down, left, right)]
            Puzzle[i][j] = [1]

uniqueValue = 3

for run in range(3):
    # Choose a random starting point
    startChosen = False

    while not startChosen:
        rnd_indxX = random.randrange(len(Puzzle))
        rnd_indxY = random.randrange(len(Puzzle[0]))

        if Puzzle[rnd_indxX][rnd_indxY][0] != 1:
            # Puzzle[rnd_indxX][rnd_indxY][0] = uniqueValue
            startChosen = True

    xold = rnd_indxX
    yold = rnd_indxY
    x, y, dir, noValid = pickAWall(rnd_indxX, rnd_indxY, Puzzle)
    print(x)
    print(y)
    print(dir)

    if Puzzle[xold][yold][0] > 0:
        assignSet = Puzzle[xold][yold][0]

    else:
        assignSet = uniqueValue

    if Puzzle[x][y][0] > 0:
        print('Value needs to be replaced')

    Puzzle[x][y][0] = assignSet
    if dir == 1:
        Puzzle[x][y-1][0] = assignSet
    elif dir == 2:
        Puzzle[x][y+1][0] = assignSet
    elif dir == 3:
        Puzzle[x+1][y][0] = assignSet
    elif dir == 4:
        Puzzle[x-1][y][0] = assignSet

    uniqueValue += 1


output_image_Kruskals('Kruskals Test.png', Puzzle, defaultWall)

for i in range(len(Puzzle)):
    print(Puzzle[i])


# for i in range(mazeWidth*mazeLength):
#     print(Wallset[i],  end=" ")
#     if (i + 1) % 10 == 0:
#         print()
