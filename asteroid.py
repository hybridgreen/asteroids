import circleshape
import pygame #type:ignore
import constants

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
    