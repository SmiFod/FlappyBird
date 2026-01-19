import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
YELLOW = (255, 255, 0)
RED = (220, 20, 60)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird!")
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with background color
    screen.fill((135, 206, 235))  # Sky blue
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()