from circleshape import CircleShape
from constants import *
import pygame # type: ignore

class Shot(CircleShape):
    
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        
    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)
    
    def update(self, dt):
        super().update(dt)
        self.position += self.velocity*dt