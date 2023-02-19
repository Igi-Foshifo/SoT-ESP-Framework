"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
For community support, please contact me on Discord: DougTheDruid#2784
"""

import struct
import logging
from memory_helper import ReadMemory
from helpers import OFFSETS, CONFIG, logger
from Modules.mapping import ship_keys, \
    gem_keys, \
    skull_keys, \
    shipwreck_keys, \
    resource_keys, \
    ai_common_drops_keys

from Modules.Ships.ship import Ship

from Modules.Players.crews import Crews

from Modules.Loot.gem import Gem
from Modules.Loot.skull import Skull
from Modules.Loot.resource import Resource

from Modules.Map.shipwreck import Shipwreck

from Modules.AI.ai_common_drop import AICommonDrop


class SoTMemoryReader:
    """
    Wrapper class to handle reading data from the game, parsing what is
    important, and returning it to be shown by pyglet
    """

    def __init__(self):
        """
        Upon initialization of this object, we want to find the base address
        for the SoTGame.exe, then begin to load in the static addresses for the
        uWorld, gName, gObject, and uLevel objects.

        We also poll the local_player object to get a first round of coords.
        When running read_actors, we update the local players coordinates
        using the camera-manager object

        Also initialize a number of class variables which help us cache some
        basic information
        """
        self.rm = ReadMemory("SoTGame.exe")
        base_address = self.rm.base_address
        logging.info(f"Process ID: {self.rm.pid}")

        u_world_offset = self.rm.read_ulong(
            base_address + self.rm.u_world_base + 3
        )
        u_world = base_address + self.rm.u_world_base + u_world_offset + 7
        self.world_address = self.rm.read_ptr(u_world)

        g_name_offset = self.rm.read_ulong(
            base_address + self.rm.g_name_base + 3
        )
        g_name = base_address + self.rm.g_name_base + g_name_offset + 7
        logging.info(f"SoT gName Address: {hex(g_name)}")
        self.g_name = self.rm.read_ptr(g_name)

        g_objects_offset = self.rm.read_ulong(
            base_address + self.rm.g_object_base + 2
        )
        g_objects = base_address + self.rm.g_object_base + g_objects_offset + 22
        logging.info(f"SoT gObject Address: {hex(g_objects)}")
        self.g_objects = self.rm.read_ptr(g_objects)

        self.u_level = self.rm.read_ptr(self.world_address +
                                        OFFSETS.get('World.PersistentLevel'))

        self.u_local_player = self._load_local_player()
        self.player_controller = self.rm.read_ptr(
            self.u_local_player + OFFSETS.get('LocalPlayer.PlayerController')
        )

        self.my_coords = self._coord_builder(self.u_local_player)
        self.my_coords['fov'] = 90

        self.actor_name_map = {}
        self.server_players = []
        self.display_objects = []
        self.crew_data = None

    def _load_local_player(self) -> int:
        """
        Returns the local player object out of uWorld.UGameInstance.
        Used to get the players coordinates before reading any actors
        :rtype: int
        :return: Memory address of the local player object
        """
        game_instance = self.rm.read_ptr(
            self.world_address + OFFSETS.get('World.OwningGameInstance')
        )
        local_player = self.rm.read_ptr(
            game_instance + OFFSETS.get('GameInstance.LocalPlayers')
        )
        return self.rm.read_ptr(local_player)

    def update_my_coords(self):
        """
        Function to update the players coordinates and camera information
        storing that new info back into the my_coords field. Necessary as
        we dont always run a full scan and we need a way to update ourselves
        """
        manager = self.rm.read_ptr(
            self.player_controller + OFFSETS.get('PlayerController.CameraManager')
        )
        self.my_coords = self._coord_builder(
            manager,
            OFFSETS.get('PlayerCameraManager.CameraCache')
            + OFFSETS.get('CameraCacheEntry.MinimalViewInfo'),
            fov=True)

    def _coord_builder(self, actor_address: int, offset=0x78, camera=True,
                       fov=False) -> dict:
        """
        Given a specific actor, loads the coordinates for that actor given
        a number of parameters to define the output
        :param int actor_address: Actors base memory address
        :param int offset: Offset from actor address to beginning of coords
        :param bool camera: If you want the camera info as well
        :param bool fov: If you want the FoV info as well
        :rtype: dict
        :return: A dictionary containing the coordinate information
        for a specific actor
        """
        if fov:
            actor_bytes = self.rm.read_bytes(actor_address + offset, 44)
            unpacked = struct.unpack("<ffffff16pf", actor_bytes)
        else:
            actor_bytes = self.rm.read_bytes(actor_address + offset, 24)
            unpacked = struct.unpack("<ffffff", actor_bytes)

        coordinate_dict = {"x": unpacked[0]/100, "y": unpacked[1]/100,
                           "z": unpacked[2]/100}
        if camera:
            coordinate_dict["cam_x"] = unpacked[3]
            coordinate_dict["cam_y"] = unpacked[4]
            coordinate_dict["cam_z"] = unpacked[5]
        if fov:
            coordinate_dict['fov'] = unpacked[7]

        return coordinate_dict

    def read_actors(self):
        """
        Represents a full scan of every actor within our render distance.
        Will create an object for each type of object we are interested in,
        and store it in a class variable (display_objects).
        Then our main game loop updates those objects
        """
        # On a full run, start by cleaning up all the existing text renders
        for display_ob in self.display_objects:
            try:
                display_ob.text_render.delete()
            except:
                continue
            try:
                display_ob.icon.delete()
            except:
                continue

        self.display_objects = []
        self.update_my_coords()

        actor_raw = self.rm.read_bytes(self.u_level + 0xa0, 0xC)
        actor_data = struct.unpack("<Qi", actor_raw)

        # Credit @mogistink https://www.unknowncheats.me/forum/members/3434160.html
        # One very large read for all the actors addresses to save us 1000+ reads every read_all
        level_actors_raw = self.rm.read_bytes(actor_data[0], actor_data[1] * 8)

        self.server_players = []
        for x in range(0, actor_data[1]):
            # We start by getting the ActorID for a given actor, and comparing
            # that ID to a list of "known" id's we cache in self.actor_name_map
            raw_name = ""
            actor_address = int.from_bytes(level_actors_raw[(x*8):(x*8+8)], byteorder='little', signed=False)
            actor_id = self.rm.read_int(
                actor_address + OFFSETS.get('Actor.actorId')
            )

            # We save a mapping of actor id to actor name for the sake of
            # saving memory calls
            if actor_id not in self.actor_name_map and actor_id != 0:
                try:
                    raw_name = self.rm.read_gname(actor_id)
                    self.actor_name_map[actor_id] = raw_name
                except Exception as e:
                    logger.error(f"Unable to find actor name: {e}")
            elif actor_id in self.actor_name_map:
                raw_name = self.actor_name_map.get(actor_id)

            # Ignore anything we cannot find a name for
            if not raw_name:
                continue
            
            
            # --------------- PARSE ENABLED OPTIONS ---------------#
            
            # Debug visual GUI for display all actors within 500m
            if CONFIG.get('DEBUG_ENABLED'):
                if "BP_" in raw_name:
                    # debug = Debug(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                    # if debug.distance < 500:
                    #     self.display_objects.append(debug)
                    print(raw_name)
                    continue

            # If we have Ship ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ship_keys object, interpret the actor
            # as a ship
            if CONFIG.get('SHIPS_ENABLED') and raw_name in ship_keys:
                ship = Ship(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(ship)

            # If we have the crews data enabled in helpers.py and the name
            # of the actor is CrewService, we create a class based on that Crew
            # data to generate information about people on the server
            # NOTE: This will NOT give us information on nearby players for the
            # sake of ESP
            if CONFIG.get('CREWS_ENABLED') and raw_name == "CrewService":
                self.crew_data = Crews(self.rm, actor_id, actor_address)
                
            # If we have gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py gem_keys object, interpret the actor
            # as a gem
            if CONFIG.get('GEMS_ENABLED') and raw_name in gem_keys:
                gem = Gem(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if gem.distance < 500:
                    self.display_objects.append(gem)
                    
            # If we have gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py shipwreck_keys object, interpret the actor
            # as a shipwreck
            if CONFIG.get('SHIPWRECKS_ENABLED') and raw_name in shipwreck_keys:
                shipwreck = Shipwreck(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(shipwreck)
                
            # If we have gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py skull_keys object, interpret the actor
            # as a skull
            if CONFIG.get('SKULLS_ENABLED') and raw_name in skull_keys:
                skull = Skull(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if skull.distance < 500:
                    self.display_objects.append(skull)

            # If we have gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py resource_keys object, interpret the actor
            # as a resource
            if CONFIG.get('RESOURCES_ENABLED') and raw_name in resource_keys:
                resource = Resource(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if resource.distance < 500:
                    self.display_objects.append(resource)

            # If we have gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ai_common_drops_keys object, interpret the actor
            # as a drop
            if CONFIG.get('AIDROPS_ENABLED') and raw_name in ai_common_drops_keys:
                ai_drop = AICommonDrop(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if ai_drop.distance < 500:
                    self.display_objects.append(ai_drop)
            
            # If we have gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py island_keys object, interpret the actor
            # as an island
            # if CONFIG.get('ISLANDS_ENABLED') and raw_name in island_keys:
            #     # island = Island(self.rm, actor_id, actor_address, self.my_coords, raw_name)
            #     # self.display_objects.append(island)
            #     continue
                
            # If we have gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py outpost_keys object, interpret the actor
            # as an outpost
            # if CONFIG.get('OUTPOSTS_ENABLED') and raw_name in outpost_keys:
            #     # outpost = Outpost(self.rm, actor_id, actor_address, self.my_coords, raw_name)
            #     # self.display_objects.append(outpost)
            #     continue
