import pygame
from PIL import Image
import os

class Button(pygame.sprite.Sprite):

    xpos = 0
    ypos = 0
    width = 0
    height = 0
    colour = (255, 255, 255)
    command = None
    buttonGroup = None
    pygame = None
    imageName = None
    image = None

    def __init__(self, xpos, ypos, width, height, image, pygame):

        super().__init__()
        self.pygame = pygame
        self.xpos = xpos
        self.ypos = ypos

        self.image = image
        self.rect = self.image.get_rect()
        # image = image.resize((500,500),Image.ANTIALIAS)

    def addCommand(self, command):
        self.command = command

    def update(self):
        self.pygame.blit(self.image, self.rect)


    def on_click(event):
        pass
