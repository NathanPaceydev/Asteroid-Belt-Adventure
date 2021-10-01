#simple pygame program

#imports
import random
import pygame
import time
import numpy as np
#initalize library
pygame.init()

#set up the window displayed
# with user input
print("Enter Window Length:")
WINDOW_LENGTH  = int(input())

print("Enter the Window Width:")
WINDOW_WIDTH = int(input())

screen = pygame.display.set_mode([WINDOW_LENGTH, WINDOW_WIDTH])

# set the game to run until the user quits
running = True

## initalizing computation variables
# location x, y
location = [250,250]

# size item
size = 150
#time
t = 0
#center location in the screen
center = [WINDOW_LENGTH/2,WINDOW_WIDTH/2]

#radius of rotation
radius = (center[0]+center[1])/2
print(radius)

ballcolor = [0, 0, 250]

# main loop
while running:
        #iterate through the possible events in the pygame event attribute
        # set flag running to false if user quits
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # fill the background with rgb  colour
        screen.fill((255,255,223))
    
        # create a circle on the "screen", RGB, location, size
        pygame.draw.circle(screen,(ballcolor[0], ballcolor[1], ballcolor[2]), (location[0], location[1]), size)
        
        time.sleep(0.1)
        t+=1

        location[0] = center[0]+radius*np.sin(t)
        location[1] = center[1]+radius*np.cos(t)
        
        radius-=5

        size = random.randint(1,150)

        for i in range(len(ballcolor)):
            #print(ballcolor[i])
            ballcolor[i] = random.randint(0,250)

        if abs(radius)>WINDOW_WIDTH or abs(radius)>WINDOW_LENGTH:
            radius = 0
        # display the screen
        
        pygame.display.flip()

# else quit the program
pygame.quit()
