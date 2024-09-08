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
            #print(letter, " is correct")

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

def lossCheck():
    if len(wrong_letters) >= 6:
        write(f"You Lose, the word was {correctWord}", 640, 150, 50)

def winCheck():
    print(lettersOnScreen)
    print(correct_letters)
    lettersMatch = True
    for i in range(len(correct_letters)):
        if correct_letters[i] not in lettersOnScreen:
            lettersMatch = False
            lossCheck()
            guy(len(wrong_letters))
    if lettersMatch == True:
        write("You Win", 640, 150, 50)
    
        
   



def guy(numOfWrongLetters):
    headArea = pygame.Rect(100, 70, 160, 160)
    eye1 = pygame.Rect(130, 110, 30, 30)
    eye2 = pygame.Rect(200, 110, 30, 30)
    pygame.draw.ellipse(screen, (0, 0, 0), headArea, 1)
    pygame.draw.ellipse(screen, (0, 0, 0), eye1, 1)
    pygame.draw.ellipse(screen, (0, 0, 0), eye2, 1)
    pygame.draw.line(screen, (0, 0, 0), (150, 190), (210, 190))
    pygame.draw.line(screen, (0, 0, 0), (180, 230), (180, 500))
    pygame.draw.line(screen, (0, 0, 0), (180, 500), (260, 650))
    pygame.draw.line(screen, (0, 0, 0), (180, 500), (100, 650))
    pygame.draw.line(screen, (0, 0, 0), (180, 350), (80, 270))
    pygame.draw.line(screen, (0, 0, 0), (180, 350), (280, 270))
    if numOfWrongLetters >= 1:
        pygame.draw.line(screen, (255, 255, 255), (180, 500), (260, 650))
    if numOfWrongLetters >= 2:
        pygame.draw.line(screen, (255, 255, 255), (180, 500), (100, 650))
    if numOfWrongLetters >= 3:
        pygame.draw.line(screen, (255, 255, 255), (180, 350), (80, 270))
    if numOfWrongLetters >= 4:
        pygame.draw.line(screen, (255, 255, 255), (180, 350), (280, 270))
    if numOfWrongLetters >= 5:
        pygame.draw.line(screen, (255, 255, 255), (180, 230), (180, 500))

    if numOfWrongLetters >= 6:
        pygame.draw.line(screen, (255, 255, 255), (150, 190), (210, 190))
        pygame.draw.ellipse(screen, (255, 255, 255), eye1, 1)
        pygame.draw.ellipse(screen, (255, 255, 255), eye2, 1)
    


setWord(words)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     #print("keys = ", keys)
    

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
    

    winCheck()
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()