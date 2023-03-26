from Randomized_Prims_algorithm import randomizedPrimsAlg, output_image_Prims
from Kruskals_algorithm import Kruskals, output_image_Kruskals
import random
mazeWidth = 90
mazeLength = 90
defaultWall = 3


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


Puzzle = randomizedPrimsAlg(mazeWidth, mazeLength, defaultWall)
# Puzzle = Kruskals(mazeWidth, mazeLength, defaultWall)


# Refactor Maze
for i in range(mazeWidth):
    for j in range(mazeLength):
        if Puzzle[i][j][0] != 1:
            Puzzle[i][j][0] = 0

# Defining the starting position (for the user)
Puzzle[1][1][0] = 2

# Defining the ending position (for the user)
Puzzle[mazeWidth-2][mazeLength-2][0] = 5

# Pick a starting position
position = [1, 1]

# Mark the current cell as visited
# Puzzle[1][1][0] = 3

Stack = [position]
mazeSolved = False
while not mazeSolved:
    # Check Valid next moves (i.e no wall between current cell and next cell)
    # Look at surrounding Nodes (1 = up, 2 = down, 3 = left, 4 = right)
    # Choose the next move in some non-random manner (i.e up, down, left, right)
    dir = 0
    move = [0, 0]
    moveMade = False
    for i in range(4):
        dir += 1
        if not moveMade:
            if Puzzle[position[0]][position[1]][dir] < 0:
                if dir == 1:
                    if Puzzle[position[0]][position[1] - 1][0] in [0, 5]:
                        move = [0, -1]
                        moveMade = True
                elif dir == 2:
                    if Puzzle[position[0]][position[1] + 1][0] in [0, 5]:
                        move = [0, 1]
                        moveMade = True
                elif dir == 3:
                    if Puzzle[position[0] + 1][position[1]][0] in [0, 5]:
                        move = [1, 0]
                        moveMade = True
                else:
                    if Puzzle[position[0] - 1][position[1]][0] in [0, 5]:
                        move = [-1, 0]
                        moveMade = True

    if not moveMade:
        # Mark Deadend
        position = Stack[len(Stack)-1][0]
        Puzzle[position[0]][position[1]][0] = 4

        # If dead end is reach pop the last value of the stack and set the last value of the Stack as the current position
        Stack.pop(len(Stack)-1)
        position = Stack[len(Stack)-1][0]
        # print(position)
    else:
        position = [position[0] + move[0], position[1] + move[1]]

        # End Condition
        if Puzzle[position[0]][position[1]][0] == 5:
            mazeSolved = True
        else:
            # Make the choosen cell the current cell and mark the current cell as visited
            Puzzle[position[0]][position[1]][0] = 3
            # Add current position to Stack
            Stack.append([position])

    # print(Stack)


output_image_Prims('DFS.png',
                   Puzzle, mazeWidth, mazeLength)

for i in range(mazeLength):
    for j in range(mazeWidth):
        print(Puzzle[j][i][0], end=' ')
    print()
