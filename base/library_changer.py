from base import important_constants


class LibraryChanger:
    # TODO add link for this code (replace 'insert_link_here')
    """ A class that allows the user to modify constants and other variables instead of actually modifying the code.
        IMPORTANT: All the methods of this class must be called from the second line onwards with the first line being
        from base.library_changer import LibraryChanger, so none of the other code is initialized with the old constants.
        See insert_link_here for example"""

    @staticmethod
    def set_screen_dimensions(screen_length, screen_height):
            """Sets the dimensions of the screen. IMPORTANT see class description for details on how to call the methods """

            important_constants.SCREEN_LENGTH = screen_length
            important_constants.SCREEN_HEIGHT = screen_height

    @staticmethod
    def set_background_color(background_color):
        """Sets the background color of the screen (doesn't affect anything if an image is the background)"""

        important_constants.BACKGROUND_COLOR = background_color

    @staticmethod
    def set_number_of_frames_history_keeper_stores(number_of_frames_history_keeper_stores):
        """Sets the number of frames the HistoryKeeper keeps in it at one time"""

        important_constants.NUMBER_OF_FRAMES_HISTORY_KEEPER_STORES = number_of_frames_history_keeper_stores

