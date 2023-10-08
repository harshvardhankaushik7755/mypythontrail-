import pygame

pygame.init()
width = 1000
height = 900
screen = pygame.display.set_mode(width, height)
font = pygame.font.Font("freesanbold.ttf", 50)
timer = pygame.time.Clock()
fps = 60
pygame.display.set_caption("CHESS")
#game vars + imgs
white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
white_locations = [(0, 0), (1,0),(2,0),(3,0), (4,0),(5,0),(6,0),(7,0)
                   (0, 1), (1,1),(2,1),(3,1), (4,1),(5,1),(6,1),(7,1)]
black_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
black_locations = [(0, 7), (1,7),(2,7),(3,7), (4,0),(5,0),(6,0),(7,0)
                   (0, 6), (1,6),(2,6),(3,6), (4,6),(5,6),(6,6),(7,6)]  
cap_pieces_white = []
black_cap_pieces = []
turn_step = 0
selection = 100
valid_moves = []

run = True
while run:
    timer.tick(fps)
    screen.fill("dark gray")
    
    #event handling
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.flip()
pygame.quit()