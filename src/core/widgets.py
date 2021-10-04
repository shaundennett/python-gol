import pygame
from PIL import Image

class Button(pygame.sprite.Sprite):

    xpos = 0
    ypos = 0
    width = 0
    height = 0
    colour = (255, 255, 255)
    command = None

    def __init__(self, xpos, ypos, width, height, image, pygame, screen):

        super().__init__()

        self.screen = screen
        self.pygame = pygame
        self.xpos = xpos
        self.ypos = ypos
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        # image = image.resize((500,500),Image.ANTIALIAS)
        self.rect.topleft = (xpos, ypos)
    
    def addCommand(self, command):
        self.command = command

    def update(self):
        self.xpos = self.xpos + 0.01
        self.rect.topleft = (self.xpos, self.ypos)

    #def draw(self, screen):
    #    
    #    self.screen.blit(self.image, (self.xpos, self.ypos))

    def on_click(self, event):
        pass
