import pyglet
import os
from pyglet.text import Label
from pyglet.gl import Config
from utils.helpers import SOT_WINDOW, SOT_WINDOW_H, SOT_WINDOW_W, main_batch, logger
from utils.sot_hack import SoTMemoryReader

# The FPS __Target__ for the program.
FPS_TARGET = 60

# Pyglet clock used to track time via FPS
clock = pyglet.clock.Clock()


def generate_all(_):
    """
    Triggers an entire read_actors call in our SoT Memory Reader. Will
    re-populate all the display objects if something entered the screen
    or render distance.
    """
    smr.read_actors()


def update_graphics(_):
    """
    Our main graphical loop which updates all of our "interesting" items.
    During a "full run" (update_all()), a list of the objects near us, and we
    care about is generated. Each of those objects has a ".update()" method
    we use to re-poll data for that item (required per display_object.py)
    """
    # Update our players coordinate information
    smr.update_my_coords()

    # Initialize a list of items which are no longer valid in this loop
    to_remove = []

    # Update static 'actors' or those ESP elements that don't actually have
    # an assigned/identifiable actor but require memory reads and updating
    for static_actor in smr.display_static_objects:
        # Call the update function within the object
        static_actor.update(smr.my_coords)

        # If the actor isn't the actor we expect (per .update), prepare to nuke
        if static_actor.to_delete:
            to_remove.append(static_actor)

    # For each actor that is stored from the most recent run of read_actors
    for actor in smr.display_objects:
        # Call the update function within the actor object
        actor.update(smr.my_coords)

        # If the actor isn't the actor we expect (per .update), prepare to nuke
        if actor.to_delete:
            to_remove.append(actor)

    # Clean up any items which aren't valid anymore
    for removable in to_remove:
        smr.display_objects.remove(removable)


if __name__ == '__main__':
    # Initialize our SoT Hack object, and do a first run of reading actors
    smr = SoTMemoryReader()

    # You may want to add/modify this custom config per the pyglet docs to
    # disable vsync or other options: https://tinyurl.com/45tcx6eu
    config = Config(double_buffer=True, depth_size=24, sample_buffers=1, samples=2, alpha_size=8)

    # Create an overlay window with Pyglet at the same size as our SoT Window
    window = pyglet.window.Window(SOT_WINDOW_W, SOT_WINDOW_H,
                                  vsync=False, style='overlay', config=config,
                                  caption="")
    hwnd = window._hwnd  # pylint: disable=protected-access

    # Move our window to the same location that our SoT Window is at
    window.set_location(SOT_WINDOW[0], SOT_WINDOW[1])


    @window.event
    def on_draw():
        """
        The event which our window uses to determine what to draw on the
        screen. First clears the screen, then draws both our batch (think of a canvas)
        """
        window.clear()

        # Draw our main batch
        main_batch.draw()


    # # Initializing the window for writing
    # init = initialize_window()

    # We schedule an "update all" to scan all actors every 5seconds
    pyglet.clock.schedule_interval(generate_all, 5)

    # We schedule a check to make sure the game is still running every 3 seconds
    pyglet.clock.schedule_interval(smr.rm.check_process_is_active, 3)

    # We schedule a basic graphics load which is responsible for updating
    # the actors we are interested in (from our generate_all). Runs as fast as possible
    pyglet.clock.schedule(update_graphics)

    pyglet.font.add_file("resources" + os.sep + "font" + os.sep + "cq-mono.ttf")
    pyglet.font.add_file("resources" + os.sep + "font" + os.sep + "univa.ttf")

    crosshair = Label("+",
                      font_size=15,
                      color=(0, 255, 0, 255),
                      x=SOT_WINDOW_W * .5,
                      y=SOT_WINDOW_H * .5,
                      anchor_x="center",
                      anchor_y="center",
                      batch=main_batch)

    # Runs our application, targeting a specific refresh rate (1/60 = 60fps)
    pyglet.app.run(interval=1 / FPS_TARGET)
    # Note - ***Nothing past here will execute as app.run() is a loop***
