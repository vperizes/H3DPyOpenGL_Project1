import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()

screen_width = 1000
screen_height = 800

# this defines the size of the screen displayed AND how it will be rendered
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')  # this sets the title of the game

# Declare method that sets up camera. This is an orthographic projection
def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)  # drawing the camera in 2D starting from 0-640 in x dir

# This block of code allows the window to stay open - a loop that runs forever until the user quits
done = False  # setting this is a bool var to define if the user is done with the application window
init_ortho()  # calling method for camera setup
while not done:
    for event in pygame.event.get():  # this get all events that happened in loop and stores in var event
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clears out color and depth info from frame buffer
    glMatrixMode(GL_MODELVIEW)  # sets up openGL to start drawing objects in MODEL coordinate system - diff form
    # projection coordinate system for camera
    glLoadIdentity()  # clears whatever is in MODEL view
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(100, 50)
    glVertex2i(630, 450)
    glEnd()
    pygame.display.flip()  # this flips display to second buffer (see screen var)
    pygame.time.wait(100)  # this makes sure that our loop pauses for 100 msec before it loops again - Allows you to
    # see animations. Completely optional
pygame.quit()
