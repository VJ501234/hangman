#Hangman
import pygame
import random
import wordlist



# pygame setup
pygame.init()
words = wordlist.words
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

def getNineLetterWords(words):
    
    return(words)



player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

screen.fill((255, 255, 255))

#Creates space for letters
def showSpaceForLetters(numOfLetters, height, size):
    for i in range(numOfLetters):
        pygame.draw.line(screen, (255, 0, 0), ((i+4) * 100, height), ((i+4) * 100 + size, height))

#Writes words on the screen
def write(word, xPosition, yPosition, fontSize):
    font = pygame.font.SysFont("Arial", fontSize)
    textsurface = font.render(word, True, blue)
    screen.blit(textsurface,(xPosition - textsurface.get_width() // 2, yPosition - textsurface.get_height() // 2))
    

#returns the keycode of a - z
def allTheLetters():
    return range(pygame.K_a, pygame.K_z + 1)

#sets a Word
def setWord(wordList, correctLetters):
    
    correctWord = wordList[random.randint(0, len(wordList) - 1)]
    while len(correctWord) >= 10:
        correctWord = wordList[random.randint(0, len(wordList) - 1)]
    for i in range(len(correctWord)):
        correctLetters.append(correctWord[i])
    return(correctWord)

#makes a button
def makeButton(text, buttonParameters):
    (xPos, yPos, width, height) = buttonParameters
    pygame.draw.line(screen, (0, 0, 0), (xPos, yPos), (xPos + width, yPos))
    pygame.draw.line(screen, (0, 0, 0), (xPos, yPos+height), (xPos + width, yPos+height))
    pygame.draw.line(screen, (0, 0, 0), (xPos, yPos), (xPos, yPos+height))
    pygame.draw.line(screen, (0, 0, 0), (xPos+width, yPos), (xPos+width, yPos+height))
    write(text, xPos+width / 2, yPos + height / 2, height // 3)
    
#checks if the is inside the box area
def isMouseInBox(buttonParameters, mouse):
    (xPos, yPos, width, height) = buttonParameters
    # if its to the right of the left line..
    # if its to the left of the right line..
    #if its to under the top line..
    #if its over the bottom line..
    (mouseX, mouseY) = mouse
    return(mouseX >= xPos and mouseX <= xPos + width and mouseY >= yPos and mouseY <= yPos + height)

#Checks if you want or don't want to play again but doesn't do anything but print something
def playAgain():

    write("Would you like to play again?", 640, 150, 40)

    yesButtonParameters = (500, 200, 100, 70) #Rectangle!
    noButtonParameters = (700, 200, 100, 70) # aka, pygame.Rect(x,y,width, height)

    makeButton("Yes", yesButtonParameters)
    makeButton("No", noButtonParameters)

    mousePos = pygame.mouse.get_pos()
    isMouseInYesBox = isMouseInBox(yesButtonParameters, mousePos)
    isMouseInNoBox = isMouseInBox(noButtonParameters ,mousePos)
    mouseButtonsPressed = pygame.mouse.get_pressed()
    isMousePressed = mouseButtonsPressed[0]
    if isMouseInYesBox and isMousePressed:
        print("yes button pressed")
        screen.fill((255,255,255))
        return("Restart")
    if isMouseInNoBox and isMousePressed:
        print("no button pressed")
        return("Stop")
    else:
        return("Continue")

#check if key is pressed
def isKeyPressed(keycode):
    
    keys = pygame.key.get_pressed()
    return(keys[keycode])

#checks what key is pressed and 
def letterCheck(keycode, letter, correctLetters, wrongLetters, lettersOnScreen):
    isLetterCorrect = False
   
    if isKeyPressed(keycode):
        print("keycode = ", keycode)
        for i in range(len(correctLetters)):
            print("i=", i)
            #if letter is in the word, write the letters where it goes in the word based on i
            if letter == correctLetters[i]:
                write(letter, (i+4.35) * 100, 341, 36)
                isLetterCorrect = True
                
        if isLetterCorrect:
            # if the letter is not in the letters on screen variable,
            # add it so we know what letters are on the screen.
            if letter not in lettersOnScreen:
                lettersOnScreen.append(letter)
        else:
            print(letter, " isn't correct")

            # if the letter is not in wrongletters, then add it.
            if letter not in wrongLetters:
                wrongLetters.append(letter)
            # then, write out all the wrong letters.
                for i in range(len(wrongLetters)):
                    write(wrongLetters[i], (i+4.2) * 100, 500, 24)
        

def takeKeyInput(correctLetters, wrongLetters, lettersOnScreen):
    y = 0
    for keycode in allTheLetters():
        letter = chr(keycode)
        letterCheck(keycode, letter, correctLetters, wrongLetters, lettersOnScreen)
        y = y + 1

def lossCheck(numOfWrongLetters):
    return(len(numOfWrongLetters) >= 6)
        
    

def winCheck(correctLetters, lettersOnScreen):
    lettersMatch = True
    for i in range(len(correctLetters)):
        if correctLetters[i] not in lettersOnScreen:
            lettersMatch = False
            
    return(lettersMatch)

def endGameCheck(correctLetters, wrongLetters, lettersOnScreen, correctWord):
    win = winCheck(correctLetters, lettersOnScreen)
    lose = lossCheck(wrongLetters)
    
    # what should the logic for winning and losing be?
    if lose:
        write(f"You Lose, the word was {correctWord}", 640, 100, 50)
    if win:
        write("You Win", 640, 100, 50)
    if lose or win:
        return(playAgain())
    if not win and not lose:
        takeKeyInput(correctLetters, wrongLetters, lettersOnScreen)
        guy(len(wrongLetters))
    return("continue")

   



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
    

def game():
    correctLetters = []
    wrongLetters = []
    correctWord = setWord(words, correctLetters)
    lettersOnScreen = []
    running = True
    clickedNo = False
    showSpaceForLetters(len(correctLetters), 720/2, 60)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("X button clicked")
                running = False
                clickedNo = True
      
                #the user pressed the X button


        #print("keys = ", keys)
        #keys = pygame.key.get_pressed()
      

        # Show the letter on the screen:
        
        #Write wrong letters for where the wrong letters should go
        write("Wrong Letters:", 620, 425, 36)
        
        #Checks if the game has ended
        
        if running:

            if endGameCheck(correctLetters, wrongLetters, lettersOnScreen, correctWord) == "Stop":
                clickedNo = True
                running = False
            elif endGameCheck(correctLetters, wrongLetters, lettersOnScreen, correctWord) == "Restart":
                running = False
                clickedNo = False
            elif endGameCheck(correctLetters, wrongLetters, lettersOnScreen, correctWord) == "Continue":
                running = True
                
            
            

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000
            
    return(clickedNo)
    #pygame.quit()


def main():
    userClickedNo=False
    while not userClickedNo:
        userClickedNo = game()
        print("userClickedNo =", userClickedNo)
        print("Game has ended")
    pygame.quit()


main()
print("Getting to the end of the program")
pygame.quit()