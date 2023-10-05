import random # For generating random numbers
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports

# Global Variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/background.png'
PIPE = 'gallery/sprites/pipe.png'

def welcomeScreen():
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()


        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            return     

        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                GAME_SOUNDS['point'].play()


        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False

def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2} #lower Pipe
    ]
    return pipe






if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init() # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by CodeWithHarry')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('data:image/jpeg;base64,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').convert_alpha(),
        pygame.image.load('data:image/jpeg;base64,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').convert_alpha(),
        pygame.image.load('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlMrU46Qwyt3m9hwbUKv8rpUrrS_YvSXuDEg&usqp=CAU').convert_alpha(),
        pygame.image.load('data:image/jpeg;base64,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').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    ) 

    GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a button
        mainGame() # This is the main game function