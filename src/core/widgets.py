import pygame
from PIL import Image

class Button(pygame.sprite.Sprite):

    xpos = 0
    ypos = 0
    width = 0
    height = 0
    colour = (255, 255, 255)
    command = None

    def __init__(self, xpos, ypos, width, height, image, pygame):

        super().__init__()

        self.pygame = pygame
        self.xpos = xpos
        self.ypos = ypos
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos, ypos)
    
    def addCommand(self, command):
        self.command = command

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        self.rect.topleft = (self.xpos, self.ypos)
        if click == (1,0,0):
            print(mouse)
            self.check_events(mouse)        

    def check_events(self, mouse):
       if pygame.Rect.collidepoint(self.rect, mouse):
          print("clicked")
