#imports 
import pygame # type: ignore
from constants import *
import player

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
    player.Player.containers = (updatables, drawables)

     #Initialise individual spritesg
    p1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

     #Main game loop to imprement game funtionality
    while(True):
        screen.fill("black")
        updatables.update(dt) 
        for sprite in drawables:
             sprite.draw(screen) 

        for event in pygame.event.get(): # Implementing the exit button to close the game window
             if event.type == pygame.QUIT:
                  return
        pygame.display.flip() #refresh the screen
        dt = clk.tick(60)/1000


if __name__ == "__main__":
        main()
