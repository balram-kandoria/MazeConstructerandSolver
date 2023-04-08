from Randomized_Prims_algorithm import randomizedPrimsAlg
import random
import os
import numpy as np

mazeWidth = 20
mazeLength = 20
defaultWall = 3


def output_image_Prims(filename, Puzzle, mazeWidth, mazeLength, norm):
    from PIL import Image, ImageDraw
    cell_size = 30

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
            if Puzzle[i][j][0] == -1:
                fill = (40, 40, 40)

            # Set Path Visual
            elif Puzzle[i][j][0] == 0:
                fill = (255, 255, 255)

            # Set Starting Point Visual
            elif Puzzle[i][j][0] == -2:
                fill = (124, 252, 0)

            # Set Starting Point Visual
            elif Puzzle[i][j][0] == norm + 1:
                fill = (124, 128, 200)

            # Set Ending Point Visual
            elif Puzzle[i][j][0] == -5:
                fill = (255, 0, 0)

            else:
                fill = (int(255*(Puzzle[i][j][0]/norm)), int(128 *
                        (Puzzle[i][j][0]/norm)), int(50 *
                        (Puzzle[i][j][0]/norm)))
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


# Refactor Maze
# Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
unvisitedSet = []
for i in range(mazeWidth):
    for j in range(mazeLength):
        if Puzzle[i][j][0] != 1:
            Puzzle[i][j][0] = 0
            unvisitedSet.append([i, j, np.inf])
        else:
            Puzzle[i][j][0] = -1

# Defining the starting position (for the user)
Puzzle[1][1][0] = 2

# Defining the ending position (for the user)
Puzzle[mazeWidth-2][mazeLength-2][0] = -5

# Pick a starting position
position = [1, 1]


# Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes.
# During the run of the algorithm, the tentative distance of a node v is the length of the shortest path discovered so far
# between the node v and the starting node. Since initially no path is known to any other vertex than the source itself
# (which is a path of length zero), all other tentative distances are initially set to infinity. Set the initial node as current.[17]
distance = 2
childList = []
visitList = [position]
solution = False
run = 0
while not solution:
    # for i in range(mazeLength):
    #     for j in range(mazeWidth):
    #         if Puzzle[unvisitedSet[run][0] + move[0]][unvisitedSet[run][1] + move[1]][0] == distance:
    #             visitList.append([i, j])
    if run != 0:
        visitList = childList
        childList = []

    run += 1
    # For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node.
    # Compare the newly calculated tentative distance to the one currently assigned to the neighbor and assign it the smaller one.
    # For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2,
    # then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8.
    # Otherwise, the current value will be kept.
    visitlistZero = False
    for run in range(len(visitList)):
        dir = 0
        position = visitList[0]
        # print(position)
        visitList.pop(0)
        for i in range(4):
            moveMade = False
            dir += 1
            if Puzzle[position[0]][position[1]][dir] < 0:
                distance = Puzzle[position[0]][position[1]][0] + 1
                if dir == 1:
                    if Puzzle[position[0]][position[1] - 1][0] in [0, -5]:
                        move = [0, -1]
                        moveMade = True
                elif dir == 2:
                    if Puzzle[position[0]][position[1] + 1][0] in [0, -5]:
                        move = [0, 1]
                        moveMade = True
                elif dir == 3:
                    if Puzzle[position[0] + 1][position[1]][0] in [0, -5]:
                        move = [1, 0]
                        moveMade = True
                else:
                    if Puzzle[position[0] - 1][position[1]][0] in [0, -5]:
                        move = [-1, 0]
                        moveMade = True

            if moveMade:
                currentdistance = Puzzle[position[0] +
                                         move[0]][position[1] + move[1]][0]
                if currentdistance > distance or currentdistance == 0:
                    if Puzzle[position[0] + move[0]][position[1] + move[1]][0] != -5:
                        Puzzle[position[0] + move[0]
                               ][position[1] + move[1]][0] = distance
                        childList.append(
                            [position[0] + move[0], position[1] + move[1]])
                    else:
                        solution = True

                if Puzzle[position[0] + move[0]][position[1] + move[1]][0] == -5:
                    solution = True
                # print(currentdistance)

    # unvisitedSet.pop(0)


# When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove
# it from the unvisited set. A visited node will never be checked again (this is valid and optimal in connection with the behavior
# in step 6.: that the next nodes to visit will always be in the order of 'smallest distance from initial node first' so any visits
#  after would have a greater distance).

# If the destination node has been marked visited (when planning a route between two specific nodes) or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm has finished.
# Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, and go back to step 3.
norm = distance
print(norm)

distance += 1
position = [mazeWidth-2, mazeLength-2]
for j in range((5)):
    dir = 0
    distance -= 1

    distanceList = [False, False, False, False]
    for i in range(4):
        moveMade = False
        dir += 1
        value = Puzzle[position[0]][position[1]][0]
        if Puzzle[position[0]][position[1]][dir] < 0 and Puzzle[position[0]][position[1]][dir] != mazeLength*mazeWidth:
            if dir == 1:
                moveMade = True
                distanceList[0] = True
            elif dir == 2:
                moveMade = True
                distanceList[1] = True
            elif dir == 3:

                moveMade = True
                distanceList[2] = True
            else:
                move = [-1, 0]
                moveMade = True
                distanceList[3] = True

    temp = mazeLength*mazeWidth
    tempPos = []
    indx = 0
    if distanceList[0]:
        move = [0, -1]
        if Puzzle[position[0] + move[0]][position[1] + move[1]][0] < temp:
            tempPos = [position[0] + move[0], position[1] + move[1]]
            temp = Puzzle[position[0] + move[0]][position[1] + move[1]][0]
    if distanceList[1]:
        move = [0, 1]
        if Puzzle[position[0] + move[0]][position[1] + move[1]][0] < temp:
            tempPos = [position[0] + move[0], position[1] + move[1]]
            temp = Puzzle[position[0] + move[0]][position[1] + move[1]][0]
            indx = 1
    if distanceList[2]:
        move = [1, 0]
        if Puzzle[position[0] + move[0]][position[1] + move[1]][0] < temp:
            tempPos = [position[0] + move[0], position[1] + move[1]]
            temp = Puzzle[position[0] + move[0]][position[1] + move[1]][0]
            indx = 2
    if distanceList[3]:
        move = [-1, 0]
        if Puzzle[position[0] + move[0]][position[1] + move[1]][0] < temp:
            tempPos = [position[0] + move[0], position[1] + move[1]]
            temp = Puzzle[position[0] + move[0]][position[1] + move[1]][0]
            indx = 3

    print(indx)
    print(tempPos)
    print(distanceList)
    Puzzle[tempPos[0]][tempPos[1]][0] = mazeWidth*mazeLength
    position = [tempPos[0], tempPos[1]]

output_image_Prims('Dijkstras.png', Puzzle, mazeWidth, mazeLength, norm)


print()
print(norm)

for i in range((mazeLength)):
    for j in range((mazeWidth)):
        print(Puzzle[i][j][0], end=' ')
    print()
