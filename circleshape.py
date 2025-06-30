import pygame 

# circleshape.py
# Defines a base class for circular game objects using pygame's Sprite system.

# Base class for game objects with a circular shape
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # If 'containers' attribute exists, pass it to the Sprite initializer (for sprite groups)
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # Position of the circle (center)
        self.position = pygame.Vector2(x, y)
        # Velocity vector (default stationary)
        self.velocity = pygame.Vector2(0, 0)
        # Radius of the circle
        self.radius = radius

    def draw(self, screen):
        # Placeholder: should be overridden by subclasses to draw the shape
        pass

    def update(self, dt):
        # Placeholder: should be overridden by subclasses to update the object each frame
        pass

    def collide(self, other):
        # Returns True if this circle collides with another circle (distance < sum of radii)
        return self.position.distance_to(other.position) < (self.radius + other.radius)