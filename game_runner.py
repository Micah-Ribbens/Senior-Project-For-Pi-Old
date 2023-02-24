from base.library_changer import LibraryChanger
import cProfile

LibraryChanger.set_screen_dimensions(2200, 1300)


import pygame

from base.game_runner_function import run_game
from main_screen import MainScreen
from base.important_variables import game_window


# Have to use try except because pygame throws an error when the application is closed
cProfile.run("run_game(MainScreen())", None, "tottime")

# If there is no error thrown then the code should still be run
