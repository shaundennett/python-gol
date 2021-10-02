import numpy as np
import pygame
import core.model as model
import core.widgets as widgets
from PIL import Image as image


class GameView:

    rows = 50
    cols = 50
    screen = None
    box_x = 0
    box_y = 0
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)

    model = None
    pygame = None

    button = None
    buttons = None

    def __init__(self, model, game):

        self.pygame = game
        self.screen = pygame.display.set_mode([500, 700])
        ## calculate the box sizes
        self.box_x = 500 / self.cols
        self.box_y = 500 / self.rows
        self.model = model
        self.buttons = pygame.sprite.Group()

    def add_button(self, x, y, height, width, image):

        self.button = widgets.Button(x, y, height, width , image, self.screen)
        self.buttons.add(self.button)

    def create_grid(self):

        pos_x = 0
        pos_y = 0
        colour = self.GREEN
        grid = self.model.check_cells()
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i, j] == 1:
                    pygame.draw.rect(
                        self.screen, colour, (pos_x, pos_y, self.box_x, self.box_y), 1
                    )
                else:
                    pygame.draw.rect(
                        self.screen, colour, (pos_x, pos_y, self.box_x, self.box_y)
                    )

                # pygame.display.flip()
                pos_x = pos_x + self.box_x
            pos_x = 0
            pos_y = pos_y + self.box_y

    def draw(self):
        self.screen.fill(self.BLACK)
        self.create_grid()
        self.show_buttons()
        # Flip the display
        pygame.display.flip()
    
    def show_buttons(self):
        self.buttons.update()

if __name__ == "__main__":
    worker = GameView()
