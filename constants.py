# constants.py
# This file contains game configuration constants for the Asteroids game.

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Asteroid properties
ASTEROID_MIN_RADIUS = 20           # Minimum radius of an asteroid
ASTEROID_KINDS = 3                 # Number of asteroid size types
ASTEROID_SPAWN_RATE = 0.8          # Time (in seconds) between asteroid spawns
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Maximum asteroid radius

# Player properties
PLAYER_RADIUS = 20                 # Radius of the player's ship
PLAYER_TURN_SPEED = 300            # Player's turning speed (degrees per second)
PLAYER_SPEED = 200                 # Player's movement speed (pixels per second)
PLAYER_SHOOT_RATE = 0.3            # Minimum time (in seconds) between shots

# Shot properties
SHOT_RADIUS = 5                    # Radius of a shot/bullet
SHOT_SPEED = 500                   # Speed of a shot (pixels per second)