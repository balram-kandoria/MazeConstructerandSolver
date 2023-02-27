from main import *

mazeWidth = 35
mazeLength = 35
defaultWall = 5

# testMaze = Maze(mazeWidth, mazeLength, (0,0), (20,20))

# area = mazeLength*mazeWidth

# testMaze.mazeBorderCreate()
# testMaze.output_image("maze1.png")

# testMaze.RecursiveDevision(startx = 0, endx = mazeWidth, starty = 0, endy = mazeLength, mode = 0, startxin=0, endxin = mazeWidth, startyin = 0, endyin = mazeLength, resolution =300
#                            , MazeWidth = mazeWidth, MazeLength = mazeLength, stop = False, count=1)

# testMaze.output_image("maze2.png")


maze = Maze(mazeWidth, mazeLength, defaultWall)

maze.set_algGenerate('Aldous-Broder algorithm')
