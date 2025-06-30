import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

# Player class represents the player-controlled ship, inheriting from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Ship's current rotation angle in degrees
        self.cool_down = 0.0  # Time remaining before next allowed shot

    def draw(self, screen):
        # Draw the player as a triangle (ship) on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        # Calculate the three points of the ship's triangle based on position and rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        # Handle player input and update state each frame
        keys = pygame.key.get_pressed()
        self.cool_down = max(0.0, self.cool_down - dt)  # Update shooting cooldown

        if keys[pygame.K_w]:
            self.move(dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right
        if keys[pygame.K_SPACE]:
            self.shoot(dt)  # Attempt to shoot

    def rotate(self, dt):
        # Rotate the ship by a fixed speed
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # Move the ship forward or backward based on rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        # Shoot a projectile if cooldown has elapsed
        if self.cool_down <= 0.0:
            self.cool_down = PLAYER_SHOOT_RATE  # Reset cooldown
            shoot = Shot(self.position.x, self.position.y)
            shoot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
