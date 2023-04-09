# Fionn Ganzenboard
# pygame inistialstion
import pygame
import random
from ganzenbordSquares import squaresBoard1, squaresBoard2, squaresBoard3


def ganzenbord(player0Name, player1Name, player2Name, player3Name, player4Name, player5Name, resolution, maxPlayerAmmount):
    # Global variables

    screenSizeInteger = [1, (2200/2800), (2000/2800), (1800/2800),
                         (1600/2800), (1400/2800), (1200/2800), (1000/2800)]
    screenSize_x = int(2800 * screenSizeInteger[resolution])
    screenSize_y = int(screenSize_x) / 2

    windowSize = (screenSize_x, screenSize_y)
    screen = pygame.display.set_mode(windowSize)

    pygame.init()

    # let us run a infinite loop for the game
    done = False

    # needed for framerate of the game
    clock = pygame.time.Clock()

    # title
    pygame.display.set_caption("Ganzenboard around the world")

    # Player posistion
    position = [0, 0, 0, 0, 0, 0]
    skipped = [False, False, False, False, False, False]
    

    # who's turn is it?
    turn = 0

    # dice throw
    throw = 1
    diceMax = 6

    # wheel option
    wheelOption = 0

    # show text on screen
    myfont = pygame.font.SysFont(None, 30)
    nameFont = pygame.font.SysFont(None, 15)

    # coordinates

    # images
    board = pygame.image.load("photosOne/Ganzenbord1.png")
    board = pygame.transform.scale(board, (screenSize_x, screenSize_y))

    # Player images while ganzenboard is active
    players = [pygame.image.load("photosOne/Goose0.png"), pygame.image.load("photosOne/Goose1.png"), pygame.image.load("photosOne/Goose2.png"),
               pygame.image.load("photosOne/Goose3.png"), pygame.image.load("photosOne/Goose4.png"), pygame.image.load("photosOne/Goose5.png")]

    playerNames = [player0Name, player1Name, player2Name,
                   player3Name, player4Name, player5Name]

    # dice images

    diceNumbers = [pygame.image.load("photosOne/diceNumber1.png"), pygame.image.load("photosOne/diceNumber2.png"), pygame.image.load("photosOne/diceNumber3.png"),
                   pygame.image.load("photosOne/diceNumber4.png"), pygame.image.load("photosOne/diceNumber5.png"), pygame.image.load("photosOne/diceNumber6.png")]
    
    wheelOptions = [pygame.image.load("wheelAnimations/Wheeloption0.png"), pygame.image.load("wheelAnimations/Wheeloption1.png"), pygame.image.load("wheelAnimations/Wheeloption2.png"), pygame.image.load("wheelAnimations/Wheeloption3.png")]
    
    wheelAnimations = [pygame.image.load("wheelAnimations/Wheelanimation0.png"), pygame.image.load("wheelAnimations/Wheelanimation1.png"),pygame.image.load("wheelAnimations/Wheelanimation2.png"),pygame.image.load("wheelAnimations/Wheelanimation3.png")]
    
    confetti = [pygame.image.load("wheelAnimations/Confetti0.png"), pygame.image.load("wheelAnimations/Confetti1.png"), pygame.image.load("wheelAnimations/Confetti2.png"), pygame.image.load("wheelAnimations/Confetti3.png"),
                pygame.image.load("wheelAnimations/Confetti4.png"), pygame.image.load("wheelAnimations/Confetti5.png"),pygame.image.load("wheelAnimations/Confetti6.png"), pygame.image.load("wheelAnimations/Confetti7.png")]
    # Global functions
    def skipPlayer(turn, skipped):
        if skipped[turn]:
            skipped[turn] = False
            turn = nextPlayer(turn)
        return skipped and turn

    # Player names:

    def playerNamesFunction():
        player_names = [player0Name, player1Name, player2Name,
                        player3Name, player4Name, player5Name]
        player = str(player_names[turn])
        return player

    # the highest position of a player
    def highestPlayerPosition(position):
        highestPosition = None

        for num in position:
            if (highestPosition is None or num > highestPosition):
                highestPosition = num

        return highestPosition

    def lowestPlayerPosition(position):
        maxPlayers = maxPlayerAmmount + 1
        lst = position[0:maxPlayers]
        lowestPosition = min(lst)

        return lowestPosition
    
    def lowestPlayerTurn(position):
        lowest = position[0]
        lowest_pos = 0
        maxPlayers = maxPlayerAmmount + 1
        lst = position[0:maxPlayers]
        
        for i in range(1, len(lst)):
            if position[i] < lowest:
                lowest = position[i]
                lowest_pos = i

        return lowest_pos


    # lowest position of a player
    def nextPlayer(turn):
        if turn < maxPlayerAmmount:
            turn += 1
        elif turn == maxPlayerAmmount:
            turn = 0

        return turn

    # rendering functions:

    def updateScreen(board, players, playerNames, position, squares, throw):
        screen.fill((0,0,0))
        boardStraight = board.get_rect()
        screen.blit(board, boardStraight)
        renderDice(throw)
        renderPlayers(players, playerNames, position, squares)
        pygame.display.flip()

    #wheel rendering
    def wheelRender(wheelOption):
        wheelChoice = pygame.transform.scale(wheelOptions[wheelOption], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
        board.blit(
                wheelChoice, (2400 * screenSizeInteger[resolution], 800 * screenSizeInteger[resolution]))
        
        
    def wheelAnimation():
        i = 0
        j = 0
        f = 0
        background_colour = pygame.Color(255, 255, 255, 0) 
        wheelPosition = (2400 * screenSizeInteger[resolution], 800 * screenSizeInteger[resolution])
        wheelRect = pygame.Rect(wheelPosition, (200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
        
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

        while f < 7:
            screen.fill(background_colour, wheelRect)
            confettiAnimation = pygame.transform.scale(confetti[f], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
            screen.blit(confettiAnimation, wheelPosition)
            pygame.display.update(wheelRect)
            pygame.time.delay(100)
            f += 1
    
    def debufWheelRandomizer(turn, position, lowDice):
        debuf = random.randint(1,8)

        if debuf == 1 or 3 or 5:
            position[turn] -= 3
            print("change -3")
        elif debuf == 2 or 4:
            skipPlayer(turn, skipped)
            print("skip player")
        elif debuf == 6:
            position[turn] -= 9
            print("change -9")
        elif debuf == 7:
            lowDice[turn] = True
        elif debuf == 8:
            lowestPlayerCache = lowestPlayerTurn(position)
            swappedPosition = position[turn] 
            position[turn] = lowestPlayerPosition(position)
            position[lowestPlayerCache] = swappedPosition

        return position
    
    def debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice):
        renderPlayers(players, playerNames, position, squares)
        wheelOption = random.randint(0,3)
        wheelAnimation()
        wheelRender(wheelOption)
        debufWheelRandomizer(turn, position, lowDice)
        return position

        
        
    def renderSquare(squares):
        if squares == squaresBoard2:
            backgroundSquare = pygame.image.load(
                "photosTwo/BackgroundColour.png")

            squareScaled = pygame.transform.scale(backgroundSquare, (int(
                500 * screenSizeInteger[resolution]), int(500 * screenSizeInteger[resolution])))

            screen.blit(
                squareScaled, (int(2400 * screenSizeInteger[resolution]), 0))


    # Render Dice
    def renderDice(throw):
        diceNumber = pygame.transform.scale(diceNumbers[throw - 1], (
            200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
        screen.blit(diceNumber, (int(
            2400 * screenSizeInteger[resolution]), int(1000 * screenSizeInteger[resolution])))


    def diceRollAnimation(throw):
        i = 0
        while i < 9:
            pygame.display.flip()
            diceRandomizer = random.randint(0, 5)
            diceRandom = pygame.transform.scale(diceNumbers[diceRandomizer], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
            screen.blit(
                diceRandom, (2400 * screenSizeInteger[resolution], 1000 * screenSizeInteger[resolution]))
            pygame.time.delay(100)
            i += 1
        

    #player rendering
    def renderPlayers(players, playerNames, position, squares):
        sublist = []
        squaresMultiplied = [[i * screenSizeInteger[resolution]
                              for i in sublist] for sublist in squares]
        squaresMultiplied = [[round(x) for x in sublist]
                             for sublist in squaresMultiplied]

        for i in range(maxPlayerAmmount + 1):
            player_x = squaresMultiplied[position[i]][0]
            player_y = squaresMultiplied[position[i]][1]

            # fix at later date
            # playerNameRenderer = nameFont.render(playerNames[i], 1, (0, 0, 0))
            # screen.blit(playerNameRenderer, (player_x + (30 * screenSizeInteger[resolution]), player_y + (30 * screenSizeInteger[resolution])))

            playersScaled = pygame.transform.scale(
                players[i], (120 * screenSizeInteger[resolution], 120 * screenSizeInteger[resolution]))
            if i % 2 == 0:
                screen.blit(
                    playersScaled, (int(player_x - 40 * screenSizeInteger[resolution]), int(player_y - 40 * screenSizeInteger[resolution])))
            else:
                screen.blit(
                    playersScaled, (int(player_x - 80 * screenSizeInteger[resolution]), int(player_y - 80 * screenSizeInteger[resolution])))

    # Game Part 2

    def ganzenbordPart2(done, clock, turn, throw, diceMax):

        # images
        board = pygame.image.load("photosTwo/TransitionBoard.png")
        board = pygame.transform.scale(board, (screenSize_x, screenSize_y))

        playerNamesFunction()

        # title
        pygame.display.set_caption("Where am I?")
        # Player posistion
        position = [0, 0, 0, 0, 0, 0]
        wheelOption = 0
        lowDice = [False, False, False, False, False, False]
        squares = squaresBoard2
        while not done:

            # Check for inputs

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quits the game
                    done = True
                elif event.type == pygame.KEYDOWN:  # checks if a key has been pressed

                    if event.key == pygame.K_SPACE:  # spacebar
                        skipPlayer(turn, skipped)

                        if position[turn] >= 10 and squares == squaresBoard2:
                            turn = nextPlayer(turn)

                        if lowDice[turn]:
                            diceMax = 3 
                            throw = random.randint(1, diceMax)
                            lowDice = False
                        else:
                            throw = random.randint(1, diceMax)

                        if throw == 6:
                            turn - 1

                        diceRollAnimation(throw)
                        position[turn] += throw

                        print(position)  # For bug fixing

                        # positioning rules (actual board positions + 10)
                        if squares == squaresBoard3:
                            if position[turn] == 1:
                                position[turn] = 10
                            elif position[turn] == 2:
                                debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice)
                            elif position[turn] == 12:
                                skipped[turn] = True
                            elif position[turn] == 14:
                                debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice)
                            elif position[turn] == 17:
                                position[turn] = 23
                            elif position[turn] == 22:
                                skipped[turn] = True
                            elif position[turn] == 24:
                                debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice)
                            elif position[turn] == 41:
                                position[turn] = 50
                            elif position[turn] == 52:
                                debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice)
                            elif position[turn] == 62:
                                debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice)
                            elif position[turn] == 68:
                                debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice)
                            elif position[turn] == 73:
                                skipped[turn] = True
                            elif position[turn] == 74:
                                debufWheel(players, playerNames, position, squares, wheelOption, turn, lowDice)
                            elif position[turn] == 81:
                                skipped[turn] = True
                            elif position[turn] == 82:
                                position[turn] = 72

                        # Checks while on intermediate board
                        if position[turn] >= 5 and squares == squaresBoard2:
                            players[turn] = pygame.image.load(
                                f"photosTwo/CyberpunkGoose{turn}.png")

                        if lowestPlayerPosition(position) >= 9 and squares == squaresBoard2:
                            board = pygame.image.load(
                                "photosTwo/PunkPunkBoard.png")
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

            # show text on screen
            nameFont = pygame.font.SysFont(None, 15)

            # Render
            updateScreen(board, players, playerNames, position, squares, throw)
            renderSquare(squares)

            # Update game with new graphics
            clock.tick(60)
            pygame.display.flip()
    # ----------------------------------------- Main game -----------------------------------------#

    while not done:

        # Check for inputs

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quits the game
                done = True
            elif event.type == pygame.KEYDOWN:  # checks if a key has been pressed

                if event.key == pygame.K_SPACE:  # spacebar
                    if skipped[turn]:
                        skipped[turn] = False
                        turn = nextPlayer(turn)

                    throw = random.randint(5, diceMax)     
                    diceRollAnimation(throw)
                    

                    position[turn] += throw  # Adds throw to position
                    # print(position)  # For bug fixing
                    print(f"Lowest player position is {lowestPlayerPosition(position)}")
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

                    # Changes board depending on position
                    if highestPlayerPosition(position) >= 11 and highestPlayerPosition(position) < 20:
                        board = pygame.image.load("photosOne/Ganzenbord2.png")
                        board = pygame.transform.scale(
                            board, (screenSize_x, screenSize_y))
                        pygame.display.set_caption("What's going on?")

                    elif highestPlayerPosition(position) >= 20 and highestPlayerPosition(position) < 28:
                        board = pygame.image.load("photosOne/Ganzenbord3.png")
                        board = pygame.transform.scale(
                            board, (screenSize_x, screenSize_y))
                        pygame.display.set_caption("This is not good...")

                    elif highestPlayerPosition(position) >= 28 and highestPlayerPosition(position) < 35:
                        board = pygame.image.load("photosOne/Ganzenbord4.png")
                        board = pygame.transform.scale(
                            board, (screenSize_x, screenSize_y))
                        pygame.display.set_caption("OH GOD HELP")

                    elif highestPlayerPosition(position) > 35:
                        skipped = [False, False, False, False, False, False]
                        ganzenbordPart2(done, clock, turn, throw, diceMax)

                elif event.key == pygame.K_BACKSPACE:
                    position = [0, 0, 0, 0, 0, 0]
                    turn = 0
        updateScreen(board, players, playerNames, position, squaresBoard1, throw)
        
        # Update game with new graphics
        clock.tick(60)

    # end game
    pygame.quit()


ganzenbord("Fionn1", "Fionn2", "Fionn3", "Fionn4", "Fionn5", "Fionn6", 3, 5)
