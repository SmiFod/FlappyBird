import pygame
import random
import sys
from bird import Bird
from obs import Obstacle

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

# Create button
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = GREEN
        self.text_color = WHITE
        self.font = pygame.font.Font(None, 32)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create bird
bird = Bird(50, SCREEN_HEIGHT // 2)

# Create button
start_button = Button(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2, 150, 60, "START")

# Create obstacle list
obstacles = []
obstacle_spawn_timer = 0
obstacle_spawn_interval = 100  # Spawn new obstacle every 100 frames

# Game states
game_started = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                if start_button.is_clicked(event.pos):
                    game_started = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    game_started = True
                else:
                    bird.flap()
    
    # Fill screen with background color
    screen.fill((135, 206, 235))  # Sky blue
    
    if not game_started:
        # Draw start screen
        title_font = pygame.font.Font(None, 60)
        title_text = title_font.render("Flappy Bird", True, BLACK)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_text, title_rect)
        
        start_button.draw(screen)
        
        # Draw instruction text
        instruction_font = pygame.font.Font(None, 24)
        instruction_text = instruction_font.render("Press SPACE to start", True, BLACK)
        instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(instruction_text, instruction_rect)
    else:
        # Update bird
        bird.update()
        
        # Spawn new obstacles
        obstacle_spawn_timer += 1
        if obstacle_spawn_timer >= obstacle_spawn_interval:
            obstacles.append(Obstacle(SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT))
            obstacle_spawn_timer = 0
        
        # Update and remove off-screen obstacles
        for obstacle in obstacles[:]:
            obstacle.update()
            if obstacle.is_off_screen():
                obstacles.remove(obstacle)
        
        # Check collisions with obstacles
        for obstacle in obstacles:
            if obstacle.check_collision(bird):
                print("Game Over! You hit an obstacle!")
                game_started = False
                obstacles = []
        
        # Check if bird hit top or bottom
        if bird.is_off_screen(SCREEN_HEIGHT):
            print("Game Over! You hit the ground or ceiling!")
            game_started = False
            obstacles = []
        
        # Draw obstacles
        for obstacle in obstacles:
            obstacle.draw(screen)
        
        # Draw bird
        bird.draw(screen)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()