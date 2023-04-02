from Randomized_Prims_algorithm import randomizedPrimsAlg, output_image_Prims
from Kruskals_algorithm import Kruskals, output_image_Kruskals
import random
import os
import cv2
import numpy as np
import glob

mazeWidth = 25
mazeLength = 25
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


def BFS(Puzzle, mazeWidth, mazeLength):
    image = 1
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

    # Initilize a stack of nodes to explore from the current position
    # Select one node from the stack and delete it from the stack
    # add the valid moves from that node to a new stack or end if at the end

    Stack = []
    ChildStack = [position]
    mazeSolved = False

    # Check Valid next moves (i.e no wall between current cell and next cell)
    # Look at surrounding Nodes (1 = up, 2 = down, 3 = left, 4 = right)
    # Choose the next move in some non-random manner (i.e up, down, left, right)
    Map = []
    dir = 0
    move = [0, 0]
    moveMade = False
    image = 0
    map_indx = 0
    while not mazeSolved:
        print(f"Stack is: {ChildStack}")
        Stack = ChildStack
        Map.append(ChildStack[:])
        ChildStack = []
        for run in range(len(Stack)):
            position = Stack[0]
            print(f"Current position: {position}")
            print(Stack[0])
            Stack.pop(0)
            dir = 0
            moveMade = False
            if Puzzle[position[0]][position[1]][0] != 5:
                Puzzle[position[0]][position[1]][0] = 3
            for i in range(4):
                dir += 1
                if Puzzle[position[0]][position[1]][dir] < 0:
                    if dir == 1:
                        if Puzzle[position[0]][position[1] - 1][0] in [0, 4, 5]:
                            move = [0, -1]
                            moveMade = True
                    elif dir == 2:
                        if Puzzle[position[0]][position[1] + 1][0] in [0, 4, 5]:
                            move = [0, 1]
                            moveMade = True
                    elif dir == 3:
                        if Puzzle[position[0] + 1][position[1]][0] in [0, 4, 5]:
                            move = [1, 0]
                            moveMade = True
                    else:
                        if Puzzle[position[0] - 1][position[1]][0] in [0, 4, 5]:
                            move = [-1, 0]
                            moveMade = True

                    # if not moveMade:
                    #     # Mark Deadend
                    #     position = Stack[len(Stack)-1][0]
                    #     Puzzle[position[0]][position[1]][0] = 4

                    #     # If dead end is reach pop the last value of the stack and set the last value of the Stack as the current position
                    #     # Stack.pop(len(Stack)-1)
                    #     # position = Stack[len(Stack)-1][0]
                    #     # print(position)

                # else:

                if moveMade:
                    newposition = [position[0] +
                                   move[0], position[1] + move[1]]

                    # End Condition
                    if Puzzle[newposition[0]][newposition[1]][0] == 5:
                        mazeSolved = True
                        break
                    else:
                        print('Made')
                        moveMade = False
                        # Make the choosen cell the current cell and mark the current cell as visited
                        if Puzzle[newposition[0]][newposition[1]][0] != 5:
                            Puzzle[newposition[0]][newposition[1]][0] = 4
                        # Add current position to Stack
                        ChildStack.append(newposition)
                        map_indx += 1
                        print(f"Discovered position: {newposition}")
        image += 1
        imageName = str(image) + '_BFS' + '.png'
        cwd = os.getcwd()
        directory = cwd + '\\' + 'BFS\\' + imageName
        output_image_Prims(
            directory, Puzzle, mazeWidth, mazeLength)

        print()

    for i in range(mazeLength):
        for j in range(mazeWidth):
            print(Puzzle[j][i][0], end=' ')
        print()

    # print(Stack[0])
    print(len(Map))
    for i in range(len(Map)):
        print(Map[i])

    # Given a Map of All visited positions
    # define what the ending position that was solved for
    # Take the last layer of the Map and determine which value is a valid move from the ending position
    # Add the valid position to a Solution stack
    # Remove the layer that was being looked at
    Solution = []
    position = [mazeWidth-2, mazeLength-2]
    print(position)
    for i in range(len(Map)-1, -1, -1):
        for j in range(len(Map[i])):
            currentPosition = Map[i][j]
            dir = 0
            for k in range(4):
                dir += 1
                if Puzzle[position[0]][position[1]][dir] < 0:
                    if dir == 1:
                        if [position[0], position[1] - 1] == currentPosition:
                            move = [0, -1]
                            moveMade = True
                    elif dir == 2:
                        if [position[0], position[1] + 1] == currentPosition:
                            move = [0, 1]
                            moveMade = True
                    elif dir == 3:
                        if [position[0] + 1, position[1]] == currentPosition:
                            move = [1, 0]
                            moveMade = True
                    else:
                        if [position[0] - 1, position[1]] == currentPosition:
                            move = [-1, 0]
                            moveMade = True

        if moveMade:
            newposition = [position[0] +
                           move[0], position[1] + move[1]]

            Solution.append(newposition)
            moveMade = False
            position = newposition
            print(f"Discovered position: {newposition}")
            Puzzle[newposition[0]][newposition[1]][0] = 6

    Puzzle[1][1][0] = 2
    image += 1
    imageName = str(image) + '_BFS' + '.png'
    cwd = os.getcwd()
    directory = cwd + '\\' + 'BFS\\' + imageName
    output_image_Prims(
        directory, Puzzle, mazeWidth, mazeLength)

    return Puzzle


Puzzle = BFS(Puzzle, mazeWidth, mazeLength)
