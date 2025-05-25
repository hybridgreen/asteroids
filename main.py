#imports 
import pygame # type: ignore
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() #Initialise all pygame modules
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Setup game screen object
    clk = pygame.time.Clock()
    dt = 0
    while(True):
        screen.fill("black")
        for event in pygame.event.get(): # Implementing the exit button to close the game window
             if event.type == pygame.QUIT:
                  return
        pygame.display.flip() #refresh the screen
        dt = clk.tick(60)/1000



if __name__ == "__main__":
        main()
