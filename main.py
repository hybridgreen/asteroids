#imports 
import pygame # type: ignore
from constants import *
import player

def main():
    print("Starting Asteroids!")
    pygame.init() #Initialise all pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Setup game screen object
    clk = pygame.time.Clock()
    dt = 0
    p1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while(True):
        screen.fill("black")
        p1.update(dt) 
        p1.draw(screen) # render the player
        for event in pygame.event.get(): # Implementing the exit button to close the game window
             if event.type == pygame.QUIT:
                  return
        pygame.display.flip() #refresh the screen
        dt = clk.tick(60)/1000


if __name__ == "__main__":
        main()
