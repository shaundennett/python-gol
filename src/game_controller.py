import numpy as np
import pygame
import core.model as gol_model
import core.game_view as gol_view
import core.widgets as widgets
from PIL import Image as image

class GameController:

    rows = 50
    cols = 50
    screen = None
    box_x = 0
    box_y = 0
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    #modes
    STOPPED = 0
    RUNNING = 1
    PLOTTING = 2

    mode = STOPPED

    def __init__(self):
        pygame.init()
        self.model = gol_model.Game_of_life_model(self.cols, self.rows)
        self.view = gol_view.GameView(self.model, pygame)
        self.setup_event_listeners()
        self.main_loop()


    def setup_event_listeners(self):
        self.view.button_start_stop.add_command(self.start_stop_clicked)

    def start_stop_clicked(self, val):
        print("Button state :" + str(val))
        if val == 0:
            self.draw = False
        else:
            self.draw = True
   
    def reset_clicked(self):
        pass

    def main_loop(self):
        running = True
        clock = pygame.time.Clock()
        self.draw = True
        while running:

            # Did the user click the window close button?
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    
            if self.draw:
                self.model.check_cells()
          
            # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
            #draw = True
            self.view.draw()
            clock.tick(10)


if __name__ == "__main__":
    worker = GameController()
