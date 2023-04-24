import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 800

# this defines the size of the screen displayed AND how it will be rendered
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')  # this sets the title of the game

# This block of code allows the window to stay open - a loop that runs forever until the user quits
done = False  # setting this is a bool var to define if the user is done with the application window
while not done:
    for event in pygame.event.get():  # this get all events that happened in loop and stores in var event
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()  # this flips display to second buffer (see screen var)
    pygame.time.wait(100)  # this makes sure that our loop pauses for 100 msec before it loops again - Allows you to
    # see animations
pygame.quit()
