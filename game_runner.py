from base.library_changer import LibraryChanger
import pygame
import cProfile

LibraryChanger.set_screen_dimensions(1000, 700)
LibraryChanger.set_game_library("pygame")

from base.game_runner_function import run_game
from main_screen import MainScreen

pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.play(-1)

# Have to use try except because pygame throws an error when the application is closed
# cProfile.run("run_game(MainScreen())", None, "tottime")
run_game(MainScreen())

