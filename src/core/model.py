import numpy as np
import random
import math

from pygame.constants import QUIT

from core.widgets import current_milli_time


class Game_of_life_model:

    cols = 0
    rows = 0
    max = 0
    offsets = []
    base = np.array(0)
    last_grid = (0, 0)

    def __init__(self, cols, rows):
        """
        set up the play grid
        """
        self.cols = cols
        self.rows = rows
        self.max = self.cols * self.rows
        self.offsets = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        self.base = np.zeros(self.max, dtype="i")
        for x in range(self.max):
            if random.randint(0, 100) % 3 == 0:
                self.base[x] = 1

        self.grid = self.base.reshape(self.rows, self.cols)

    def check_cells(self) -> np.array:
        """
        Iterate through the grid and apply the rules to create a replacement grid

        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        counter = 0
        replacememt_grid = np.zeros(self.max, dtype="i").reshape(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                dead = False
                counter = 0
                # apply the rules by checking the offets for the current position
                for offset in self.offsets:
                    x_offset = i + offset[0]
                    y_offset = j + offset[1]

                    value = 0
                    if (
                        x_offset < 0
                        or x_offset > self.rows - 1
                        or y_offset < 0
                        or y_offset > self.cols - 1
                    ):
                        value = 0
                    else:
                        value = self.grid[x_offset, y_offset]
                    if value == 1:
                        counter = counter + 1
                        # print(counter)
                    if counter > 3:
                        dead = True
                        break
                if not dead:
                    if self.grid[i, j] == 1:
                        if counter >= 2 and counter <= 3:
                            replacememt_grid[i, j] = 1
                        else:
                            replacememt_grid[i, j] = 0
                    else:
                        if counter == 3:
                            replacememt_grid[i, j] = 1
                        else:
                            replacememt_grid[i, j] = 0

                else:
                    replacememt_grid[i, j] = 0
                # print("cell" + str(i) + ":" + str(j) + " current " + str(self.grid[i,j]) + " live cells " + str(counter) + " dead " + str(dead) + " final decision " + str(replacememt_grid[i,j]))

        self.grid = replacememt_grid.copy()
        return self.grid

    def display_grid(self):
        display_array = self.grid.astype("i")
        for i in range(self.rows):
            rowstring = ""
            for j in range(self.cols):
                rowstring = rowstring + str(display_array[i, j]) + " "
            print(rowstring)

        print("\n")

    def clear_grid(self):
        self.base = np.zeros(self.max, dtype="i")
        self.grid = self.base.reshape(self.rows, self.cols)

    def randomize_grid(self):
        self.base = np.zeros(self.max, dtype="i")
        for x in range(self.max):
            if random.randint(0, 100) % 3 == 0:
                self.base[x] = 1

        self.grid = self.base.reshape(self.rows, self.cols)

    def set_grid_point(self, pos):
        pass

    def change_cell(self, pos):

        current_cell_value = self.grid[pos[0]][pos[1]]

        self.grid[pos[0]][pos[1]] = abs(current_cell_value - 1)


if __name__ == "__main__":
    game = Game_of_life_model(20, 20)
    game.display_grid()
    game.check_cells()
    game.display_grid()
