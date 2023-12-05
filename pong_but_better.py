import pygame

pygame.init()

#INITIAL
#This creates a blank window with width at 1000 and height at 600
WIDTH, HEIGHT = 1000,600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nat's Ping Pong")
run = True

#colors
BLUE = (0, 0, 255)

#for the ball
# keeping the ball at the exact center of the screen
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius

#mainloop
while run:
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT:
            run = False

#drawing of objects
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius )
    #updating the position of the ball
    pygame.display.update()