import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500))  # draw blank window 1000 wide by 500 high
done = False
red_circle = True
x = 500                                         #starting location of circle
y = 250

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
        if pressed[pygame.K_UP]:        y -= 5          # move 5 pixels down
        if pressed[pygame.K_DOWN]:      y += 5          # move 5 pixels up
        if pressed[pygame.K_LEFT]:      x -= 5          # move 5 pixels left
        if pressed[pygame.K_RIGHT]:     x += 5          # move 5 pixels right
        
        screen.fill((0, 0, 0))                          # blank the screen
        position = (x,y)
        if red_circle: color = (255, 0, 0)              # use red color
        else: color = (0, 100, 0)                       # use other color
        pygame.draw.circle(screen, color, position, 30, 0)      # draw a circle        
        pygame.display.update()                         # update the display
        clock.tick(60)                                  # delay 60 milliseconds
