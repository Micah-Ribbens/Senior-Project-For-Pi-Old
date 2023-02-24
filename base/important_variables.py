"""Holds all the important variables for the game like screen_dimensions, BACKGROUND_COLOR, etc"""

from base.keyboard import Keyboard
from gui_components.window import Window
from base.important_constants import *
from library_abstraction.keys import *

keyboard = Keyboard()
game_window = Window(SCREEN_LENGTH, SCREEN_HEIGHT, BACKGROUND_COLOR, "Game Basics")
