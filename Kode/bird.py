# c:\Users\Sami Fouad\OneDrive - Osloskolen\Documents\GitHub\FlappBird\Kode\bird.py
import pygame

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.velocity = 0
        self.gravity = 0.5
        self.max_fall_speed = 10

    def update(self):
        # Gravity pulls the bird down
        self.velocity += self.gravity
        self.velocity = min(self.velocity, self.max_fall_speed)
        self.y += self.velocity

    def flap(self):
        # Bird jumps up when flapping
        self.velocity = -12

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), self.radius)

    def is_off_screen(self, screen_height):
        # Check if bird hit top or bottom
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            return True
        return False