import numpy as np
import random
cols = 20
rows = 20
max = cols * rows

offsets = [(-1, -1),
           (-1, 0),
           (-1, 1),
           (0, -1),
           (0, 1),
           (1, -1),
           (1, 0),
           (1, 1),
           ]
base = np.zeros(max)
for x in range(max):
    if random.randint(0, 9) % 3 == 0:
        base[x] = 1

grid = base.reshape(rows, cols)


def check_cells(min, max, grid,  row, col, offsets):
    counter = 0

 
        


#if __name__ == "__main__":
