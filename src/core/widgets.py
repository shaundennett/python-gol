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
        self.check_events()        

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("clicked")
