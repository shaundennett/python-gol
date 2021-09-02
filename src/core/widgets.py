from _typeshed import StrPath
import pygame
import numpy as np
from pygame.constants import WINDOWHITTEST

class Button(pygame.sprite.Sprite):

    xpos=0
    ypos=0
    text="Default"
    width=0
    height=0
    colour=(255,255,255)
    command = None
    buttonGroup = None

    def __init__(self, xpos, ypos, text, width, height, colour):
        self.xpos = xpos
        self.ypos = ypos
        self.text = text
        self.width = width
        self.height = height    
        self.colour = colour
        self.butonGroup = pygame.sprite.Group()


    def addCommand(self, command):
        pass






if __name__ == "__main__":

    myButton = Button()

