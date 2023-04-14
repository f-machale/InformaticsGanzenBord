# Fionn Ganzenboard
# pygame inistialstion
import pygame
import easygui
import random
from ganzenbordSquares import squaresBoard1, squaresBoard2, squaresBoard3

#making the game in a function so that it can be loaded from the game
def ganzenbord(player0Name, player1Name, player2Name, player3Name, player4Name, player5Name, resolution, maxPlayerAmmount):
    #calculate the screen size and create numbers for scaling the other images
    screenSizeInteger = [1, (2200/2800), (2000/2800), (1800/2800),
                         (1600/2800), (1400/2800), (1200/2800), (1000/2800)]
    screenSize_x = int(2800 * screenSizeInteger[resolution])
    screenSize_y = int(screenSize_x) / 2

    #set the screen size
    windowSize = (screenSize_x, screenSize_y)
    screen = pygame.display.set_mode(windowSize)

    #initialise the game and the music player
    pygame.init()
    pygame.mixer.init()

    # needed for framerate of the game
    clock = pygame.time.Clock()

    # show text on screen
    infoFont = pygame.font.SysFont(None, int(40 * screenSizeInteger[resolution]))

    # images
    board = pygame.image.load("photosOne/Ganzenbord0.png")
    board = pygame.transform.scale(board, (screenSize_x, screenSize_y))

    players = [pygame.image.load("photosOne/Goose0.png"), pygame.image.load("photosOne/Goose1.png"), pygame.image.load("photosOne/Goose2.png"),
               pygame.image.load("photosOne/Goose3.png"), pygame.image.load("photosOne/Goose4.png"), pygame.image.load("photosOne/Goose5.png")]
    
    diceNumbers = [pygame.image.load("photosOne/diceNumber1.png"), pygame.image.load("photosOne/diceNumber2.png"), pygame.image.load("photosOne/diceNumber3.png"),
                   pygame.image.load("photosOne/diceNumber4.png"), pygame.image.load("photosOne/diceNumber5.png"), pygame.image.load("photosOne/diceNumber6.png")]
    
    wheelOptions = [pygame.image.load("wheelAnimations/Wheeloption0.png"), pygame.image.load("wheelAnimations/Wheeloption1.png"), pygame.image.load("wheelAnimations/Wheeloption2.png"), pygame.image.load("wheelAnimations/Wheeloption3.png")]
    
    wheelAnimations = [pygame.image.load("wheelAnimations/Wheelanimation0.png"), pygame.image.load("wheelAnimations/Wheelanimation1.png"),pygame.image.load("wheelAnimations/Wheelanimation2.png"),pygame.image.load("wheelAnimations/Wheelanimation3.png")]
    
    confetti = [pygame.image.load("wheelAnimations/Confetti0.png"), pygame.image.load("wheelAnimations/Confetti1.png"), pygame.image.load("wheelAnimations/Confetti2.png"), pygame.image.load("wheelAnimations/Confetti3.png"),
                pygame.image.load("wheelAnimations/Confetti4.png"), pygame.image.load("wheelAnimations/Confetti5.png"),pygame.image.load("wheelAnimations/Confetti6.png"), pygame.image.load("wheelAnimations/Confetti7.png")]
    
    cardArt = [pygame.image.load("cardAnimation/cardAnimation0.png"),pygame.image.load("cardAnimation/cardAnimation1.png"),pygame.image.load("cardAnimation/cardAnimation2.png")]

    # Music
    backgroundMusic1 = ["backgroundMusic/Blackout_BGM.mp3", "backgroundMusic/Calm 1 (Minecraft).mp3", "backgroundMusic/Living Mice.mp3", "backgroundMusic/Subwoofer Lullaby.mp3","backgroundMusic/Triangular_BGM.mp3"]
    backgroundMusic2 = ["backgroundMusic/cinematic-documentary-115669.mp3", "backgroundMusic/aesthetics-138637.mp3", "backgroundMusic/lofi-study-112191.mp3"]
    
    #A list for indexing all the playernames
    playerNames = [player0Name, player1Name, player2Name,
                   player3Name, player4Name, player5Name]
    
    #---------------------------------------------------------------------------- Global functions ----------------------------------------------------------------------------

    #-------------------------------------- Player functions: --------------------------------------
    def skipPlayer(turn, skipped):
        # function to indicate if a player has been skipped, does not work as function for some reason
        if skipped[turn]:
            skipped[turn] = False
            turn = nextPlayer(turn)
        return skipped and turn

    def highestPlayerPosition(position):
        #returns the highest position of any player
        highestPosition = None

        for num in position:
            if (highestPosition is None or num > highestPosition):
                highestPosition = num

        return highestPosition

    def lowestPlayerPosition(position):
        #returns the lowest position of any player
        maxPlayers = maxPlayerAmmount + 1
        lst = position[0:maxPlayers]
        lowestPosition = min(lst)

        return lowestPosition
    
    def lowestPlayerTurn(position):
        #returns the which player is on the lowest position
        lowest = position[0]
        lowest_pos = 0
        maxPlayers = maxPlayerAmmount + 1
        lst = position[0:maxPlayers]
        
        for i in range(1, len(lst)):
            if position[i] < lowest:
                lowest = position[i]
                lowest_pos = i

        return lowest_pos

    def nextPlayer(turn):
        #A function to swap turn to the next player
        if turn < maxPlayerAmmount:
            turn += 1
        elif turn == maxPlayerAmmount:
            turn = 0

        return turn
    #-------------------------------------- Music: --------------------------------------
    def music(squares):
        #A function for playing the music at random and the music depending on the board
        musicChoice = random.randint(0,4)
        pygame.mixer.music.set_volume(0.5)
        if squares == squaresBoard3 or squares == squaresBoard2:
            pygame.mixer.music.load(backgroundMusic1[musicChoice]) 
            pygame.mixer.music.play()
            pygame.mixer.music.fadeout(10)
            musicChoice = random.randint(0,4)
            pygame.mixer.music.queue(backgroundMusic1[musicChoice])
        else:
            musicChoice = random.randint(0,2)
            pygame.mixer.music.load(backgroundMusic2[musicChoice])
            pygame.mixer.music.play()
            pygame.mixer.music.fadeout(10)
            musicChoice = random.randint(0,2)
            pygame.mixer.music.queue(backgroundMusic2[musicChoice])

    #-------------------------------------- challenge card functions and rendering --------------------------------------
    def rockPaperScissors(position, turn):
        #rock paper scissors for the cards
        rpsRandom = random.randint(0,2)
        rpsChoice = easygui.buttonbox("Choose one: ", "Rock, Paper, Scissors", ("Rock", "Paper", "Scissors"))

        if rpsChoice == "Rock":
            if rpsRandom == 0:
                easygui.msgbox("You tied, the AI also chose rock. You don't move")
            elif rpsRandom == 1:
                easygui.msgbox("You lost, the AI chose paper. You move back 4 spaces")
                position[turn] -= 4
            elif rpsRandom == 2:
                easygui.msgbox("You won, the AI chose scissors. You move forward 5 spaces")
                position[turn] += 5
        elif rpsChoice == "Paper":
            if rpsRandom == 0:
                easygui.msgbox("You won, the AI chose rock. You move forward 5 spaces")
                position[turn] += 5
            elif rpsRandom == 1:
                easygui.msgbox("You tied, the AI also chose paper. You don't move")
            elif rpsRandom == 2:
                easygui.msgbox("You lost, the AI chose scissors. You move back 4 spaces")
                position[turn] -= 4
        elif rpsChoice == "Scissors":
            if rpsRandom == 0:
                easygui.msgbox("You lost, the AI chose rock. You move back 4 spaces")
                position[turn] -= 4
            elif rpsRandom == 1:
                easygui.msgbox("You won, the AI chose paper. You move forward 5 spaces")
                position[turn] += 5
            elif rpsRandom == 2:
                easygui.msgbox("You tied, the AI also chose scissors. You don't move")
        
        return position
    
    def coinFlip(position, turn):
        # a simple coin flip guessing game
        coinFlip = random.randint(0,1)
        button_list = ["Heads", "Tails"]
        coinList = [True, False]
        coinFlipChoice = easygui.boolbox("Choose one: ", "Coin Flip", ("Heads", "Tails"))
        if coinFlipChoice == coinList[coinFlip]:
            easygui.msgbox(f"Congrats, you got it right! The coin landed on {button_list[coinFlip]}. You now get to move 3 places forward")
            position[turn] += 3
        elif coinFlipChoice != coinList[coinFlip] != coinFlip:
            easygui.msgbox(f"Unfortunatly, you got it wrong. The coin landed on {button_list[coinFlip]}. You now get to move 3 places backwards")
            position[turn] -= 3

    def numberGuess(position, turn):
        # A number guessing game for the cards
        number = random.randint(1,10)
        numberChoice = easygui.buttonbox("Choose a number between 1 and 10: ", "A guessing game", ("1", "2","3","4","5","6","7","8","9","10"))
        
        if numberChoice == str(number):
            easygui.msgbox(f"Congrats, you got it right! The number was {number}. You now get to move 6 places forward")
            position[turn] += 9
        else:
            easygui.msgbox(f"Unfortunatly, you got it wrong. The number was {number}. You now get to move 3 places backwards")
            position[turn] -= 3
    
    def cardAnimation():
        #animation for choosing cards
        i = 0
        j = 0

        cardPosition = (2400 * screenSizeInteger[resolution], 950 * screenSizeInteger[resolution])
        cardRect = pygame.Rect(cardPosition, (200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))

        while i < 12:
            if j == 3:
                j = 0
            cardAnimation = pygame.transform.scale(cardArt[j], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
            screen.blit(cardAnimation, cardPosition)
            pygame.display.update(cardRect)
            pygame.time.delay(100)
            i += 1 
            j += 1
    
    def challengeCards(position, turn):
        # compiles all the card fuctions into one
        challengeChoice = random.randint(0,2)
        cardAnimation()
        if challengeChoice == 0:
            rockPaperScissors(position, turn)
        elif challengeChoice == 2:
            coinFlip(position, turn)
        else:
            numberGuess(position, turn)
        return position


    #-------------------------------------- debufWheel functions and rendering: --------------------------------------
    def wheelRender(wheelOption):
        #renders the wheel somewhere, this function used to work
        wheelChoice = pygame.transform.scale(wheelOptions[wheelOption], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
        screen.blit(
                wheelChoice, (2400 * screenSizeInteger[resolution], 950 * screenSizeInteger[resolution]))
        
        
    def wheelAnimation():
        #wheel animation
        i = 0
        j = 0
        f = 0
        background_colour = pygame.Color(255, 255, 255, 0) 
        wheelPosition = (2400 * screenSizeInteger[resolution], 950 * screenSizeInteger[resolution])
        wheelRect = pygame.Rect(wheelPosition, (200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
        
        #wheel rolling animation
        while i < 15:
            if j == 3:
                j = 0
            screen.fill(background_colour, wheelRect)
            wheelAnimation = pygame.transform.scale(wheelAnimations[j], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
            screen.blit(wheelAnimation, wheelPosition)
            pygame.display.update(wheelRect)
            pygame.time.delay(100)
            i += 1
            j += 1
        
        #confetti
        while f < 7:
            screen.fill(background_colour, wheelRect)
            confettiAnimation = pygame.transform.scale(confetti[f], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
            screen.blit(confettiAnimation, wheelPosition)
            pygame.display.update(wheelRect)
            pygame.time.delay(100)
            f += 1

    def wheelPopUp(text):
        #text for outcome of debuf wheel
        easygui.msgbox(text, "Debuf Wheel")
    
    def debufWheelRandomizer(turn, position, lowDice, debuf, skipped):
        #what happens to the player after the wheel was spun
        if debuf == 1 or debuf == 3:
            text = "Unlucky, move back 3 places"
            position[turn] -= 3
            wheelPopUp(text)
        elif debuf == 2 or debuf == 4: 
            text = "Unlucky, you skip your next turn"
            skipPlayer(turn, skipped)
            wheelPopUp(text)
        elif debuf == 5:
            text = "Lucky, move forward 5 places"
            position[turn] +=5
            wheelPopUp(text)
        elif debuf == 6:
            text = "Unlucky, move back 9 places"
            position[turn] -= 9
            wheelPopUp(text)
        elif debuf == 7:
            text = "Unlucky, use a 3 sided dice for your next turn"
            wheelPopUp(text)
            lowDice[turn] = True
        elif debuf == 8:
            text = "Unlucky, swap positions with the lowest player" 
            wheelPopUp(text)
            lowestPlayerCache = lowestPlayerTurn(position)
            swappedPosition = position[turn] 
            position[turn] = lowestPlayerPosition(position)
            position[lowestPlayerCache] = swappedPosition

        return position and lowDice and skipped
    
    def debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped):
        #Function that compiles every debuf wheel function into one
        debuf = random.randint(1,8)
        renderPlayers(players, position, squares)
        wheelOption = random.randint(0,3)
        wheelAnimation()
        wheelRender(wheelOption)
        debufWheelRandomizer(turn, position, lowDice, debuf, skipped)
        return position and lowDice and skipped
    
    #-------------------------------------- winner functions: --------------------------------------
    def winner(turn):
        #displays text for when someone wins
        text =  f"{playerNames[turn]} is the winner!!!!"
        easygui.msgbox(text, "We have a winnner!")
        
    
    #-------------------------------------- rendering functions: --------------------------------------
    def renderSquare(squares):
        #renders square to hide players on board 2
        if squares == squaresBoard2:
            backgroundSquare = pygame.image.load(
                "photosTwo/BackgroundColour.png")

            squareScaled = pygame.transform.scale(backgroundSquare, (int(
                500 * screenSizeInteger[resolution]), int(450 * screenSizeInteger[resolution])))

            screen.blit(
                squareScaled, (int(2400 * screenSizeInteger[resolution]), 0))


    # Render Dice
    def renderDice(throw):
        #rendering the throw and final dice
        diceNumber = pygame.transform.scale(diceNumbers[throw - 1], (
            200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
        screen.blit(diceNumber, (int(
            2400 * screenSizeInteger[resolution]), int(1150 * screenSizeInteger[resolution])))


    def diceRollAnimation(throw):
        #the animation that plays when you roll the dice
        i = 0
        while i < 9:
            pygame.display.flip()
            diceRandomizer = random.randint(0, 5)
            diceRandom = pygame.transform.scale(diceNumbers[diceRandomizer], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
            screen.blit(
                diceRandom, (2400 * screenSizeInteger[resolution], 1150 * screenSizeInteger[resolution]))
            pygame.time.delay(100)
            i += 1
        
    def renderPlayers(players, position, squares):
        sublist = []
        squaresMultiplied = [[i * screenSizeInteger[resolution]
                              for i in sublist] for sublist in squares]
        squaresMultiplied = [[round(x) for x in sublist]
                             for sublist in squaresMultiplied]
        
        for i in range(maxPlayerAmmount + 1):
            
            player_x = squaresMultiplied[position[i]][0]
            player_y = squaresMultiplied[position[i]][1]

            #scales each player based on the resolution that was chosen
            playersScaled = pygame.transform.scale(
                players[i], (120 * screenSizeInteger[resolution], 120 * screenSizeInteger[resolution]))
            if i % 2 == 0:
                screen.blit(
                    playersScaled, (int(player_x - 40 * screenSizeInteger[resolution]), int(player_y - 40 * screenSizeInteger[resolution])))
            else:
                screen.blit(
                    playersScaled, (int(player_x - 80 * screenSizeInteger[resolution]), int(player_y - 80 * screenSizeInteger[resolution])))
                
    def renderInfoBackground(squares):
        # renders background for each row of information in renderGameInfo
        if squares == squaresBoard2:
            text_X = 1490 * screenSizeInteger[resolution]
            text_Y = 170 * screenSizeInteger[resolution]
        else:
            text_X = 2290 * screenSizeInteger[resolution]
            text_Y = 540 * screenSizeInteger[resolution]
            
        textDown = [-50, 0, 50, 100, 150, 200, 250]
        for i in range(maxPlayerAmmount + 2):
            backgroundList = [
                          pygame.Rect(int(text_X), int(text_Y + textDown[i] * screenSizeInteger[resolution]), int(490 * screenSizeInteger[resolution]), int(60 * screenSizeInteger[resolution])),
                          pygame.Rect(int(text_X), int(text_Y + textDown[i] * screenSizeInteger[resolution]), int(490 * screenSizeInteger[resolution]), int(60 * screenSizeInteger[resolution])),
                          pygame.Rect(int(text_X), int(text_Y + textDown[i] * screenSizeInteger[resolution]), int(490 * screenSizeInteger[resolution]), int(60 * screenSizeInteger[resolution])),
                          pygame.Rect(int(text_X), int(text_Y + textDown[i] * screenSizeInteger[resolution]), int(490 * screenSizeInteger[resolution]), int(60 * screenSizeInteger[resolution])),
                          pygame.Rect(int(text_X), int(text_Y + textDown[i] * screenSizeInteger[resolution]), int(490 * screenSizeInteger[resolution]), int(60 * screenSizeInteger[resolution])),
                          pygame.Rect(int(text_X), int(text_Y + textDown[i] * screenSizeInteger[resolution]), int(490 * screenSizeInteger[resolution]), int(60 * screenSizeInteger[resolution])),
                          pygame.Rect(int(text_X), int(text_Y + textDown[i] * screenSizeInteger[resolution]), int(490 * screenSizeInteger[resolution]), int(60 * screenSizeInteger[resolution]))]
            pygame.draw.rect(screen, (242, 247, 253), backgroundList[i], 0, 4, 4, 4, 4)
    
    def renderGameInfo(playerNames, position, skipped, lowDice, squares):
        #renders all information about the game on the a scoreboard
        textDown = [0, 50, 100, 150, 200, 250] 
        if squares == squaresBoard2:
            text_X = 1500 * screenSizeInteger[resolution]
            text_Y = 180 * screenSizeInteger[resolution] 
        else:
            text_X = 2300 * screenSizeInteger[resolution]
            text_Y = 550 * screenSizeInteger[resolution]
            
        for i in range(maxPlayerAmmount + 1):
            #checks if player is on board three, if they are add 10 to the position being displayed
            if squares == squaresBoard3:
                stringPosition = str(position[i] + 10)
            else:
                stringPosition = str(position[i])

            #renders names and positions of each player
            nameInfoRender = infoFont.render(playerNames[i], 1, (0, 0, 0))
            screen.blit(nameInfoRender, ((int(text_X)), (int(text_Y + textDown[i] * screenSizeInteger[resolution]))))

            positionInfoRender = infoFont.render(stringPosition, 1, (0, 0, 0))
            screen.blit(positionInfoRender, ((int(text_X + 130 * screenSizeInteger[resolution])), (int(text_Y + textDown[i] * screenSizeInteger[resolution]))))

            #checks if a player has been skipped and displays yes or no
            skippedText = "No"
            if skipped[i]:
                skippedText = "Yes"
            skippedInfoRender = infoFont.render(skippedText, 1, (0, 0, 0))
            screen.blit(skippedInfoRender, ((int(text_X + 210 * screenSizeInteger[resolution])), (int(text_Y + textDown[i] * screenSizeInteger[resolution]))))
            
            #checks if a player has a low dice and displays yes or no
            lowDiceText = "No"
            if lowDice[i]:
                lowDiceText = "Yes"
            lowDiceInfoRender = infoFont.render(lowDiceText, 1, (0, 0, 0))
            screen.blit(lowDiceInfoRender, ((int(text_X + 300 * screenSizeInteger[resolution])), (int(text_Y + textDown[i] * screenSizeInteger[resolution]))))

        #render the titles for each row of information    
        namesTextRender = infoFont.render("Names:", 1, (0, 0, 0))
        screen.blit(namesTextRender, ((int(text_X)), (int(text_Y - 50 * screenSizeInteger[resolution]))))

        positionTextRender = infoFont.render("Pos:", 1, (0, 0, 0))
        screen.blit(positionTextRender, ((int(text_X + 130 * screenSizeInteger[resolution])), (int(text_Y - 50 * screenSizeInteger[resolution]))))

        skippedTextRender = infoFont.render("Skip:", 1, (0, 0, 0))
        screen.blit(skippedTextRender, ((int(text_X + 210 * screenSizeInteger[resolution])), (int(text_Y - 50 * screenSizeInteger[resolution]))))

        lowDiceTextRender = infoFont.render("3 sided dice:", 1, (0, 0, 0))
        screen.blit(lowDiceTextRender, ((int(text_X + 300 * screenSizeInteger[resolution])), (int(text_Y - 50 * screenSizeInteger[resolution]))))

    def updateScreen(board, players, playerNames, position, squares, throw, skipped, lowDice):
        # compilation of all the functions needed for rendering
        screen.fill((0,0,0))
        boardStraight = board.get_rect()
        screen.blit(board, boardStraight)
        renderDice(throw)
        renderPlayers(players, position, squares)
        renderInfoBackground(squares)
        renderGameInfo(playerNames, position, skipped, lowDice, squares)
        renderSquare(squares)
        pygame.display.flip()

    
    # Game Part 2

    def ganzenbordPart2(done, clock, turn, throw):

        # images
        board = pygame.image.load("photosTwo/TransitionBoard.png")
        board = pygame.transform.scale(board, (screenSize_x, screenSize_y))

        # title
        pygame.display.set_caption("Where are we going?")

        # local variables for this part of the game
        position = [0, 0, 0, 0, 0, 0]
        wheelOption = 0
        diceMax = 6
        skipped = [False, False, False, False, False, False]
        lowDice = [False, False, False, False, False, False]
        squares = squaresBoard2

        music(squares) #plays music

        while not done:

            # Check for inputs

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quits the game
                    done = True
                elif event.type == pygame.KEYDOWN:  # checks if a key has been pressed

                    if event.key == pygame.K_SPACE:  # spacebar
                        #check if a player was skipped                        
                        if skipped[turn]:
                            skipped[turn] = False
                            turn = nextPlayer(turn)

                        #check if a player needs to be skipped on the second board
                        if position[turn] >= 10 and squares == squaresBoard2:
                            turn = nextPlayer(turn)

                        #Checks if a player has a low dice
                        if lowDice[turn]:
                            diceMax = 3 
                            lowDice[turn] = False
                            throw = random.randint(1, diceMax)

                        #roll the dice
                        throw = random.randint(1, diceMax)

                        #animate the dice and update position
                        diceRollAnimation(throw)
                        position[turn] += throw

                        # positioning rules (actual board positions + 10)

                        if squares == squaresBoard3:
                            if position[turn] == 1:
                                position[turn] = 10
                            elif position[turn] == 2:
                                debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped)
                            elif position[turn] == 4:
                                challengeCards(position, turn)
                            elif position[turn] == 7:
                                challengeCards(position, turn)
                            elif position[turn] == 12:
                                skipped[turn] = True
                            elif position[turn] == 14:
                                debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped)
                            elif position[turn] == 17:
                                position[turn] = 23
                            elif position[turn] == 20:
                                challengeCards(position, turn)
                            elif position[turn] == 22:
                                skipped[turn] = True
                            elif position[turn] == 24:
                                debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped)
                            elif position[turn] == 29:
                                challengeCards(position, turn)
                            elif position[turn] == 37:
                                challengeCards(position, turn)
                            elif position[turn] == 41:
                                position[turn] = 50
                            elif position[turn] == 47:
                                challengeCards(position, turn)
                            elif position[turn] == 52:
                                debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped)
                            elif position[turn] == 59:
                                challengeCards(position, turn)
                            elif position[turn] == 62:
                                debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped)
                            elif position[turn] == 68:
                                debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped)
                            elif position[turn] == 73:
                                skipped[turn] = True
                            elif position[turn] == 74:
                                debufWheel(players, position, squares, wheelOption, turn, lowDice, skipped)
                            elif position[turn] == 76:
                                challengeCards(position, turn)
                            elif position[turn] == 81:
                                skipped[turn] = True
                            elif position[turn] == 82:
                                position[turn] = 72
                            elif position[turn] >= 83:
                                winner(turn) 

                        # Checks while on intermediate board
                        if position[turn] >= 5 and squares == squaresBoard2:
                            players[turn] = pygame.image.load(
                                f"photosTwo/CyberpunkGoose{turn}.png")
                        
                        # changes background to the third board
                        if lowestPlayerPosition(position) >= 9 and squares == squaresBoard2:
                            board = pygame.image.load(
                                "photosTwo/PunkPunkBoard.png")
                            pygame.display.set_caption("Where are we?")
                            position = [0, 0, 0, 0, 0, 0]
                            squares = squaresBoard3
                            board = pygame.transform.scale(
                                board, (screenSize_x, screenSize_y))

                        # makes player go to next turn
                        turn = nextPlayer(turn)

                    elif event.key == pygame.K_BACKSPACE:
                        position = [0, 0, 0, 0, 0, 0]
                        turn = 0

            boardStraight = board.get_rect()
            screen.blit(board, boardStraight)

            # Render
            updateScreen(board, players, playerNames, position, squares, throw, skipped, lowDice)
            

            # Update game with new graphics
            clock.tick(60)
            pygame.display.flip()
    # ----------------------------------------- Main game -----------------------------------------#
    music(squaresBoard1) #playes music

    # title
    pygame.display.set_caption("Ganzenboard around the world")

    # let us run a infinite loop for the game
    done = False

    # Local variables for the main game
    position = [0, 0, 0, 0, 0, 0]
    skipped = [False, False, False, False, False, False]
    lowDice = [False, False, False, False, False, False]
    turn = 0
    throw = 1

    while not done:
        
        # Check for inputs

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quits the game
                done = True
            elif event.type == pygame.KEYDOWN:  # checks if a key has been pressed
                
                if event.key == pygame.K_SPACE:  # spacebar
                    #check if a player was skipped 
                    if skipped[turn]:
                        skipped[turn] = False
                        turn = nextPlayer(turn)
                    
                    #roll the dice
                    throw = random.randint(1, 6)

                    #animate the dice and update position
                    diceRollAnimation(throw)
                    position[turn] += throw

                    # dice rules
                    if throw == 6:
                        turn - 1

                    # position rules
                    if position[turn] == 6:
                        position[turn] += 6
                    elif position[turn] == 19:
                        skipped[turn] = True
                    elif position[turn] == 24:
                        position[turn] = 18

                    # makes player go to next turn
                    turn = nextPlayer(turn)

                    # Changes board and title depending on position
                    if highestPlayerPosition(position) >= 11 and highestPlayerPosition(position) < 20:
                        board = pygame.image.load("photosOne/Ganzenbord1.png")
                        board = pygame.transform.scale(
                            board, (screenSize_x, screenSize_y))
                        pygame.display.set_caption("What's going on?")

                    elif highestPlayerPosition(position) >= 20 and highestPlayerPosition(position) < 28:
                        board = pygame.image.load("photosOne/Ganzenbord2.png")
                        board = pygame.transform.scale(
                            board, (screenSize_x, screenSize_y))
                        pygame.display.set_caption("This is not good...")

                    elif highestPlayerPosition(position) >= 28 and highestPlayerPosition(position) < 35:
                        board = pygame.image.load("photosOne/Ganzenbord3.png")
                        board = pygame.transform.scale(
                            board, (screenSize_x, screenSize_y))
                        pygame.display.set_caption("OH GOD HELP")
                        if highestPlayerPosition(position) > 33: #fades out music for next board
                            pygame.mixer.music.fadeout(300)

                    elif highestPlayerPosition(position) > 35:
                        skipped = [False, False, False, False, False, False]
                        ganzenbordPart2(done, clock, turn, throw)

                elif event.key == pygame.K_BACKSPACE:
                    position = [0, 0, 0, 0, 0, 0]
                    turn = 0
        updateScreen(board, players, playerNames, position, squaresBoard1, throw, skipped, lowDice)
        
        # Update game with new graphics
        clock.tick(60)
    
    # end game
    pygame.quit()