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
ball_vel_x, ball_vel_y = 0.7, 0.7

#paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 -paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH -(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0


#mainloop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            #if key pressed is up or down arrow then move the paddles accordingly
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    #ball's movement controls
    if ball_y <= 0 + radius or ball_y >= HEIGHT -radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 -radius, HEIGHT/2 -radius
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 -radius
        ball_vel_x, ball_vel_y = 0.7, 0.7

    



    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel


#drawing of objects
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius )
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    #updating the position of the ball
    pygame.display.update()