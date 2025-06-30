import pygame
from circleshape import CircleShape
from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS, \
    ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
    

    def update(self, dt):
        self.position += self.velocity * dt
    

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        elif self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            asteroid1.velocity = v1 * 1.2
            asteroid2.velocity = v2 * 1.2
            self.kill()