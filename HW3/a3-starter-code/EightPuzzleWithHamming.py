'''
Student Name: Tianyi Zhang
Student ID: 1868540
EightPuzzleWithHamming.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.'''
from EightPuzzle import *
goal = [[0,1,2],[3,4,5],[6,7,8]]
def h(s):  # heuristc using hamming distance
    total_h = 0
    for i in range(3):
        for j in range(3):
            if goal[i][j] != s.b[i][j] and s.b[i][j] != 0:
                total_h += 1
    return total_h

