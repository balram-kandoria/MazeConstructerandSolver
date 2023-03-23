import random
import numpy

mazeWidth = 50
mazeLength = 50
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
            topBorder = Puzzle[i][j][1]
            bottomBorder = Puzzle[i][j][2]
            rightBorder = Puzzle[i][j][3]
            leftBorder = Puzzle[i][j][4]
            draw.rectangle(([(i * cell_size + rightBorder, j * cell_size + topBorder), ((
                i + 1) * cell_size - leftBorder, (j + 1) * cell_size - bottomBorder)]), fill=fill)

    img.save(filename)


def pickAWall(x, y, Puzzle, defaultWall, removeZeros, RandUn):
    Direction = ['up', 'down', 'left', 'right']
    validPathChosen = False
    checkUP = False
    checkDN = False
    checkLT = False
    checkRT = False
    dir = 0
    noValid = False
    # print('Function While loop')
    while not validPathChosen:
        step = random.choice(Direction)
        if step == 'up':
            try:
                # and findCycle(Puzzle, x, y+1) == False:
                if removeZeros:
                    if (Puzzle[x][y+1][0] != Puzzle[x][y][0]):
                        if Puzzle[x][y+1][0] != 1 and ((Puzzle[x][y+1][1] + Puzzle[x][y+1][2] + Puzzle[x][y+1][3] + Puzzle[x][y+1][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            y += 1
                            validPathChosen = True
                            dir = 1
                        else:
                            checkUP = True
                    else:
                        checkUP = True
                else:
                    if (Puzzle[x][y+1][0] != Puzzle[x][y][0]):
                        if Puzzle[x][y+1][0] != 1 and ((Puzzle[x][y+1][1] + Puzzle[x][y+1][2] + Puzzle[x][y+1][3] + Puzzle[x][y+1][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            y += 1
                            validPathChosen = True
                            dir = 1
                        else:
                            checkUP = True
                    else:
                        checkUP = True
            except:
                checkUP = True

        elif step == 'down':
            try:
                # and findCycle(Puzzle, x, y-1) == False:
                if removeZeros:
                    if (Puzzle[x][y-1][0] != Puzzle[x][y][0]):
                        if Puzzle[x][y-1][0] != 1 and ((Puzzle[x][y-1][1] + Puzzle[x][y-1][2] + Puzzle[x][y-1][3] + Puzzle[x][y-1][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            y -= 1
                            validPathChosen = True
                            dir = 2
                        else:
                            checkDN = True
                    else:
                        checkDN = True
                else:
                    if (Puzzle[x][y-1][0] != Puzzle[x][y][0]):
                        if Puzzle[x][y-1][0] != 1 and ((Puzzle[x][y-1][1] + Puzzle[x][y-1][2] + Puzzle[x][y-1][3] + Puzzle[x][y-1][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            y -= 1
                            validPathChosen = True
                            dir = 2
                        else:
                            checkDN = True
                    else:
                        checkDN = True
            except:
                checkDN = True

        elif step == 'left':
            try:
                # and findCycle(Puzzle, x-1, y) == False:
                if removeZeros:
                    if (Puzzle[x-1][y][0] != Puzzle[x][y][0]):
                        if Puzzle[x-1][y][0] != 1 and ((Puzzle[x-1][y][1] + Puzzle[x-1][y][2] + Puzzle[x-1][y][3] + Puzzle[x-1][y][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            x -= 1
                            validPathChosen = True
                            dir = 3
                        else:
                            checkLT = True
                    else:
                        checkLT = True
                else:
                    if (Puzzle[x-1][y][0] != Puzzle[x][y][0]):
                        if Puzzle[x-1][y][0] != 1 and ((Puzzle[x-1][y][1] + Puzzle[x-1][y][2] + Puzzle[x-1][y][3] + Puzzle[x-1][y][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            x -= 1
                            validPathChosen = True
                            dir = 3
                        else:
                            checkLT = True
                    else:
                        checkLT = True
            except:
                checkLT = True
        elif step == 'right':
            try:
                # and findCycle(Puzzle, x+1, y) == False:
                if removeZeros:
                    if (Puzzle[x+1][y] != Puzzle[x][y]):
                        if Puzzle[x+1][y][0] != 1 and ((Puzzle[x+1][y][1] + Puzzle[x+1][y][2] + Puzzle[x+1][y][3] + Puzzle[x+1][y][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            x += 1
                            validPathChosen = True
                            dir = 4
                        else:
                            checkRT = True
                    else:
                        checkRT = True
                else:
                    if (Puzzle[x+1][y] != Puzzle[x][y]) and Puzzle[x][y] == RandUn:
                        if Puzzle[x+1][y][0] != 1 and ((Puzzle[x+1][y][1] + Puzzle[x+1][y][2] + Puzzle[x+1][y][3] + Puzzle[x+1][y][4]) > -2) and ((Puzzle[x][y][1] + Puzzle[x][y][2] + Puzzle[x][y][3] + Puzzle[x][y][4]) > -2):
                            x += 1
                            validPathChosen = True
                            dir = 4
                        else:
                            checkRT = True
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
        temp.append([0, defaultWall, defaultWall,
                     defaultWall, defaultWall])
        Wallset.append([i, j])
    Puzzle.append(temp)

# Create Maze Border
for i in range(mazeWidth):
    # input("Prompt")
    for j in range(mazeLength):
        if (i == 0) or (i == mazeWidth - 1) or (j == 0) or (j == mazeLength-1):
            # [Border, Border Wall Thickness (up, down, left, right)]
            Puzzle[i][j] = [1, defaultWall, defaultWall,
                            defaultWall, defaultWall]
startChosen = False

while not startChosen:
    rnd_indxX = random.randrange(len(Puzzle))
    rnd_indxY = random.randrange(len(Puzzle[0]))

    if Puzzle[rnd_indxX][rnd_indxY][0] != 1:
        Puzzle[rnd_indxX][rnd_indxY][0] = 3
        startChosen = True

uniqueValue = 4
removeZeros = True
MergingSet = -1
UnqiueValSet = []
visitedSet = []
for run in range(4000):
    count = 0
    # Choose a random starting point
    if run != 0:
        startChosen = False
        # print('Main While loop')
        temp = []
        while not startChosen:
            if removeZeros:
                for i in range(mazeWidth):
                    for j in range(mazeLength):
                        if Puzzle[i][j][0] == 0:
                            temp.append([i, j])

                if len(temp) > 0:
                    choice = random.choice(temp)
                    rnd_indxX = choice[0]
                    rnd_indxY = choice[1]
                else:
                    removeZeros = False
                    UnqiueValSet = []
                    for width in range(mazeWidth):
                        for length in range(mazeLength):
                            if Puzzle[width][length][0] > 1:
                                UnqiueValSet.append([width, length])

            elif not removeZeros:
                try:
                    choice = random.randrange(len(UnqiueValSet))
                    rnd_indxX = UnqiueValSet[choice][0]
                    rnd_indxY = UnqiueValSet[choice][1]
                    UnqiueValSet.pop(choice)
                    MergingSet = Puzzle[rnd_indxX][rnd_indxY][0]
                    print(MergingSet)
                    if len(UnqiueValSet) == 0:
                        for width in range(mazeWidth):
                            for length in range(mazeLength):
                                if Puzzle[width][length][0] > 1:
                                    UnqiueValSet.append([width, length])
                except:
                    continue

            if Puzzle[rnd_indxX][rnd_indxY][0] != 1:
                if Puzzle[rnd_indxX][rnd_indxY][0] == 0:
                    Puzzle[rnd_indxX][rnd_indxY][0] = uniqueValue
                startChosen = True
            count += 0
            if count > mazeLength*mazeWidth:
                break

    xold = rnd_indxX
    yold = rnd_indxY
    x, y, dir, noValid = pickAWall(
        rnd_indxX, rnd_indxY, Puzzle, defaultWall, removeZeros, MergingSet)
    # print(x)
    # print(y)
    # print(dir)
    if noValid == False:
        startingNode = Puzzle[xold][yold][0]
        endingNode = Puzzle[x][y][0]
        if Puzzle[xold][yold][0] > 0:
            assignSet = Puzzle[xold][yold][0]
        else:
            assignSet = uniqueValue

        # if Puzzle[x][y][0] > 0:
        #     print('Value needs to be replaced')

         # Create a list of the set identifiers for merging
        if not removeZeros:
            assignSet = MergingSet

        Puzzle[x][y][0] = assignSet

        middleNode = -1
        if dir == 1:
            # middleNode = Puzzle[x][y-1][0]
            # Puzzle[x][y-1][0] = assignSet
            # Puzzle[x][y-1][2] = noWallValue
            Puzzle[x][y][dir] = noWallValue/2
            Puzzle[xold][yold][2] = noWallValue/2
        elif dir == 2:
            # middleNode = Puzzle[x][y+1][0]
            # Puzzle[x][y+1][0] = assignSet
            # Puzzle[x][y+1][1] = noWallValue
            Puzzle[x][y][dir] = noWallValue/2
            Puzzle[xold][yold][1] = noWallValue/2
        elif dir == 3:
            # middleNode = Puzzle[x+1][y][0]
            # Puzzle[x+1][y][0] = assignSet
            Puzzle[x][y][4] = noWallValue/2
            Puzzle[xold][yold][dir] = noWallValue/2
            # Puzzle[x+1][y][4] = noWallValue
        elif dir == 4:
            # middleNode = Puzzle[x-1][y][0]
            # Puzzle[x-1][y][0] = assignSet
            Puzzle[x][y][3] = noWallValue/2
            Puzzle[xold][yold][dir] = noWallValue/2
            # Puzzle[x-1][y][3] = noWallValue

        uniqueValue += 1

        print(f"Run: {run}")
        print(f"Starting Value: {startingNode}")
        print(f"Middle Value: {middleNode}")
        print(f"Ending Value: {endingNode}")
        print(f"Valid Move: {not(noValid)}")
        print()

        if endingNode > 1:
            temp = []
            for i in range(mazeWidth):
                # input("Prompt")
                for j in range(mazeLength):
                    temp.append(Puzzle[i][j][0])
                    if Puzzle[i][j][0] == endingNode:
                        Puzzle[i][j][0] = startingNode

            if len(set(temp)) == 2:
                break

        # if middleNode > 1:
        #     for i in range(mazeWidth):
        #         # input("Prompt")
        #         for j in range(mazeLength):
        #             if Puzzle[i][j][0] == middleNode:
        #                 Puzzle[i][j][0] = startingNode

output_image_Kruskals('Kruskals Test.png', Puzzle, defaultWall)

temp = []
for i in range(mazeWidth):
    for j in range(mazeLength):
        print(Puzzle[i][j][0], end='  ')
        temp.append(Puzzle[i][j][0])
    print()
print(len(set(temp))-2)

print(run)


# for i in range(mazeWidth*mazeLength):
#     print(Wallset[i],  end=" ")
#     if (i + 1) % 10 == 0:
#         print()
