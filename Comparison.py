from BFS import BFS
from Depth_First_Search import DFS

from Randomized_Prims_algorithm import randomizedPrimsAlg, output_image_Prims

width = 25
length = 25
wall = 3

Puzzle = randomizedPrimsAlg(width, length, wall)

Puzzle = BFS(Puzzle, width, length)

Puzzle = DFS(Puzzle, width, length)
