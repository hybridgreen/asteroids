import circleshape
import pygame #type:ignore
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        pass

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(split_angle)
            velocity2 = self.velocity.rotate(-1 * split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            spawn1 = Asteroid(self.position.x, self.position.y,new_radius)
            spawn1.velocity = velocity1 * 1.2
            spawn2 = Asteroid(self.position.x, self.position.y,new_radius)
            spawn2.velocity = velocity2 * 1.2
        pass