import numpy as np
import pygame
import model as gol_model

class GameView():

    rows = 50
    cols = 50
    screen = None
    box_x = 0
    box_y = 0
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)

    model = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([500, 700])
        ## calculate the box sizes
        self.box_x = 500 / self.cols
        self.box_y = 500 / self.rows
        self.model = gol_model.Game_of_life_model(self.cols, self.rows)
        self.main_loop()


    def create_grid(self):

        pos_x = 0
        pos_y = 0
        colour = self.GREEN
        grid = self.model.check_cells()
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i,j] == 1:
                     pygame.draw.rect(self.screen, colour, (pos_x, pos_y, self.box_x, self.box_y),1)
                else:
                     pygame.draw.rect(self.screen, colour, (pos_x, pos_y, self.box_x, self.box_y))
               
                #pygame.display.flip()
                pos_x = pos_x + self.box_x
            pos_x = 0
            pos_y = pos_y + self.box_y    

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



            # Draw a solid blue circle in the center
            #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
            draw = True
            if draw:
                self.screen.fill(self.BLACK)
                self.create_grid()
                # Flip the display
                pygame.display.flip()
            clock.tick(10)


if __name__ == "__main__":
   worker = GameView()
