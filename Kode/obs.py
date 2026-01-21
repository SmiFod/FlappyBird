import pygame
import random

GREEN = (34, 139, 34)

class Obstacle:
    def __init__(self, x, screen_width, screen_height):
        self.x = x
        self.width = 50
        self.gap_size = 150  # Space between top and bottom pipes
        self.speed = 5
        
        # Randomize gap position (leaving margin from top and bottom)
        margin = 50
        self.gap_y = random.randint(margin, screen_height - self.gap_size - margin)
        
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def update(self):
        # Move obstacle to the left
        self.x -= self.speed
    
    def draw(self, screen):
        # Draw top pipe (green color)
        pygame.draw.rect(screen, (GREEN), 
                        (self.x, 0, self.width, self.gap_y))
        
        # Draw bottom pipe (green color)
        bottom_pipe_y = self.gap_y + self.gap_size
        pygame.draw.rect(screen, (GREEN), 
                        (self.x, bottom_pipe_y, self.width, 
                         self.screen_height - bottom_pipe_y))
    
    def is_off_screen(self):
        # Check if obstacle has passed the screen
        return self.x + self.width < 0
    
    def check_collision(self, bird):
        # Check if bird hits top or bottom pipe
        bird_left = bird.x - bird.radius
        bird_right = bird.x + bird.radius
        bird_top = bird.y - bird.radius
        bird_bottom = bird.y + bird.radius
        
        # Check if bird is horizontally aligned with obstacle
        if bird_left < self.x + self.width and bird_right > self.x:
            # Check collision with top pipe
            if bird_top < self.gap_y:
                return True
            # Check collision with bottom pipe
            if bird_bottom > self.gap_y + self.gap_size:
                return True
        
        return False
