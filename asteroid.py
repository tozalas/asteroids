import pygame
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS, \
    ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt