import pygame

from gui_components.dimensions import Dimensions
from base.engines import CollisionsEngine
from base.events import Event
from base.history_keeper import HistoryKeeper
from base.utility_functions import *
from base.velocity_calculator import VelocityCalculator
from game_dependencies.platformer.gravity_engine import GravityEngine
from games.platformer.players.player import Player
from games.platformer.platformer_screen import PlatformerScreen
from base.important_variables import *
from gui_components.grid import Grid
from gui_components.text_box import TextBox
from base.colors import *


class GeneratorTestScreen(PlatformerScreen):
    """A screen that is used for testing the generator"""

    screen_number_field = None
    platform_type_field = None
    generation_difficulty_field = None
    main_platform_number_field = None
    main_platforms = []
    hardest_platforms = []
    easiest_platforms = []
    current_index = 0
    is_hard_platform = True
    hud = None
    time = 0
    has_started = False
    can_change_index = False

    def __init__(self, screen_number, total_screens, generation_difficulty, main_platforms, hardest_platforms, easiest_platforms):
        """Initializes the object"""

        self.players = [Player(KEY_A, KEY_D, KEY_W, KEY_S, KEY_F)]
        self.gravity_engine = GravityEngine(self.players, self.players[0].jumping_path.acceleration)

        self.hardest_platforms, self.easiest_platforms = hardest_platforms, easiest_platforms
        self.main_platforms = main_platforms

        # Have to do this here, so I can put the player on the platform
        other_platform_list = self.hardest_platforms if self.is_hard_platform else self.easiest_platforms
        self.platforms = [self.main_platforms[self.current_index], other_platform_list[self.current_index]]

        for player in self.players:
            player.gravity_engine = self.gravity_engine
            player.left_edge = self.platforms[0].left_edge + 10
            player.base_top_edge = self.platforms[0].top_edge - player.height
            player.set_top_edge(player.base_top_edge)

        self.screen_number_field = TextBox(f"Screen Number {screen_number} of {total_screens}", 20, purple, white, False)
        self.platform_type_field = TextBox("", 20, False, medium_green, white)
        self.generation_difficulty_field = TextBox(f"Generation Difficulty: {generation_difficulty}", 20, black, white, False)
        self.main_platform_number_field = TextBox("", 20, blue, white, False)

        self.hud = [self.screen_number_field, self.platform_type_field, self.generation_difficulty_field, self.main_platform_number_field]
        grid = Grid(Dimensions(0, 0, SCREEN_LENGTH, SCREEN_HEIGHT * .1), 1, None)
        grid.turn_into_grid(self.hud, None, None)

    def run_base_game(self):
        """Runs everything that the base game is doing (with some exceptions like side_scrolling)"""

        self.gravity_engine.run()
        for player in self.players:
            # Have to do this every cycle so the player is realisticly affected by gravity every cycle
            if player.platform_is_on is not None and not CollisionsEngine.is_collision(player, player.platform_is_on):
                player.set_is_on_platform(False, None)

            player.run()

        if self.frames % 1 == 0 and self.frames > 1:
            self.update_game_objects()
            self.run_all_collisions()

            # All the enemies and players should do something based on the updated collision they got from 'self.run_all_collisions()'
            for game_object in self.enemies + self.players:
                game_object.run_collisions(self.last_time)

        if self.frames % 1 == 0:
            self.add_game_objects()
            self.last_time = VelocityCalculator.time

        for enemy in self.enemies:
            enemy.run_player_interactions(self.players)

        self.frames += 1

    def run(self):
        """Runs all that is necessary to have a generator test screen"""

        self.run_base_game()

        other_platform_list = self.hardest_platforms if self.is_hard_platform else self.easiest_platforms
        self.platforms = [self.main_platforms[self.current_index], other_platform_list[self.current_index]]

        self.main_platform_number_field.text = f"Main Platform #{self.current_index + 1}"
        self.platform_type_field.text = "Showing Hard Platform" if self.is_hard_platform else "Is Showing Easy Platform"

        if key_is_clicked(KEY_DOWN) and self.can_change_index:
            self.current_index = get_previous_index(self.current_index, len(self.main_platforms) - 1)

        if key_is_clicked(KEY_UP) and self.can_change_index:
            self.current_index = get_next_index(self.current_index, len(self.main_platforms) - 1)

        if key_is_clicked(KEY_QUESTION_MARK):
            self.is_hard_platform = not self.is_hard_platform

        self.can_change_index = True

        # If the platforms were changed then the game should be reset
        if key_is_clicked(KEY_DOWN) or key_is_clicked(KEY_UP):
            self.reset_game()
            self.can_change_index = False

    def get_components(self):
        """returns: Component[]; all the components that should be ran and rendered"""

        return self.hud + self.platforms + self.players

    def reset_game(self):
        """Resets the game after the player's death"""

        for player in self.players:
            player.left_edge = self.main_platforms[self.current_index].left_edge
            player.base_top_edge = self.main_platforms[self.current_index].top_edge - player.height
            player.set_top_edge(player.base_top_edge)
            player.reset()

        HistoryKeeper.reset()
        self.gravity_engine.reset()
        self.frames = 0
        self.has_started = False

    def setup(self):
        self.reset_game()

