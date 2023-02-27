# This is a sample Python script.
import random
import turtle
import tkinter
import pandas as pd
import random
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Maze(object, Width, Length, Wall):
    def __init__(self):
        self.mazeWidth = Width
        self.mazeLength = Length
        self.defaultWall = Wall
        self.__alg = ""
        self.__borders = {}
        self.solution = None
        self.walls = {}
        self.explored = []
        self.visited = {}
        self.randStartCell = tuple()
        self.randNeighbor = tuple()
        self.path = {}
        self.visitedColorVar = {}
        # Recursive Division
        self.desiredResolution = 5

    def __str__(self):
        return "The algorithms available for the maze generator are: Aldous-Broder algorithm, Y, Z"

    def set_algGenerate(self, Algorithm):
        '''Sets the algorithm to be used to generate the maze'''
        self.__alg = Algorithm

        if self.__alg == 'Aldous-Broder algorithm':
            self.Aldous_Broder_Alg(self.mazeWidth, self.mazeLength, self.defaultWall, 'Aldous-Broder algorithm.png')

    def mazeBorderCreate(self):
        for i in range(self.__width):
            for j in range(self.__height):
                if (i,j) != self.__start and (i,j) != self.__end:
                    self.__borders[(i,j)] = 1
                else:
                    self.__borders[(i, j)] = 0

    def MazePathProof(self):
        from random import shuffle, randrange
        direction = []

        direction += [(0, 1)]
        direction += [(0, -1)]
        direction += [(-1, 0)]
        direction += [(1, 0)]
        flag = True
        lastpos = self.__end
        newpos = self.__end

        j = 0

        while flag:
            j += 1
            if lastpos not in self.visited.keys():
                valid = []
                self.visited[lastpos] = True
                for i in range(len(direction)):
                    x = lastpos[0] + direction[i][0]
                    y = lastpos[1] + direction[i][1]
                    if 0 <= x < self.__width:
                        if 0 <= y < self.__height:
                            if (x, y) not in self.visited.keys() and (x, y) not in self.walls.keys():
                                valid += [i]
                print(f"Valid Options: {valid}")

                if len(valid) != 0:
                    continuePath = random.choice(valid)
                    print(f"The Continued Path: {continuePath}")
                    #valid.remove(continuePath)
                    newpos = (lastpos[0] + direction[continuePath][0], lastpos[1] + direction[continuePath][1])
                    #self.visited[newpos] = True
                    print(f"Visited: {newpos}")
                    wallprev = continuePath
                    length = len(valid)-1
                    print(f"Valid len: {length}")
                    i = 0
                    while i < length:
                        wallDirection = random.choice(valid)
                        x = lastpos[0] + direction[wallDirection][0]
                        y = lastpos[1] + direction[wallDirection][1]
                        if (x, y) not in self.visited.keys() and (x, y) != newpos:  # Change visited to any visited value and move current visited to new path dictionary
                            i += 1
                            print(f"Modified valid: {valid}")
                            self.walls[
                                (x, y)] = True
                            print(f"Wall: {x, y}")
                            print(f"Valid value: {valid[i]}")
                            wallprev = wallDirection

                    # for i in range(len(valid)):
                    #     if i != continuePath:
                    #         self.walls[
                    #             (lastpos[0] + direction[valid[i]][0], lastpos[1] + direction[valid[i]][1])] = True
                    #         print(f"Wall: {lastpos[0] + direction[valid[i]][0], lastpos[1] + direction[valid[i]][1]}")
                    #         print(f"Valid value: {valid[i]}")
                    #     else:
                    #         newpos = (lastpos[0] + direction[continuePath][0], lastpos[1] + direction[continuePath][1])
                    #         #self.visited[newpos] = True
                    #         print(f"Visited: {newpos}")
                    lastpos = newpos
                    print("here")
            if j == 1000:
                flag = False
                print(j)
            if newpos == self.__start:
                flag = False
                print("c2")
                print("SUCCESS")




        j = 0
        for i in self.visited.keys():
            #self.visited.keys()[i] = self.visited.values(), 255 - i
            j+=1
            self.visitedColorVar[i] = [0]
        print(self.visited)
        print(self.walls)

    # Add functionality
    # Pick a random square that is not a wall or a path
    # Run the maze path creating code until no viable options left to run for that iteration
    #   Add branching functionality: A new branch will split randomly after 2-5 runs (branches can't occur consecutively)
    #   Add a feature that allows a path to randomly break a wall and place a path but not vice verse.

    # def recursiveDepthFirstSearch(self):
    #     desiredCoverage = {}
    #     for i in range(len(self.__width)):
    #         for j in range(len(self.__height)):
    #             coordSet = (i, j)
    #             desiredCoverage[coordSet] = True

        #base case: No more routes can be taken (nextMove = no value)

    def createStPt(self, startx, endx, starty, endy): # returns (startptx, startpty)

        startptx = ((endx - startx) // 2) + startx
        startpty = ((endy - starty) // 2) + starty
        return (startptx, startpty)# returns (startptx, startpty)
    def createGapy(self, x, y, starty, endy):
            flag = True
            while flag:
                wallHeightLoc = random.choice(np.arange(starty, endy, dtype=int))
                if (x, wallHeightLoc) not in self.visited.keys() and (x, wallHeightLoc) != (x, y):
                    self.visited[(x, wallHeightLoc)] = True
                    self.visited[(x + 1, wallHeightLoc)] = True
                    self.visited[(x - 1, wallHeightLoc)] = True
                    flag = False
    def createGapx(self, x, y, startx, endx):
            flag = True
            while flag:
                wallWidthLoc = random.choice(np.arange(startx, endx, dtype=int))
                if (wallWidthLoc, y) not in self.visited.keys() and (wallWidthLoc, y) != (x, y):
                    self.visited[(wallWidthLoc, y - 1)] = True
                    self.visited[(wallWidthLoc, y)] = True
                    self.visited[(wallWidthLoc, y + 1)] = True
                    flag = False
    def RecursiveDevision(self, startx, endx, starty, endy, mode, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count):
        if not stop:
            if mode == 1: # Vertical Line
                height = np.arange(starty, endy, dtype= int) #abs(endy - starty)
                (x, y) = self.createStPt(startx, endx, starty, endy)

                self.createGapy(x, y, starty+1, endy)
                for i in range(len(height)): #Vertical Line
                    if (x, height[i]) not in self.visited.keys():
                        self.walls[(x, height[i])] = True

                '''Check area'''
                areaUppLeft = (x - startx)*(y - starty)
                areaUppRight = (endx - x)*(y - starty)
                areaDownLeft = (x - startx)*(endy - y)
                areaDownRight = (endx - x)*(endy - y)
                if count > 7:
                    stop = True
                    print("Stopped")
                print(areaDownRight)
                print(count)
                m = 2
            else:
                (x, y) = self.createStPt(startx, endx, starty, endy)
                width = np.arange(x, endx, dtype=int)  # abs(endx - startx)
                self.createGapx(x, y, x + 1, endx)
                for i in range(len(width)):  # Horizontal Line
                    if (width[i], y) not in self.visited.keys():
                        self.walls[(width[i], y)] = True

                '''Check area'''
                areaUppLeft = (x - startx) * (y - starty)
                areaUppRight = (endx - x) * (y - starty)
                areaDownLeft = (x - startx) * (endy - y)
                areaDownRight = (endx - x) * (endy - y)
                if count > 7:
                    stop = True
                    print("Stopped")
                print(areaDownRight)
                print(count)
                m = 1
            if count < 6:
                if m == 1:
                    self.RecursiveDevision(startx, endx, starty, y, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1) # Upp Right, m=1
                    self.RecursiveDevision(startx, x, starty, y, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1) # Upp Left, m=2
                    self.RecursiveDevision(startx, x, y, endy, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1) # Down Left, m=2
                    self.RecursiveDevision(x, endx, y, endy, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1)  # Down Right, m=1
                else:
                    self.RecursiveDevision(x, endx, starty, endy, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1) # Upp Right, m=1
                    self.RecursiveDevision(startx, x, starty, y, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1) # Upp Left, m=2
                    self.RecursiveDevision(startx, x, y, endy, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1) # Down Left, m=2
                    self.RecursiveDevision(x, endx, y, endy, m, startxin, endxin, startyin, endyin, resolution, MazeWidth, MazeLength, stop, count+1)  # Down Right, m=1

    def output_image(self, filename, show_solution=False, show_explored=False):
        from PIL import Image, ImageDraw
        cell_size = 40
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.__width * cell_size, self.__height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        #solution = self.solution[1] if self.solution is not None else None
        for i in range(self.__width):
            #input("Prompt")
            for j in range(self.__height):

                # Walls
                if self.__borders[(i,j)] == 1:
                    fill = (40, 40, 40)

                # Start
                if (i, j) == self.__start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.__end:
                    fill = (0, 171, 28)

                elif (i, j) in self.walls.keys():
                    fill = (0, 0, 0)

                elif (i, j) in self.visited.keys():
                    fill = (255, 255, 255)

                # # Solution
                # elif solution is not None and show_solution and (i, j) in solution:
                #     fill = (220, 235, 113)
                #
                # # Explored
                # elif solution is not None and show_explored and (i, j) in self.explored:
                #     fill = (212, 97, 85)

                # Empty cell
                else:
                    fill = (255, 255, 255)#(40, 40, 40)

                # Draw cell
                draw.rectangle(([(i * cell_size + cell_border, j * cell_size + cell_border),((i + 1) * cell_size - cell_border, (j + 1) * cell_size - cell_border)]),fill=fill)


        img.save(filename)

    def output_image_Aldous_Broder(self, filename, Puzzle, mazeWidth, mazeLength):
        from PIL import Image, ImageDraw
        cell_size = 40

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (mazeWidth * cell_size, mazeLength * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        #solution = self.solution[1] if self.solution is not None else None
        for i in range(mazeWidth):
            #input("Prompt")
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
                draw.rectangle(([(i * cell_size + rightBorder, j * cell_size + topBorder),((i + 1) * cell_size - leftBorder, (j + 1) * cell_size - bottomBorder)]),fill=fill)


        img.save(filename)

    def chooseDirection(self, x, y, Puzzle):
                Direction = ['up','down','left','right']
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
                        if (Puzzle[x][y+1][0] == 0):# and findCycle(Puzzle, x, y+1) == False:
                            y += 1
                            validPathChosen = True
                            dir = 1
                        else:
                            checkUP = True
                    elif step =='down':
                        if (Puzzle[x][y-1][0] == 0):# and findCycle(Puzzle, x, y-1) == False:
                            y -= 1
                            validPathChosen = True
                            dir = 2
                        else:
                            checkDN = True
                    elif step =='left':
                        if (Puzzle[x-1][y][0] == 0):# and findCycle(Puzzle, x-1, y) == False:
                            x -= 1
                            validPathChosen = True
                            dir = 3
                        else:
                            checkLT = True
                    elif step =='right':
                        if (Puzzle[x+1][y][0] == 0):# and findCycle(Puzzle, x+1, y) == False:
                            x += 1
                            validPathChosen = True
                            dir = 4
                        else:
                            checkRT = True

                    if checkRT and checkLT and checkDN and checkUP:
                        noValid = True
                        break
                        
                return  x, y, dir, noValid
    def Aldous_Broder_Alg(self, mazeWidth, mazeLength, defaultWall, filename):
        # 0 = Init, 1 = Border, 2 = Start,, 3 = Path with a Valid Next Move, 4 = Path with NO Valid Next Move, 5 = End
        # Init Maze
        
        noWallValue = (defaultWall * -1)
        Puzzle = []
        for i in range(mazeWidth):
            temp = []
            for j in range(mazeLength):
                temp.append([0, defaultWall, defaultWall, defaultWall, defaultWall]) # Path, Path Wall Thickness (up, down, left, right)
            Puzzle.append(temp)

        # Create Maze Border
        for i in range(mazeWidth):
            #input("Prompt")
            for j in range(mazeLength):
                if (i == 0) or (i == mazeWidth - 1) or (j == 0) or (j == mazeLength-1):
                    Puzzle[i][j] = [1, defaultWall, defaultWall, defaultWall, defaultWall] # [Border, Border Wall Thickness (up, down, left, right)]


        # Choose a random starting point
        startChosen = False
        while not startChosen:
            rnd_indxX = random.randrange(len(Puzzle))
            rnd_indxY = random.randrange(len(Puzzle[0]))

            if Puzzle[rnd_indxX][rnd_indxY][0] != 1:
                Puzzle[rnd_indxX][rnd_indxY][0] = 3
                startChosen = True      

        x, y, dir, noValidPath = self.chooseDirection(rnd_indxX, rnd_indxY, Puzzle)
        Puzzle[x][y][0] = 3
        if dir != 0:
            Puzzle[x][y][dir] = noWallValue

        MazeComplete = False
        while not MazeComplete:
            x, y, dir, noValidPath = self.chooseDirection(x, y, Puzzle)
            Puzzle[x][y][0] = 3
            if dir != 0:
                Puzzle[x][y][dir] = noWallValue
            else:
                Puzzle[x][y][0] = 4
                nextMove = []
                for i in range(mazeWidth):
                    for j in range(mazeLength):
                        if Puzzle[i][j][0] == 3:
                            xnew, ynew, dir, noValidPath = self.chooseDirection(i, j, Puzzle)
                            if noValidPath:
                                Puzzle[i][j][0] = 4 # COLOR SET FOR DEBUGGING
                        if Puzzle[i][j][0] == 3:
                            nextMove.append([i,j])
                if len(nextMove) != 0:
                    newStartingPt = random.choice(nextMove)
                    x = newStartingPt[0]
                    y = newStartingPt[1]
                    #Puzzle[x][y][0] = 2 # COLOR SET FOR DEBUGGING
                else:
                    MazeComplete = True
                    
        Puzzle[1][1][0] = 2 # Defining the starting position (for the user)
        Puzzle[mazeWidth-2][mazeLength-2][0] = 5 #Defining the ending position (for the user)
        
        self.output_image_Aldous_Broder(filename, Puzzle, mazeWidth, mazeLength)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
