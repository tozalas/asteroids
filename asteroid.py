import pygame
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS, \
    ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE
import random

# Asteroid class represents an asteroid object in the game.
# Inherits from CircleShape for position, radius, and velocity.
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Initialize asteroid with position (x, y) and radius.
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a white circle outline on the given screen.
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        # Update the asteroid's position based on its velocity and the time delta.
        self.position += self.velocity * dt
    
    def split(self):
        # Split the asteroid into two smaller asteroids if possible.
        if self.radius <= ASTEROID_MIN_RADIUS:
            # If the asteroid is too small, remove it from the game.
            self.kill()
        elif self.radius > ASTEROID_MIN_RADIUS:
            # Otherwise, create two smaller asteroids with rotated velocities.
            angle = random.uniform(20, 50)
            
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            asteroid1.velocity = v1 * 1.2
            asteroid2.velocity = v2 * 1.2
            # Remove the original asteroid after splitting.
            self.kill()