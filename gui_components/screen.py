from base.colors import light_gray
from base.utility_functions import render_image
from gui_components.component import Component
from base.important_variables import *
from base.utility_functions import *

screen_sized_component = Component()
screen_sized_component.number_set_dimensions(0, 0, SCREEN_LENGTH, SCREEN_HEIGHT)


class Screen(Component):
    """ Is the only thing that shows on the window at a time. The Window class (gui_components/window.py) will call the Screen's
        run() and render_background() method will be called every game frame. It will also the run() and render() method for
        all the Component(s) that the Screen's get_components() method returns"""

    components = []
    path_to_background_image = ""
    is_visible = True
    background_color = light_gray

    def __init__(self, path_to_background_image="", background_color=light_gray):
        """ Initializes the object and also loads the image which is at the path 'path_to_background_image.' No image will
            be loaded if path_to_background_image is ''"""

        self.path_to_background_image = path_to_background_image
        self.background_color = background_color

        if self.path_to_background_image != "":
            load_image(path_to_background_image)

    def get_components(self):
        """:returns: Component[]; the components of the screen"""

        return self.components

    def render_background(self):
        """Renders the background image that is at the path 'path_to_background_image'"""

        if self.path_to_background_image != "":
            render_image(self.path_to_background_image, 0, 0, SCREEN_LENGTH, SCREEN_HEIGHT)

        else:
            screen_sized_component.color = self.background_color
            screen_sized_component.render()
