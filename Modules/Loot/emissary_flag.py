"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

from pyglet.text import Label
from pyglet.shapes import Circle
from helpers import calculate_distance, object_to_screen, main_batch, TEXT_OFFSET_X, TEXT_OFFSET_Y
from Modules.mapping import emflags
from Modules.display_object import DisplayObject

EMISSARY_FLAG_COLOR = (255, 255, 255)
EMISSARY_FLAG_LABEL_COLOR = (255, 255, 255, 255)
CIRCLE_SIZE = 2  # The size of the indicator circle we want


class EmissaryFlag(DisplayObject):
    """
    Class to generate information for an emissary flag object in memory
    """

    def __init__(self, memory_reader, actor_id, address, my_coords, raw_name):
        """
        Upon initialization of this class, we immediately initialize the
        DisplayObject parent class as well (to utilize common methods)

        We then set our class variables and perform all of our info collecting
        functions, like finding the actors base address and converting the
        "raw" name to a more readable name per our Mappings. We also create
        a circle and label and add it to our batch for display to the screen.

        All of this data represents an "Emissary Flag". If you want to add more, you will
        need to add another class variable under __init__ and in the update()
        function

        :param memory_reader: The SoT MemoryHelper Object we use to read memory
        :param address: The address in which the AActor begins
        :param my_coords: a dictionary of the local players coordinates
        :param raw_name: The raw actor name used to translate w/ mapping.py
        """
        # Initialize our super-class
        super().__init__(memory_reader)

        self.actor_id = actor_id
        self.address = address
        self.actor_root_comp_ptr = self._get_root_comp_address(address)
        self.my_coords = my_coords
        self.raw_name = raw_name

        # Generate our emissary flag's info
        self.name = emflags.get(self.raw_name).get("Name")
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        self.distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        # All of our actual display information & rendering
        self.color = EMISSARY_FLAG_COLOR
        self.text_str = self._built_text_string()
        self.text_render = self._build_text_render()
        self.icon = self._build_circle_render()

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def _build_circle_render(self) -> Circle:
        """
        Creates a circle located at the screen coordinates (if they exist).
        Uses the color specified in our globals w/ a size of 10px radius.
        Assigns the object to our batch & group
        """
        if self.screen_coords:
            return Circle(self.screen_coords[0], self.screen_coords[1],
                          CIRCLE_SIZE, color=self.color, batch=main_batch)

        return Circle(0, 0, CIRCLE_SIZE, color=self.color, batch=main_batch)

    def _built_text_string(self) -> str:
        """
        Generates a string used for rendering. Separate function in the event
        you need to add more data (Sunk %, hole count, etc)
        """
        return f"{self.name} - {self.distance}m"

    def _build_text_render(self) -> Label:
        """
        Function to build our actual label which is sent to Pyglet. Sets it to
        be located at the screen coordinated + our text_offsets from helpers.py

        Assigns the object to our batch & group

        :rtype: Label
        :return: What text we want displayed next to the emissary flag
        """
        if self.screen_coords:
            return Label(self.text_str,
                         color=EMISSARY_FLAG_LABEL_COLOR,
                         x=self.screen_coords[0] + TEXT_OFFSET_X,
                         y=self.screen_coords[1] + TEXT_OFFSET_Y,
                         # x=self.screen_coords[0],
                         # y=self.screen_coords[1],
                         batch=main_batch)

        return Label(self.text_str, color=EMISSARY_FLAG_LABEL_COLOR, x=0, y=0, batch=main_batch)

    def update(self, my_coords: dict):
        """
        A generic method to update all the interesting data about an emissary flag
        object, to be called when seeking to perform an update on the
        Actor without doing a full-scan of all actors in the game.

        1. Determine if the actor is what we expect it to be
        2. See if any data has changed
        3. Update the data if something has changed

        In theory if all data is the same, we could *not* update our Label's
        text, therefore saving resources. Not implemented, but a possibility
        """
        if self._get_actor_id(self.address) != self.actor_id:
            self.to_delete = True
            self.icon.delete()
            self.text_render.delete()
            return

        self.my_coords = my_coords
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        new_distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        if self.screen_coords:
            if new_distance < 4000:
                self.text_render.visible = True
                self.icon.visible = True
            else:
                self.text_render.visible = False
                self.icon.visible = False

            # Update the position of our circle and text
            self.icon.x = self.screen_coords[0]
            self.icon.y = self.screen_coords[1]
            self.text_render.x = self.screen_coords[0]
            self.text_render.y = self.screen_coords[1]

            # Update our text to reflect out new distance
            self.distance = new_distance
            self.text_str = self._built_text_string()
            self.text_render.text = self.text_str

        else:
            # if it isn't on our screen, set it to invisible to save resources
            self.text_render.visible = False
            self.icon.visible = False
