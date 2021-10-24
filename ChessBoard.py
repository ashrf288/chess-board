
import numpy as np
import matplotlib.pyplot as plt

class ChessBoard():
    def __init__(self):
        self.grid = np.zeros((8,8,3), np.float64)
     
        div = 1
        for i in range(8):
            for j in range(8):
                div = 0 if div else 1
                if i % 2 == div and j % 2 == div:
                    self.grid[i][j] = np.array((1,1,1))

    def  add_red (self,row,col):
        self.grid[row][col]=np.array(0,1,1)

    def render(self):
        plt.imshow(self.grid)