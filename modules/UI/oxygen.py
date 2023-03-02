"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

from pyglet.text import Label
from utils.helpers import main_batch, \
    TEXT_DPI, TEXT_FONT_NAME, TEXT_FONT_SIZE, \
    SOT_WINDOW_W, SOT_WINDOW_H, OFFSETS
from modules.display_object import DisplayObject

OXYGEN_LABEL_COLOR = (255, 255, 255, 255)


class Oxygen(DisplayObject):
    """
    Class to generate information for an event object in memory
    """

    def __init__(self, memory_reader, athena_player_character):
        """
        Upon initialization of this class, we immediately initialize the
        DisplayObject parent class as well (to utilize common methods)

        We then set our class variables and perform all of our info collecting
        functions, like finding the actors base address and converting the
        "raw" name to a more readable name per our Mappings. We also create
        a circle and label and add it to our batch for display to the screen.

        All of this data represents an "Event". If you want to add more, you will
        need to add another class variable under __init__ and in the update()
        function

        :param memory_reader: The SoT MemoryHelper Object we use to read memory
        :param my_coords: a dictionary of the local players coordinates
        """
        # Initialize our super-class
        super().__init__(memory_reader)

        self.my_athena_player_character = athena_player_character
        self.raw_name = "Oxygen_ESP"

        # All of our actual display information & rendering
        self.text_str = self._built_text_string(self.my_athena_player_character)
        self.text_render = self._build_text_render()

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def _built_text_string(self, athena_player_character: int) -> str:
        """
        Based on the direction the player is facing, as per the camera's
        y coordinate, return a cardinal direction

        :param: actor y coordinate
        :rtype: string
        :return: the cardinal direction the player is facing
        """
        test_val = self.rm.read_ptr(athena_player_character +
                                    OFFSETS.get('AthenaPlayerCharacter.DrowningComponent'))
        oxygen_val = self.rm.read_float(test_val +
                                        OFFSETS.get('DrowningComponent.OxygenLevel'))

        return f"Oxygen: {str(round(oxygen_val * 100))}%"

    def _build_text_render(self) -> Label:
        """
        Function to build our actual label which is sent to Pyglet. Sets it to
        be located at the screen coordinated + our text_offsets from helpers.py

        Assigns the object to our batch & group

        :rtype: Label
        :return: What text we want displayed next to the event
        """
        if self.my_athena_player_character:
            return Label(self.text_str,
                         font_size=4,
                         x=SOT_WINDOW_W * .01,
                         y=SOT_WINDOW_H * .5,
                         dpi=300,
                         batch=main_batch)

        return Label(self.text_str, color=OXYGEN_LABEL_COLOR,
                     font_name=TEXT_FONT_NAME, font_size=TEXT_FONT_SIZE, x=0, y=0, dpi=TEXT_DPI, batch=main_batch)

    def update(self, my_coords: dict):
        """
        A generic method to update all the interesting data about an event
        object, to be called when seeking to perform an update on the
        Actor without doing a full-scan of all actors in the game.

        1. Determine if the actor is what we expect it to be
        2. See if any data has changed
        3. Update the data if something has changed

        In theory if all data is the same, we could *not* update our Label's
        text, therefore saving resources. Not implemented, but a possibility
        """
        if self.my_athena_player_character:
            self.text_render.visible = True

            # Update our text to reflect out new distance
            self.text_str = self._built_text_string(self.my_athena_player_character)
            self.text_render.text = self.text_str

        else:
            # if it isn't on our screen, set it to invisible to save resources
            self.text_render.visible = False
