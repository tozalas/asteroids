import pygame
import random
from asteroid import Asteroid
from constants import *

# AsteroidField manages spawning asteroids at the edges of the screen
class AsteroidField(pygame.sprite.Sprite):
    # Define possible spawn edges and their directions/positions
    edges = [
        [
            pygame.Vector2(1, 0),  # Rightward velocity (spawn on left edge)
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),  # Leftward velocity (spawn on right edge)
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),  # Downward velocity (spawn on top edge)
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),  # Upward velocity (spawn on bottom edge)
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        # Initialize the sprite and spawn timer
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        # Create a new asteroid at the given position, size, and velocity
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        # Update the spawn timer and spawn asteroids at intervals
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Randomly select an edge to spawn a new asteroid
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))  # Add some angle variation
            position = edge[1](random.uniform(0, 1))  # Random position along the edge
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)