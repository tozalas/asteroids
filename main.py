import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    # Initialize pygame and create the main window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Sprite groups for managing game objects
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign sprite containers for each class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create the player and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0  # Delta time for frame updates

    while True:
        # Handle events (e.g., window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all updatable sprites
        updatable.update(dt)

        # Check for collisions between asteroids and player/shots
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game Over!")
                sys,exit()  # Exit the game on collision with player
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()  # Split asteroid on shot collision
                    shot.kill()       # Remove the shot

        # Clear the screen
        screen.fill("black")

        # Draw all drawable sprites
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Limit the framerate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
