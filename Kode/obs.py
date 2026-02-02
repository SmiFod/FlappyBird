import pygame
import random

GREEN = (34, 139, 34)

class Obstacle:
    def __init__(self, x, screen_width, screen_height):
        self.x = x
        self.width = 50
        self.gap_size = 150  # Space between top and bottom pipes
        self.speed = 5
        self.passed = False  # Track if bird has passed this obstacle
        
        # Randomize gap position (leaving margin from top and bottom)
        margin = 75
        self.gap_y = random.randint(margin, screen_height - self.gap_size - margin)
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Load pipe images
        try:
            self.top_pipe_image = pygame.image.load("top_pipe.png")
            self.top_pipe_image = pygame.transform.scale(self.top_pipe_image, (self.width, self.gap_y))
            self.bottom_pipe_image = pygame.image.load("bottom_pipe.png")
            bottom_pipe_height = self.screen_height - self.gap_y - self.gap_size
            self.bottom_pipe_image = pygame.transform.scale(self.bottom_pipe_image, (self.width, bottom_pipe_height))
            self.use_images = True
        except:
            self.use_images = False
    
    def update(self):
        # Move obstacle to the left
        self.x -= self.speed
    
    def draw(self, screen):
        if self.use_images:
            # Draw top pipe image
            screen.blit(self.top_pipe_image, (self.x, 0))
            
            # Draw bottom pipe image
            bottom_pipe_y = self.gap_y + self.gap_size
            screen.blit(self.bottom_pipe_image, (self.x, bottom_pipe_y))
        else:
            # Draw top pipe (green color) - fallback
            pygame.draw.rect(screen, (GREEN), 
                            (self.x, 0, self.width, self.gap_y))
            
            # Draw bottom pipe (green color) - fallback
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
    
