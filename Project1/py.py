import pygame

pygame.init()

#screen_colo
red = (255, 0, 0)

screen_height = 1000
screen_width = 1000
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("screen by Harsh")
exit = False

while not exit:
    gameWindow.fill(red)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.quit()
    quit()
