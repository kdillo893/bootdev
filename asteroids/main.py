import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE
)


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(screen)
    gameLoop(screen)

    pass


def gameLoop(screen):

    while True:
        # process events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        # screen refresh after changes made
        pygame.display.flip()


if __name__ == "__main__":
    main()
