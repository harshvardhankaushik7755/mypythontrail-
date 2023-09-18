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
black = (255,0,0)
red = (0,0,0)

pygame.display.set_caption("Snake Game")
pygame.display.update()

exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit = True

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    
pygame.quit()
quit()    