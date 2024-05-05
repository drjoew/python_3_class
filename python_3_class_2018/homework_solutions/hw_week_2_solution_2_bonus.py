""" Game rewritten to have values set at variables rather than put in various places
The is a better way to write the code, it make it more maintainable.
We can change the size of the screen and all values get updated
We can change the size of the ball (circle) and all values get updated
"""
""" In this game the ball bounces off the wall and the direction of the arrow keys reverse
"""

import pygame

pygame.init()
screen_width = 1000
screen_height = 500
circle_radius = 30
UP_DOWN_reversed = False
LEFT_RIGHT_reversed = False
screen = pygame.display.set_mode((screen_width, screen_height))  # draw blank window 1000 wide by 500 high
done = False
red_circle = True
x = int(screen_width/2)                                        #starting location of circle
y = int(screen_height/2)

clock = pygame.time.Clock()

while (not done):
        # this program does not exit gracefully from Python shell but does work
        # correctly from command line/terminal
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                        pygame.display.quit()
                        pygame.quit()
                        exit()
                if event.type == pygame.QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        red_circle = not red_circle
        
        pressed = pygame.key.get_pressed()              # check for key press
        if pressed[pygame.K_UP]    and UP_DOWN_reversed    == False:      y -= 5          # move 5 pixels down
        if pressed[pygame.K_DOWN]  and UP_DOWN_reversed    == False:      y += 5          # move 5 pixels up
        if pressed[pygame.K_LEFT]  and LEFT_RIGHT_reversed == False:      x -= 5          # move 5 pixels left
        if pressed[pygame.K_RIGHT] and LEFT_RIGHT_reversed == False:      x += 5          # move 5 pixels right
        if pressed[pygame.K_UP]    and UP_DOWN_reversed    == True:       y += 5          # move 5 pixels up
        if pressed[pygame.K_DOWN]  and UP_DOWN_reversed    == True:       y -= 5          # move 5 pixels down
        if pressed[pygame.K_LEFT]  and LEFT_RIGHT_reversed == True:       x += 5          # move 5 pixels right
        if pressed[pygame.K_RIGHT] and LEFT_RIGHT_reversed == True:       x -= 5          # move 5 pixels left        
        #
        if x>=screen_width-circle_radius:                                # check to see if near boundry and need to reverse direction
                #xp = x-screen_width
                LEFT_RIGHT_reversed = not LEFT_RIGHT_reversed
        elif x<=circle_radius:
                #xp = x+screen_width
                LEFT_RIGHT_reversed = not LEFT_RIGHT_reversed
        #else:
                #xp = x               
        if y>=screen_height-circle_radius:
                #yp = y-screen_height
                UP_DOWN_reversed = not UP_DOWN_reversed 
        elif y<=circle_radius:
                #yp = y+screen_height
                UP_DOWN_reversed = not UP_DOWN_reversed
        #else:
                #yp = y
                
        screen.fill((0, 0, 0))                          # blank the screen
        position = (x,y)
        if red_circle: color = (255, 0, 0)              # use red color
        else: color = (0, 100, 0)                       # use other color        
        pygame.draw.circle(screen, color, position, circle_radius, 0)      # draw a circle   
        pygame.display.update()                         # update the display
        clock.tick(60)                                  # delay 60 milliseconds
