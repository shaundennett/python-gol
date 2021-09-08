import numpy as np
import pygame
import core.model as gol_model
import core.game_view as gol_view


class GameController:

    rows = 50
    cols = 50
    screen = None
    box_x = 0
    box_y = 0
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)

    model = None
    view = None

    def __init__(self):
        pygame.init()
        self.model = gol_model.Game_of_life_model(self.cols, self.rows)
        self.view = gol_view.GameView(self.model, pygame)

        self.main_loop()

    def main_loop(self):
        running = True
        clock = pygame.time.Clock()
        while running:

            # Did the user click the window close button?
            draw = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    draw = True

          
            # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
            draw = True
            if draw:
                self.view.draw()
            clock.tick(10)


if __name__ == "__main__":
    worker = GameController()
