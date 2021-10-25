from numpy.lib.type_check import imag
import pygame
from PIL import Image
import time


def current_milli_time():
    return round(time.time() * 1000)


class Button_toggler(pygame.sprite.Sprite):

    toggles = 0
    current_state = 0
    colour = (255, 255, 255)
    command = None
    last_clicked = 0
    enabled = True
    disabled_state = 0

    def __init__(self, xpos, ypos, width, height, image_names, pygame):

        super().__init__()
        self.images = []
        self.disabled = []
        self.pygame = pygame
        self.xpos = xpos
        self.ypos = ypos
        # self.image = pygame.transform.scale(image, (width, height))
        self.setup_images(image_names, width, height)
        self.image = self.images[self.current_state]
        ##self.image.set_alpha(10)
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos, ypos)

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def setup_images(self, image_names, width, height):

        self.toggles = len(image_names) - 1
        for image_name in image_names:
            self.images.append(pygame.transform.scale(image_name, (width, height)))
            
            
        self.current_state = 0

    def add_command(self, command):
        self.command = command

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
#        if self.enabled:
#               self.image.set_alpha(10)
#        else:
#           self.image.set_alpha(50)

        self.rect.topleft = (self.xpos, self.ypos)
        if click == (1, 0, 0):
            print(mouse)
            self.check_events(mouse)

    def check_events(self, mouse):

        if current_milli_time() - self.last_clicked > 300 and self.enabled:
            if pygame.Rect.collidepoint(self.rect, mouse):
                print(self.current_state)
                if self.current_state == self.toggles:
                    self.current_state = 0
                else:
                    self.current_state = self.current_state + 1
                self.image = self.images[self.current_state]
                self.rect = self.image.get_rect()
                self.rect.topleft = (self.xpos, self.ypos)
               
                if self.command is not None:
                    self.command(self.current_state)
            self.last_clicked = current_milli_time()
