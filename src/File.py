from Solver import *
from random import shuffle
import numpy as np
class File:
    def __init__(self):
        pass
    
    # fungsi untuk mengubah file txt menjadi matriks
    def txtToMatriks(self, filename):
        matrix = []
        with open(filename) as f:
            for item in f:
                matrix.append([int(i) for i in item.split()])
        puzzle = Solver()
        puzzle.matriks = matrix
        return puzzle
    
    # fungsi untuk melakukan pengacakan matriks
    def randomizer(self):
        puzzle = [i+1 for i in range(16)]
        shuffle(puzzle)
        matriks = np.reshape(puzzle, (4,4)).astype('int32')
        Puzzle = Solver()
        Puzzle.matriks = matriks
        return Puzzle
        