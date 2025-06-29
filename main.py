# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
import player


def main():
    pygame.init()

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    user = player.player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            user.update(dt)
            screen.fill((0,0,0))  # Fill the screen with the background color
            user.draw(screen)
            pygame.display.flip()  # Update the display
            dt = clock.tick(60) / 1000


    
    # print("Starting Asteroids!")
    # print(f"Screen width: {constants.SCREEN_WIDTH}")
    # print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()