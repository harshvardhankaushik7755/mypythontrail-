import pygame
import random
import math

# init

pygame.init()

#title pic etc:
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("C:\\Users\\Nandani\\Desktop\\PythonCode\\Project1\\ufo.png")
pygame.display.set_icon(icon)
# background
background = pygame.image.load("C:\\Users\\Nandani\\Desktop\\PythonCode\\Project1\\bac.jpg")
background = pygame.transform.scale(background, (800, 600))

#player
playerimg = pygame.image.load("C:\\Users\\Nandani\\Desktop\\PythonCode\\Project1\\spaceship.png")
playerimg = pygame.transform.scale(playerimg, (64, 64))
playerX = 350
playerY = 450
playerX_change = 0

#enemy
enemyimg = pygame.image.load("C:\\Users\\Nandani\\Desktop\\PythonCode\\Project1\\enemy.png")
enemyimg = pygame.transform.scale(enemyimg, (64, 64))
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 50)
enemyX_change = 0.5
enemyY_change = 25

#bullet
bulletimg = pygame.image.load("C:\\Users\\Nandani\\Desktop\\PythonCode\\Project1\\bullet.png")
bulletimg = pygame.transform.scale(bulletimg, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0



def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y):
    screen.blit(enemyimg, (x, y))

def firebullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))
    
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False
    
#game loop
running = True
while running:
    #rgb
    screen.fill((0, 0, 0))
    #background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #MOVEMENTS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
                
            if event.key == pygame.K_RIGHT:
                playerY_change = 0.5
                
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    firebullet(bulletX, bulletY)    

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.5
             
    # boundaries
    #player   
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736 
    
    #enemy
    
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX = 0.5
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX = -0.5
        enemyY += enemyY_change
        
    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state is "fire":
        firebullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    # collision
    collision = iscollision(enemyX, enemyY, bulletX, bulletY)
    if iscollision(enemyX, enemyY, bulletX, bulletY):
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 50)
        
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update() 