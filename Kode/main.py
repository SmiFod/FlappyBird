import pygame
import random
import sys
from bird import Bird

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

# Create bird
bird = Bird(50, SCREEN_HEIGHT // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()
    
    # Update bird
    bird.update()
    
    # Fill screen with background color
    screen.fill((135, 206, 235))  # Sky blue
    
    # Draw bird
    bird.draw(screen)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()