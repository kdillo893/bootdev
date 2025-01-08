import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        pass

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, delta):
        self.rotation += delta * PLAYER_TURN_SPEED

    def update(self, delta):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-delta)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(delta)

        # todo movement forward/back

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
