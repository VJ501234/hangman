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

words = ["hangman", "input", "book"]
correct_letters = []
wrong_letters = []
correctWord = None
lettersOnScreen = []

def writeUserKey(keycode, letter, position):
    keys = pygame.key.get_pressed()
    if keys[keycode]:
        write(letter, position[0], position[1], 24)


def allTheLetters():
    return range(pygame.K_a, pygame.K_z + 1)


def setWord(wordList):
    global correctWord
    correctWord = wordList[random.randint(0, len(wordList) - 1)]
    for i in range(len(correctWord)):
        correct_letters.append(correctWord[i])


def letterCheck(keycode, letter):
    isLetterCorrect = False
    keys = pygame.key.get_pressed()
    if keys[keycode]:
        print("keycode = ", keycode)
        for i in range(len(correct_letters)):
            print("i=", i)
            if letter == correct_letters[i]:
                write(letter, (i+4.35) * 100, 341, 36)
                isLetterCorrect = True
                
                #break
        if isLetterCorrect:
            #write(letter, (i+4.35) * 100, 341, 36)
            print(letter, " is correct")

            # if the letter is not in wrongletters, then add it.
            if letter not in lettersOnScreen:
                lettersOnScreen.append(letter)
        else:
            print(letter, " isn't correct")

            # if the letter is not in wrongletters, then add it.
            if letter not in wrong_letters:
                wrong_letters.append(letter)
            # then, write out all the wrong letters.
                for i in range(len(wrong_letters)):
                    write(wrong_letters[i], (i+4.2) * 100, 500, 24)
            # for i in range(len(wrong_letters)):
            #     print("inside the loop, Woohoo!!!!!")
            #     if letter == wrong_letters[i]:
            #         print(letter, " is in wrong letters")
            #         break
            #         print(letter, " is not in wrong letters")
            #         write(letter, (wrongLetterCount+4.2) * 100, 581, 24)
            #         wrongLetterCount = wrongLetterCount + 1
            #         wrong_letters.append(letter)

list1 = []
list2 = []
list3 = list1

list1 == list2  # false
list1 == list1 # true
list1 == list3 # true

list3.append("hello")

print(list3) # ["hello"]
print(list1) # ["hello"]

def winCheck():
    print(lettersOnScreen)
    print(correct_letters)
    lettersMatch = True
    for i in range(len(correct_letters)):
        if correct_letters[i] not in lettersOnScreen:
            lettersMatch = False
    if lettersMatch == True:
        write("You Win", 640, 150, 50)


def lossCheck():
    if len(wrong_letters) >= 6:
        write("You Lose", 640, 150, 50)


def guy():
    headArea = pygame.Rect(70, 70, 50, 50)
    
    pygame.draw.ellipse(screen, (0, 0, 0), headArea, 1)

setWord(words)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     #print("keys = ", keys)
    guy()

    # TODO can we call keys.getPressed only once in the main loop??
    y = 0
    for keycode in allTheLetters():
        letter = chr(keycode)
        letterCheck(keycode, letter)
        y = y + 1
    #writeUserKey(pygame.K_s, "S", (1200, 60))

    # Show the letter on the screen:
    showSpaceForLetters(len(correct_letters), 720/2, 60)
    write("Wrong Letters:", 620, 425, 36)
    
    lossCheck()
    winCheck()
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()