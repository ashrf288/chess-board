
import numpy as np
import matplotlib.pyplot as plt

class ChessBoard():
    def __init__(self):
        self.grid = np.zeros((8,8,3), np.float64)
        # self.black = (0,0,0)
        # self.white = (1,1,1)
        # self.blue = (0,1,1)
        # self.red = (1,2,0)
        div = 1
        for i in range(8):
            for j in range(8):
                div = 0 if div else 1
                if i % 2 == div and j % 2 == div:
                    self.grid[i][j] = np.array((1,1,1))
    def render(self):
        plt.imshow(self.grid)