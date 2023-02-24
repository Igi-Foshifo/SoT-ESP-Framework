"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

import struct
from pyglet.text import Label
from utils.helpers import main_batch, SOT_WINDOW_H, SOT_WINDOW_W, OFFSETS, \
    TEXT_DPI, TEXT_FONT_NAME, TEXT_FONT_SIZE
from Modules.display_object import DisplayObject

COMPASS_LABEL_COLOR = (255, 255, 255, 255)
CIRCLE_SIZE = 5  # The size of the indicator circle we want


class Compass(DisplayObject):
    """
    Class to generate information for an event object in memory
    """

    def __init__(self, memory_reader, address, my_coords):
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
        :param address: The address in which the AActor begins
        :param my_coords: a dictionary of the local players coordinates
        """
        # Initialize our super-class
        super().__init__(memory_reader)

        self.address = address
        self.my_coords = my_coords

        # All of our actual display information & rendering
        self.text_str = self._built_text_string()
        self.text_render = self._build_text_render()

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def _built_text_string(self) -> str:
        """
        Generates a string used for rendering.
        """
        return f"{self.my_coords}"

    def _build_text_render(self) -> Label:
        """
        Function to build our actual label which is sent to Pyglet. Sets it to
        be located at the screen coordinated + our text_offsets from helpers.py

        Assigns the object to our batch & group

        :rtype: Label
        :return: What direction we want to show to represent the cam_y coordinate
        """
        if self.my_coords:
            return Label(self.text_str,
                         color=COMPASS_LABEL_COLOR,
                         # font_name=TEXT_FONT_NAME,
                         font_size=TEXT_FONT_SIZE,
                         x=SOT_WINDOW_W * .5,
                         y=SOT_WINDOW_H * .9,
                         dpi=TEXT_DPI,
                         batch=main_batch)

        return Label(self.text_str, color=COMPASS_LABEL_COLOR,
                     font_name=TEXT_FONT_NAME, font_size=TEXT_FONT_SIZE, x=0, y=0, dpi=TEXT_DPI, batch=main_batch)

    def update(self, my_coords: dict):
        actor_bytes = self.rm.read_bytes(self.address +
                                         OFFSETS.get('PlayerCameraManager.CameraCache') +
                                         OFFSETS.get('CameraCacheEntry.MinimalViewInfo') +
                                         12,
                                         44)
        unpacked = struct.unpack("<ffffff16pf", actor_bytes)

        self.my_coords = unpacked[4]

        if self.my_coords:
            self.text_str = self._built_text_string()
            self.text_render.text = self.text_str
            self.text_render.visible = True

        else:
            # if it isn't on our screen, set it to invisible to save resources
            self.text_render.visible = False
