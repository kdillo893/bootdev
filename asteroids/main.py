import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE
)
from player import Player


def main():
    print("Starting asteroids!")

    # initialize game states
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    delt = 0

    # initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    gameLoop(screen, clock, delt, player)

    pass


def gameLoop(screen, clock, delt, player):

    while True:
        # process events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        player.draw(screen)

        # screen refresh after changes made
        pygame.display.flip()
        # tick wait:
        delt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
