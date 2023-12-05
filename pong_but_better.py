import pygame

pygame.init()

#INITIAL
#This creates a blank window with width at 1000 and height at 600
WIDTH, HEIGHT = 1000,600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nat's Ping Pong")
run = True

#mainloop
while run:
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT:
            run = False