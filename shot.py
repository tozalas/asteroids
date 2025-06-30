import pygame
from circleshape import CircleShape
from constants import *

# Shot class represents a projectile in the game, inheriting from CircleShape
class Shot(CircleShape):
    def __init__(self, x, y):
        # Initialize the shot at position (x, y) with a predefined radius
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Draw the shot as a white circle outline on the given screen
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Update the shot's position based on its velocity and the elapsed time (dt)
        self.position += self.velocity * dt