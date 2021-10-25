import numpy as np
import pygame
import math
import core.model as model
import core.widgets as widgets
from PIL import Image


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
    screen = None
    button = None
    buttons = None

    def __init__(self, model, game):

        self.pygame = game
        self.screen = pygame.display.set_mode((500, 600))
        ## calculate the box sizes
        self.grid_width = 500
        self.grid_height = 500
        self.gridrect = pygame.Rect(0, 0, 500, 500)
        self.box_x = self.grid_width / self.cols
        self.box_y = self.grid_height / self.rows
        self.model = model
        self.buttons = pygame.sprite.Group()
        self.create_button_section()

    def create_button_section(self):

        button_stop_img = pygame.image.load("src\\images\\button_stop.png")
        button_start_img = pygame.image.load("src\\images\\button_start.png")
        button_reset_img = pygame.image.load("src\\images\\button_reset.png")
        self.button_random_enabled_img = pygame.image.load("src\\images\\button_random_active.png").convert_alpha()
        self.button_random_enabled_img.set_alpha(50)

        self.button_start_stop = widgets.Button_toggler(
            10, 520, 80, 30, [button_start_img, button_stop_img], self.pygame
        )
        self.button_reset = widgets.Button_toggler(
            100, 520, 80, 30, [button_reset_img], self.pygame
        )
        self.button_random = widgets.Button_toggler(
            200, 520, 80, 30, [self.button_random_enabled_img], self.pygame
        )

        self.buttons.add(self.button_reset, self.button_start_stop, self.button_random)

    def create_grid(self):

        pos_x = 0
        pos_y = 0
        colour = self.GREEN
        grid = self.model.grid
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i, j] == 1:
                    pygame.draw.rect(
                        self.screen, colour, (pos_x, pos_y, self.box_x, self.box_y)
                    )
                else:
                    pygame.draw.rect(
                        self.screen, colour, (pos_x, pos_y, self.box_x, self.box_y), 1
                    )

                # pygame.display.flip()
                pos_x = pos_x + self.box_x
            pos_x = 0
            pos_y = pos_y + self.box_y

    def draw(self):
        self.screen.fill(self.BLACK)
        self.create_grid()
        self.buttons.update()
        self.buttons.draw(self.screen)
        # self.show_buttons(self.screen)
        # Flip the display
        pygame.display.flip()

    def show_buttons(self, screen):
        self.button.draw(screen)

    def is_in_grid(self, pos) -> bool:
        if pos[0] > 0 and pos[0] <= 500 and pos[1] > 0 and pos[1] <= 500:
            return True
        else:
            return False

    def get_grid_pos(self, pos) -> tuple:
        if self.is_in_grid(pos):
            x = math.floor(pos[0] / self.box_x)
            y = math.floor(pos[1] / self.box_y)
            print(str(pos) + " " + str(x) + " " + str(y))
            return (y, x)
        else:
            return 0.0


if __name__ == "__main__":
    worker = GameView()
