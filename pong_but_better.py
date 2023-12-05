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
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#for the ball
# keeping the ball at the exact center of the screen
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius

#ball velocity
ball_vel_x, ball_vel_y = 1,1

#paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 -paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)

#mainloop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT:
            run = False

    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y


#drawing of objects
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius )
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    #updating the position of the ball
    pygame.display.update()