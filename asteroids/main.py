import pygame

from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE,
    TICK_RATE
)
from player import Player


def main():
    print("Starting asteroids!")

    # initialize game states
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    delta = 0

    # initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # enter game loop
    gameLoop(screen, clock, delta, player)


def gameLoop(screen, clock, delta, player):

    while True:
        # backdrop
        screen.fill((0, 0, 0))
        
        # process game events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update objects:
        player.update(delta)

        # draw objects on screen
        player.draw(screen)

        # Render updates
        pygame.display.flip()

        # tick wait, update time delta:
        delta = clock.tick(TICK_RATE) / 1000


if __name__ == "__main__":
    main()
