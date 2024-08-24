# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

screen.fill((255, 255, 255))

def spaceForLetter(start, height, size):
    pygame.draw.line(screen, (255, 0, 0), (start, height), (start + size, height))


def showSpaceForLetters(numOfLetters, height, size):
    for i in range(numOfLetters):    
        spaceForLetter((i+4) * 100 , height, size)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Show the letter on the screen:
    showSpaceForLetters(9, 720/2, 60)
    showSpaceForLetters(6, 600, 40)
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()