"""Has all the variables that are important for the pygame code to run"""

import pygame

pygame.init()
pygame.joystick.init()
joystick = None

if pygame.joystick.get_count() >= 1:
    joystick = pygame.joystick.Joystick(0)

WINDOW = None
BACKGROUND_COLOR = None
RENDERS_PER_SECOND = 100000
RUN_CALLS_PER_SECOND = 10000
