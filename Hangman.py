# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

screen.fill((255, 255, 255))


def showSpaceForLetters(numOfLetters, height, size):
    for i in range(numOfLetters):
        pygame.draw.line(screen, (255, 0, 0), ((i+4) * 100, height), ((i+4) * 100 + size, height))

def write(word, xPosition, yPosition, fontSize):
    font = pygame.font.SysFont("Arial", fontSize)
    textsurface = font.render(word, True, blue)
    screen.blit(textsurface,(xPosition - textsurface.get_width() // 2, yPosition - textsurface.get_height() // 2))
    #pygame.Surface.blit(textsurface, screen, (xPosition...))

words = ["Hangman", "input", "book"]
correct_letters = []
wrong_letters = []

def writeUserKey(keycode, letter, position):
    keys = pygame.key.get_pressed()
    if keys[keycode]:
        write(letter, position[0], position[1], 24)


def allTheLetters():
    return range(pygame.K_a, pygame.K_z + 1)

def setWord(wordList):
    word = wordList[random.randint(0, len(wordList))]
    for i in range(len(word)):
        correct_letters.append(word[i])

def letterCheck(letter):
    for i in range(len(correct_letters)):
        if letter == correct_letters[i]:
            write(letter, (i+4) * 100, 379, 36)

setWord(words)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     #print("keys = ", keys)


    y = 0
    for keycode in allTheLetters():
        letter = chr(keycode)
        writeUserKey(keycode, letter, (1200, 20 + (y*26) ))
        letterCheck(letter)
        y = y + 1
    #writeUserKey(pygame.K_s, "S", (1200, 60))

    # Show the letter on the screen:
    showSpaceForLetters(len(correct_letters), 720/2, 60)
    showSpaceForLetters(6, 600, 40)
    write("Wrong Letters:", 620, 425, 36)
    
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()