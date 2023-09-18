import pygame
import random

pygame.init()

screen_width = 1200
screen_height = 600

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

exit_game = False
game_over = False

snake_x = 45
snake_y = 55

snake_size = 15

fps = 60

init_velocity = 5
velocity_x = 0
velocity_y = 0

score = 0

snk_list = []
snk_length = 1

gameWindow = pygame.display.set_mode((screen_height,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()

food_y = random.randint(20, screen_height/2)
food_x = random.randint(20, screen_width/2)
font = pygame.font.SysFont(None, 55)

def screen_score(text,colour,x,y):
        screen_text = font.render(text, True, colour)
        gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, colour, snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])

while not exit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:
            # print(event.type)
            exit = True
        if  event.type == pygame.KEYDOWN:
            # print(event.type)
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
                
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
                
            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0
                
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0              
    
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    
    if abs(snake_x - food_x)< 6 and abs(snake_y - food_y)< 6:
        score = score+1      
        food_y = random.randint(20, screen_height/2)
        food_x = random.randint(20, screen_width/2)
        snk_length+=5
        
        
    gameWindow.fill(white)    
    screen_score("Score: "+ str(score*10),red,5,5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    
    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)
    
    if len(snk_list)>snk_length:
        del snk_list[0]
    
    #pygame.draw.rect(gameWindow, white, [food_x, food_y, snake_size, snake_size])
    plot_snake(gameWindow, black, snk_list, snake_size)
    #pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
quit()    