import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.draw.circle) -> None:
        self.screen = pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.move = self.velocity * dt
        self.position += self.move

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 1
        log_event("asteroid_split")
        self.angle = random.uniform(20,50)
        self.new_angle1 = self.velocity.rotate(self.angle)
        self.new_angle2 = self.velocity.rotate(self.angle * -1)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        aster1 = Asteroid(self.position[0], self.position[1], self.new_radius)
        aster2 = Asteroid(self.position[0], self.position[1], self.new_radius)
        aster1.velocity = self.new_angle1 * 1.2
        aster2.velocity = self.new_angle2 * 1.2
        