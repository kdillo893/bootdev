import pygame
import random

from circleshape import CircleShape
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE
)


class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, delta):
        self.position += self.velocity * delta

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # spawning splits of asteroid
        # random angle split
        splitAngle = random.uniform(20, 50)
        newVec1 = self.velocity.rotate(splitAngle)
        newVec2 = self.velocity.rotate(-splitAngle)

        newRad = self.radius - ASTEROID_MIN_RADIUS

        # create new asteroids with the values
        Asteroid(self.position.x, self.position.y,
                 newRad).velocity = newVec1 * 1.2
        Asteroid(self.position.x, self.position.y,
                 newRad).velocity = newVec2 * 1.2
