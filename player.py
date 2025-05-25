from circleshape import CircleShape
from constants import *
import pygame # type: ignore
import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.cooldown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius/1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        super().draw(screen)
        pygame.draw.polygon(screen, "white", self.triangle(),2)
        pass

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED*dt
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.cooldown -= dt
        if keys[pygame.K_a]:
            self.rotate(-1*dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                pass
            else:
                self.shoot(dt)
        pass

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) 
        self.position += forward* PLAYER_SPEED * dt
        pass

    def shoot(self,dt):
        s1 = Shot.Shot(self.position.x,self.position.y)
        s1.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        s1.update(dt)
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        pass