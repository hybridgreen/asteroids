#imports 
import pygame # type: ignore
from constants import *
import player
import asteroid
import AsteroidField
import sys
import Shot

def main():
    print("Starting Asteroids!")
    pygame.init() #Initialise all pygame modules

     # Create game environment. Screen and clock control FPS
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clk = pygame.time.Clock()
    dt = 0

     # Create object groups to facilitate updates sprites
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatables, drawables)
    asteroid.Asteroid.containers = (updatables,drawables,asteroids)
    AsteroidField.AsteroidField.containers = (updatables)
    Shot.Shot.containers = (updatables,drawables,shots)



     #Initialise individual spritesg
    p1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    af = AsteroidField.AsteroidField()

     #Main game loop to imprement game funtionality
    while(True):
        screen.fill("black")
        updatables.update(dt)

        for ast in asteroids:
             for shot in shots:
                  if (ast.colliding_with(shot)):
                       shot.kill()
                       ast.split()
                  
             if(ast.colliding_with(p1)):
                  print("Game Over!")
                  sys.exit()
               

        for sprite in drawables:
             sprite.draw(screen) 

        for event in pygame.event.get(): # Implementing the exit button to close the game window
             if event.type == pygame.QUIT:
                  return
        pygame.display.flip() #refresh the screen
        dt = clk.tick(60)/1000


if __name__ == "__main__":
        main()
