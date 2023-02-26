from main import *
import random

mazeWidth = 20
mazeLength = 20


def output_image(filename, Puzzle):
    from PIL import Image, ImageDraw
    cell_size = 40
    cell_border = 2

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
            if Puzzle[i][j] == 1:
                fill = (40, 40, 40)
            
            # Set Path Visual
            elif Puzzle[i][j] == 0:
                fill = (255, 255, 255)

            # Set Starting Point Visual
            elif Puzzle[i][j] == 2:
                fill = (124, 252, 0)

            # Set Path Visual
            elif Puzzle[i][j] == 3:
                fill = (0, 0, 255)
            # # Walls
            # if self.__borders[(i,j)] == 1:
            #     fill = (40, 40, 40)

            # # Start
            # if (i, j) == self.__start:
            #     fill = (255, 0, 0)

            # # Goal
            # elif (i, j) == self.__end:
            #     fill = (0, 171, 28)

            # elif (i, j) in self.walls.keys():
            #     fill = (0, 0, 0)

            # elif (i, j) in self.visited.keys():
            #     fill = (255, 255, 255)

            # # Solution
            # elif solution is not None and show_solution and (i, j) in solution:
            #     fill = (220, 235, 113)
            #
            # # Explored
            # elif solution is not None and show_explored and (i, j) in self.explored:
            #     fill = (212, 97, 85)

            # Empty cell

            # Draw cell
            # if i != mazeWidth-1 or j != mazeLength-1:
            draw.rectangle(([(i * cell_size + cell_border, j * cell_size + cell_border),((i + 1) * cell_size - cell_border, (j + 1) * cell_size - cell_border)]),fill=fill)


    img.save(filename)
# testMaze = Maze(mazeWidth, mazeLength, (0,0), (20,20))

# area = mazeLength*mazeWidth

# testMaze.mazeBorderCreate()
# testMaze.output_image("maze1.png")

# testMaze.RecursiveDevision(startx = 0, endx = mazeWidth, starty = 0, endy = mazeLength, mode = 0, startxin=0, endxin = mazeWidth, startyin = 0, endyin = mazeLength, resolution =300
#                            , MazeWidth = mazeWidth, MazeLength = mazeLength, stop = False, count=1)
                           
# testMaze.output_image("maze2.png")


# 0 = Init, 1 = Border, 2 = Start,, 3 = Path
# Init Maze
Puzzle = []
for i in range(mazeWidth):
    temp = []
    for j in range(mazeLength):
        temp.append(0)
    Puzzle.append(temp)

# Create Maze Border
for i in range(mazeWidth):
    #input("Prompt")
    for j in range(mazeLength):
        if (i == 0) or (i == mazeWidth - 1) or (j == 0) or (j == mazeLength-1):
            Puzzle[i][j] = 1

# Choose a random starting point
startChosen = False
while not startChosen:
    rnd_indxX = random.randrange(len(Puzzle))
    rnd_indxY = random.randrange(len(Puzzle[0]))

    if Puzzle[rnd_indxX][rnd_indxY] != 1:
        Puzzle[rnd_indxX][rnd_indxY] = 2
        startChosen = True

#Define Walls
# Puzzle[rnd_indxX+1][rnd_indxY-1] = 1
# Puzzle[rnd_indxX+1][rnd_indxY+1] = 1
# Puzzle[rnd_indxX-1][rnd_indxY-1] = 1
# Puzzle[rnd_indxX-1][rnd_indxY+1] = 1

def findCycle(Puzzle, x, y):
    if (Puzzle[x][y+1] == 3) and (Puzzle[x+1][y+1] == 3) and (Puzzle[x+1][y] == 3):
        cycle = True
    elif (Puzzle[x][y+1] == 3) and (Puzzle[x-1][y+1] == 3) and (Puzzle[x-1][y] == 3):
        cycle = True
    elif (Puzzle[x][y-1] == 3) and (Puzzle[x-1][y-1] == 3) and (Puzzle[x-1][y] == 3):
        cycle = True
    elif (Puzzle[x][y-1] == 3) and (Puzzle[x+1][y-1] == 3) and (Puzzle[x+1][y] == 3):
        cycle = True
    else:
        cycle = False
    return cycle
        

def chooseDirection(x, y, Puzzle):
    Direction = ['up','down','left','right']
    validPathChosen = False
    checkUP = False
    checkDN = False
    checkLT = False
    checkRT = False
    while not validPathChosen:
        step = random.choice(Direction)
        if step == 'up':
            if (Puzzle[x][y+1] == 0) and findCycle(Puzzle, x, y+1) == False:
                y += 1
                validPathChosen = True
            else:
                checkUP = True
        elif step =='down':
            if (Puzzle[x][y-1] == 0) and findCycle(Puzzle, x, y-1) == False:
                y -= 1
                validPathChosen = True
            else:
                checkDN = True
        elif step =='left':
            if (Puzzle[x-1][y] == 0) and findCycle(Puzzle, x-1, y) == False:
                x -= 1
                validPathChosen = True
            else:
                checkLT = True
        elif step =='right':
            if (Puzzle[x+1][y] == 0) and findCycle(Puzzle, x+1, y) == False:
                x += 1
                validPathChosen = True
            else:
                checkRT = True

        if checkRT and checkLT and checkDN and checkUP:
            print('No Valid Path')
            break
            
    return  x, y


x, y = chooseDirection(rnd_indxX, rnd_indxY, Puzzle)
Puzzle[x][y] = 3

for i in range(30):
    x, y = chooseDirection(x, y, Puzzle)
    Puzzle[x][y] = 3

    
output_image('filename.png', Puzzle)
