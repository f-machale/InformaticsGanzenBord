# Fionn Ganzenboard
# pygame inistialstion
import pygame
import random
import time
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

    # who's turn is it?
    turn = 0

    # dice throw
    throw = 1

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

    # Global functions

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

    # lowest position of a player
    def nextPlayer(turn):
        if turn < maxPlayerAmmount:
            turn += 1
        elif turn == maxPlayerAmmount:
            turn = 0

        return turn

    # rendering functions:

    def showCorrectDie(throw):
        diceNumber = pygame.transform.scale(diceNumbers[throw - 1], (
            200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
        screen.blit(
            diceNumber, (2400 * screenSizeInteger[resolution], 1000 * screenSizeInteger[resolution]))

    def diceRollAnimation(throw):
        i = 0
        while i < 15:
            pygame.display.flip()
            diceRandomizer = random.randint(1, 6)
            diceRandom = pygame.transform.scale(diceNumbers[diceRandomizer - 1], (
                200 * screenSizeInteger[resolution], 200 * screenSizeInteger[resolution]))
            screen.blit(
                diceRandom, (2400 * screenSizeInteger[resolution], 1000 * screenSizeInteger[resolution]))
            time.sleep(0.1)
            i += 1
        showCorrectDie(throw)

    def renderPlayers(players, playerNames, position, squares):
        sublist = []
        squaresMultiplied = [[i * screenSizeInteger[resolution]
                              for i in sublist] for sublist in squares]
        squaresMultiplied = [[round(x) for x in sublist]
                             for sublist in squaresMultiplied]

        for i in range(maxPlayerAmmount + 1):
            player_x = squaresMultiplied[position[i]][0]
            player_y = squaresMultiplied[position[i]][1]
            playerNameRenderer = nameFont.render(playerNames[i], 1, (0, 0, 0))
            screen.blit(playerNameRenderer, (player_x + (30 *
                        screenSizeInteger[resolution]), player_y + (30 * screenSizeInteger[resolution])))

            playersScaled = pygame.transform.scale(
                players[i], (120 * screenSizeInteger[resolution], 120 * screenSizeInteger[resolution]))
            if i % 2 == 0:
                screen.blit(
                    playersScaled, (int(player_x - 40 * screenSizeInteger[resolution]), int(player_y - 40 * screenSizeInteger[resolution])))
            else:
                screen.blit(
                    playersScaled, (int(player_x - 80 * screenSizeInteger[resolution]), int(player_y - 80 * screenSizeInteger[resolution])))

    # Game Part 2

    def ganzenbordPart2(done, clock, turn, throw):

        # images
        board = pygame.image.load("photosTwo/TransitionBoard.png")
        board = pygame.transform.scale(board, (screenSize_x, screenSize_y))

        playerNamesFunction()

        # title
        pygame.display.set_caption("Where am I?")

        # Player posistion
        position = [0, 0, 0, 0, 0, 0]



        squares = squaresBoard1
        while not done:

            # Check for inputs

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # quits the game
                    done = True
                elif event.type == pygame.KEYDOWN:  # checks if a key has been pressed

                    if event.key == pygame.K_SPACE:  # spacebar
                        throw = random.randint(1, 6)
                        diceRollAnimation(throw)
                        position[turn] += throw

                        print(position)  # For bug fixing
                        print(lowestPlayerPosition(position))

                        if position[turn] >= 5:
                            squares = squaresBoard3
                            players[turn] = pygame.image.load(
                                f"photosTwo/CyberpunkGoose{turn}.png")

                        if lowestPlayerPosition(position) > 5:
                            board = pygame.image.load("photosTwo/PunkPunkBoard.png")
                            board = pygame.transform.scale(
                                board, (screenSize_x, screenSize_y))

                        # makes player go to next turn
                        turn = nextPlayer(turn)

                    elif event.key == pygame.K_BACKSPACE:
                        position = [0, 0, 0, 0, 0, 0]
                        turn = 0

            screen.fill((255, 255, 255))

            boardStraight = board.get_rect()
            screen.blit(board, boardStraight)

            # show text on screen
            nameFont = pygame.font.SysFont(None, 15)

            # Render players
            renderPlayers(players, playerNames, position, squares)

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
                    throw = random.randint(1, 6)
                    # diceRollAnimation()
                    position[turn] += throw  # Adds throw to position
                    print(position[turn])  # For bug fixing

                    # dice rules
                    if throw == 6:
                        turn - 1

                    # position rules
                    if position[turn] == 6:
                        position[turn] += 6
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
                        ganzenbordPart2(done, clock, turn, throw)

                elif event.key == pygame.K_BACKSPACE:
                    position = [0, 0, 0, 0, 0, 0]
                    turn = 0

        screen.fill((255, 255, 255))

        boardStraight = board.get_rect()
        screen.blit(board, boardStraight)

        renderPlayers(players, playerNames, position, squaresBoard1)

        # Update game with new graphics
        clock.tick(60)
        pygame.display.flip()
    # end game
    pygame.quit()


ganzenbord("Fionn1", "Fionn2", "Fionn3", "Fionn4", "Fionn5", "Fionn6", 5, 1)
