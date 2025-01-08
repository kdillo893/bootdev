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
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")

    # initialize game states
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    delta = 0

    # grouping classes for object/state categories
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # initialize objects or classes of them
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    # enter game loop
    while True:
        # backdrop
        screen.fill((0, 0, 0))

        # process game events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update objects
        for obj in updatable:
            obj.update(delta)

        # check collisions
        for a in asteroids:
            if a.isColliding(player):
                print("Game over!")
                return

            for s in shots:
                if s.isColliding(a):
                    s.kill()
                    a.split()

        # draw objects
        for obj in drawable:
            obj.draw(screen)

        # Render updates
        pygame.display.flip()

        # tick wait, update time delta:
        delta = clock.tick(TICK_RATE) / 1000


if __name__ == "__main__":
    main()
