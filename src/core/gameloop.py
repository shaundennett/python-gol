# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class GameLoop():

    # Define constants for the screen width and height
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Initialize pygame
    pygame.init()

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate the objects
    #player = Player()

    # Variable to keep the main loop running
    running = True

    # Main loop
    while running:
        # Look at every event in the queue
        self.manage_events()

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the objects on the screen
        
        #screen.blit(player.surf, player.rect)

        # Update the display
        pygame.display.flip()

    def manage_events(self):
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    self.running = False       
            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                self.running = False

if __name__ == "__main__":
    game = GameLoop()