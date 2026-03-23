import pygame
from engine import GameEngine

def main():
    pygame.init()
    engine = GameEngine()
    engine.run()
    pygame.quit()

if __name__ == "__main__":
    main()