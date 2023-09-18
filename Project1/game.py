# import pygame
# x = pygame.init()
# gameWindow = pygame.display.set_mode((1200,500))
# pygame.display.set_caption("my first game")

# exit_game = False
# game_over = False
# while not exit_game:
#     for event in pygame.event.get():
        # if event.type==pygame.QUIT:
        #     exit = True
            
#         if event.type == pygame.KEYDOWN:
#             if event.key== pygame.K_RIGHT:
#                 print("you have ressed right arrow")

# pygame.quit()
# quit()

import pygame

pygame.init()

screen_width = 1200
screen_height = 600
gameWindow = pygame.display.set_mode((screen_height,screen_height))
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

pygame.display.set_caption("Snake Game")
pygame.display.update()

exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
clock = pygame.time.Clock()
fps = 30

while not exit_game:
    for event in pygame.event.get():
        # print(event)
        if event.type==pygame.QUIT:
            # print(event.type)
            exit = True
        if  event.type == pygame.KEYDOWN:
            # print(event.type)
            if event.key == pygame.K_RIGHT:
                # print(event.key)
                print(snake_x)
                snake_x = snake_x + 10
                print(snake_x)
                
    gameWindow.fill(black)
    pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
quit()    