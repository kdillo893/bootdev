import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOT_COOLDOWN,
    SHOT_RADIUS
)

from shot import Shot


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shotTimer = 0.0
        self.rotation = 0.0

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

    def move(self, delta):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta

    def shoot(self):
        # create a shot moving forward (our rotation) at shot speed
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        # put shot on cooldown
        self.shotTimer = PLAYER_SHOT_COOLDOWN

    def update(self, delta):
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-delta)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(delta)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(delta)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-delta)

        # shooting
        if self.shotTimer < 0 and keys[pygame.K_SPACE]:
            self.shoot()

        # player variables to update
        self.shotTimer -= delta

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
