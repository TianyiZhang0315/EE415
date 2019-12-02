'''
Student Name: Tianyi Zhang
Student ID: 1868540
EightPuzzleWithManhattan.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.'''
from EightPuzzle import *
location = {0:[0,0],1:[0,1],2:[0,2],3:[1,0],4:[1,1],5:[1,2],6:[2,0],7:[2,1],8:[2,2]}
def h(s):  # heuristc using hamming distance
    total_h = 0
    for i in range(3):
        for j in range(3):
            total_h += abs(location[s.b[i][j]][0]-i)+abs(location[s.b[i][j]][1]-j)
    return total_h