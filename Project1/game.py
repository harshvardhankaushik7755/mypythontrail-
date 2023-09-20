import pygame   
import random

pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\Nandani\\Desktop\\PythonCode\\Project1\\song.mp3")
pygame.mixer.music.play()
screen_width = 1200
screen_height = 600

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
gameWindow = pygame.display.set_mode((screen_height,screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()
pygame.init()
# game specific vars
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text,colour,x,y):
        screen_text = font.render(text, True, colour)
        gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, colour, snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, colour, [x, y, snake_size, snake_size])

def welcome_screen():
    exit_game = False
    while not exit_game:
        gameWindow.fill(blue)
        text_screen("Welcome To Snakes", black, 100, 320)
        text_screen("Press Space bar to Play", black, 100, 350)
        text_screen("Good luck!!", black, 100, 250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 45

    snake_size = 15

    fps = 60

    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    

    
    score = 0
    food_y = random.randint(20, screen_height/2)
    food_x = random.randint(20, screen_width/2)

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen(" Oops!! Game Over!! press enter to continue", red, screen_width/2, screen_height/2)
            
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    # print(event.type)
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    # print(event.type)
                    exit_game = True
                if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                    
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
            
            if abs(snake_x - food_x)< 10 and abs(snake_y - food_y)< 10:
                score = score+10      
                food_y = random.randint(20, screen_height/2)
                food_x = random.randint(20, screen_width/2)
                snk_length+=5
    
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print("Game Over")   
            gameWindow.fill(black)    
            text_screen("Score: "+ str(score),red,5,5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            #pygame.draw.rect(gameWindow, white, [food_x, food_y, snake_size, snake_size])
            plot_snake(gameWindow, white, snk_list, snake_size)
            #pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()  
welcome_screen()
#gameloop()