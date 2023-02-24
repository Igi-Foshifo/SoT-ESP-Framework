"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
For community support, please contact me on Discord: DougTheDruid#2784
"""

import struct
import logging
from pyglet.text import Label
from utils.memory_helper import ReadMemory
from utils.helpers import OFFSETS, CONFIG, logger
from data.mapping \
    import \
    \
    ai_common_drops_keys, \
    ashlord_keys, \
    landai_keys, \
    oceanai_keys, \
    statue_keys, \
    \
    animalcontain_keys, \
    ashenkey_keys, \
    emflags_keys, \
    eventkeys_keys, \
    gem_keys, \
    genkey_keys, \
    ghchests_keys, \
    ghrelics_keys, \
    gifts_keys, \
    gunpowder_keys, \
    medallions_keys, \
    merchantcrates_keys, \
    rareloot_keys, \
    reaploot_keys, \
    resource_keys, \
    sfgold_keys, \
    skull_keys, \
    tomes_keys, \
    trident_keys, \
    \
    event_keys, \
    island_keys, \
    lootmermaid_keys, \
    meg_keys, \
    outpost_keys, \
    storm_keys, \
    \
    mermaid_keys, \
    \
    rowboat_keys, \
    ship_keys, \
    shipwreck_keys

# AI
from Modules.AI.ai_common_drop import AICommonDrop
from Modules.AI.ashen_lord import AshenLord
from Modules.AI.landai import LandAI
from Modules.AI.oceanai import OceanAI
from Modules.AI.statue import Statue

# Loot
from Modules.Loot.animal_container import AnimalContainer
from Modules.Loot.ashen_key import AshenKey
from Modules.Loot.emissary_flag import EmissaryFlag
from Modules.Loot.event_key import EventKey
from Modules.Loot.gem import Gem
from Modules.Loot.general_key import GeneralKey
from Modules.Loot.gh_chests import GHChest
from Modules.Loot.gh_relics import GHRelic
from Modules.Loot.gifts import Gift
from Modules.Loot.gunpowder import Gunpowder
from Modules.Loot.medallion import Medallion
from Modules.Loot.merchant_loot import MerchLoot
from Modules.Loot.rare_loot import RareLoot
from Modules.Loot.reaper_loot import ReaperLoot
from Modules.Loot.resource import Resource
from Modules.Loot.seafort_gold import SeaFortGold
from Modules.Loot.skull import Skull
from Modules.Loot.tome import Tome
from Modules.Loot.trident import Trident

# Map
from Modules.Map.compass import Compass
from Modules.Map.event import Event
from Modules.Map.island import Island
from Modules.Map.loot_mermaid import LootMermaid
from Modules.Map.megs import Meg
from Modules.Map.outpost import Outpost
from Modules.Map.storm import Storm

# Players
from Modules.Players.crews import Crews
from Modules.Players.mermaid import Mermaid

# Ships
from Modules.Ships.rowboat import Rowboat
from Modules.Ships.ship import Ship
from Modules.Ships.shipwreck import Shipwreck


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
            OFFSETS.get('PlayerCameraManager.CameraCache') + OFFSETS.get('CameraCacheEntry.MinimalViewInfo'),
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
            
            
            # ----------------------------------- PARSE ENABLED OPTIONS -------------------------------------#

            # --------------------------------- AI ------------------------------------#

            # If we have Enemy AI Drops ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ai_common_drops_keys object, interpret the actor
            # as a drop
            if CONFIG.get('AIDROPS_ENABLED') and raw_name in ai_common_drops_keys:
                ai_drop = AICommonDrop(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if ai_drop.distance < 500:
                    self.display_objects.append(ai_drop)

            # If we have Ashen Lord ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ashenlord_keys object, interpret the actor
            # as a drop
            if CONFIG.get('ASHEN_LORD_ENABLED') and raw_name in ashlord_keys:
                ashen_lord = AshenLord(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if ashen_lord.distance < 500:
                    self.display_objects.append(ashen_lord)

            # If we have Land Enemy ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py landai_keys object, interpret the actor
            # as a drop
            if CONFIG.get('LANDAI_ENABLED') and raw_name in landai_keys:
                landai = LandAI(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if landai.distance < 1000:
                    self.display_objects.append(landai)

            # If we have Ocean Enemy ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py oceanai_keys object, interpret the actor
            # as a drop
            if CONFIG.get('OCEANAI_ENABLED') and raw_name in oceanai_keys:
                oceanai = OceanAI(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if oceanai.distance < 1000:
                    self.display_objects.append(oceanai)

            # If we have Statue ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py statue_keys object, interpret the actor
            # as a drop
            if CONFIG.get('STATUES_ENABLED') and raw_name in statue_keys:
                statue = Statue(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if statue.distance < 500:
                    self.display_objects.append(statue)

            # --------------------------------- Loot ------------------------------------#

            # If we have Animal Container ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py animalcontain_keys object, interpret the actor
            # as an animal container
            if CONFIG.get('ANIMAL_CONTAINER_ENABLED') and raw_name in animalcontain_keys:
                animal_container = AnimalContainer(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if animal_container.distance < 500:
                    self.display_objects.append(animal_container)

            # If we have Ashen Key ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ashenkey_keys object, interpret the actor
            # as an ashen key
            if CONFIG.get('ASHEN_KEY_ENABLED') and raw_name in ashenkey_keys:
                ashen_key = AshenKey(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if ashen_key.distance < 500:
                    self.display_objects.append(ashen_key)

            # If we have Emissary Flag ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py emflags_keys object, interpret the actor
            # as an emissary flag
            if CONFIG.get('EMISSARY_FLAGS_ENABLED') and raw_name in emflags_keys:
                emissary_flag = EmissaryFlag(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if emissary_flag.distance < 4000:
                    self.display_objects.append(emissary_flag)

            # If we have Event Keys ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py eventkeys_keys object, interpret the actor
            # as an Event Key
            if CONFIG.get('EVENT_KEYS_ENABLED') and raw_name in eventkeys_keys:
                event_key = EventKey(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if event_key.distance < 500:
                    self.display_objects.append(event_key)

            # If we have Gem ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py gem_keys object, interpret the actor
            # as a gem
            if CONFIG.get('GEMS_ENABLED') and raw_name in gem_keys:
                gem = Gem(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if gem.distance < 500:
                    self.display_objects.append(gem)

            # If we have General Key ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py genkey_keys object, interpret the actor
            # as a general key
            if CONFIG.get('GENERAL_KEYS_ENABLED') and raw_name in genkey_keys:
                general_key = GeneralKey(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if general_key.distance < 500:
                    self.display_objects.append(general_key)

            # If we have Gold Hoarder Chests ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ghchests_keys object, interpret the actor
            # as a gold hoarder chest
            if CONFIG.get('GH_CHESTS_ENABLED') and raw_name in ghchests_keys:
                gh_chest = GHChest(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if gh_chest.distance < 500:
                    self.display_objects.append(gh_chest)

            # If we have Gold Hunter Relic ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ghrelics_keys object, interpret the actor
            # as a gold hunter relic
            if CONFIG.get('GH_RELICS_ENABLED') and raw_name in ghrelics_keys:
                gh_relic = GHRelic(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if gh_relic.distance < 500:
                    self.display_objects.append(gh_relic)

            # If we have Gift ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py gifts_keys object, interpret the actor
            # as a gift
            if CONFIG.get('GIFTS_ENABLED') and raw_name in gifts_keys:
                gift = Gift(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if gift.distance < 500:
                    self.display_objects.append(gift)

            # If we have Gunpowder ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py gunpowder_keys object, interpret the actor
            # as a gunpowder
            if CONFIG.get('GUNPOWDER_ENABLED') and raw_name in gunpowder_keys:
                gunpowder = Gunpowder(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if gunpowder.distance < 1000:
                    self.display_objects.append(gunpowder)

            # If we have Medallion ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py medallions_keys object, interpret the actor
            # as a medallion
            if CONFIG.get('MEDALLIONS_ENABLED') and raw_name in medallions_keys:
                medallion = Medallion(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if medallion.distance < 500:
                    self.display_objects.append(medallion)

            # If we have Merchant Loot ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py merchantcrates_keys object, interpret the actor
            # as a merchant loot item
            if CONFIG.get('MERCHANT_LOOT_ENABLED') and raw_name in merchantcrates_keys:
                merchant_loot = MerchLoot(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if merchant_loot.distance < 500:
                    self.display_objects.append(merchant_loot)

            # If we have Rare Loot ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py rareloot_keys object, interpret the actor
            # as a rare loot item
            if CONFIG.get('RARE_LOOT_ENABLED') and raw_name in rareloot_keys:
                rare_loot = RareLoot(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if rare_loot.distance < 500:
                    self.display_objects.append(rare_loot)

            # If we have Reaper Loot ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py reaploot_keys object, interpret the actor
            # as a reaper loot item
            if CONFIG.get('REAPER_LOOT_ENABLED') and raw_name in reaploot_keys:
                reaper_loot = ReaperLoot(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if reaper_loot.distance < 500:
                    self.display_objects.append(reaper_loot)

            # If we have Resource ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py resource_keys object, interpret the actor
            # as a resource
            if CONFIG.get('RESOURCES_ENABLED') and raw_name in resource_keys:
                resource = Resource(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if resource.distance < 500:
                    self.display_objects.append(resource)

            # If we have Sea Fort Gold Pouch ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py sfgold_keys object, interpret the actor
            # as a sea fort gold pouch
            if CONFIG.get('SEA_FORT_POUCH_ENABLED') and raw_name in sfgold_keys:
                sfgold = SeaFortGold(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if sfgold.distance < 100:
                    self.display_objects.append(sfgold)

            # If we have Skull ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py skull_keys object, interpret the actor
            # as a skull
            if CONFIG.get('SKULLS_ENABLED') and raw_name in skull_keys:
                skull = Skull(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if skull.distance < 500:
                    self.display_objects.append(skull)

            # If we have Tome ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py tomes_keys object, interpret the actor
            # as a tome
            if CONFIG.get('TOMES_ENABLED') and raw_name in tomes_keys:
                tome = Tome(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if tome.distance < 500:
                    self.display_objects.append(tome)

            # If we have Trident ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py trident_keys object, interpret the actor
            # as a trident
            if CONFIG.get('TRIDENTS_ENABLED') and raw_name in trident_keys:
                trident = Trident(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if trident.distance < 500:
                    self.display_objects.append(trident)

            # --------------------------------- Map ------------------------------------#

            # If we have Event ESP enabled in helpers.py and a camera y coordinate value,
            # display the compass
            if CONFIG.get('COMPASS_ENABLED') and self.my_coords['cam_y']:
                compass = Compass(self.rm, actor_address, self.my_coords)
                self.display_objects.append(compass)

            # If we have Event ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py event_keys object, interpret the actor
            # as an event
            if CONFIG.get('EVENTS_ENABLED') and raw_name in event_keys:
                event = Event(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(event)

            # If we have Island ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py island_keys object, interpret the actor
            # as an island
            if CONFIG.get('ISLANDS_ENABLED') and raw_name in island_keys:
                island = Island(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(island)

            # If we have Loot Mermaid ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py lootmermaid_keys object, interpret the actor
            # as a loot mermaid
            if CONFIG.get('LOOT_MERMAIDS_ENABLED') and raw_name in lootmermaid_keys:
                lootmermaid = LootMermaid(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if lootmermaid.distance < 800:
                    self.display_objects.append(lootmermaid)

            # If we have Megalodon ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py meg_keys object, interpret the actor
            # as a meg
            if CONFIG.get('MEGS_ENABLED') and raw_name in meg_keys:
                meg = Meg(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if meg.distance < 1000:
                    self.display_objects.append(meg)

            # If we have Outpost ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py outpost_keys object, interpret the actor
            # as an outpost
            if CONFIG.get('OUTPOSTS_ENABLED') and raw_name in outpost_keys:
                outpost = Outpost(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(outpost)

            # If we have Storm ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py statue_keys object, interpret the actor
            # as a storm
            if CONFIG.get('STORM_ENABLED') and raw_name in storm_keys:
                storm = Storm(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(storm)

            # --------------------------------- Players ------------------------------------#

            # If we have the crews data enabled in helpers.py and the name
            # of the actor is CrewService, we create a class based on that Crew
            # data to generate information about people on the server
            if CONFIG.get('CREWS_ENABLED') and raw_name == "CrewService":
                self.crew_data = Crews(self.rm, actor_id, actor_address)

            # If we have mermaid ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py mermaid_keys object, interpret the actor
            # as a mermaid
            if CONFIG.get('MERMAIDS_ENABLED') and raw_name in mermaid_keys:
                mermaid = Mermaid(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if mermaid.distance < 800:
                    self.display_objects.append(mermaid)

            # --------------------------------- Ships ------------------------------------#

            # If we have Rowboat ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py rowboat_keys object, interpret the actor
            # as a rowboat
            if CONFIG.get('ROWBOATS_ENABLED') and raw_name in rowboat_keys:
                rowboat = Rowboat(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if rowboat.distance < 500:
                    self.display_objects.append(rowboat)

            # If we have Ship ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py ship_keys object, interpret the actor
            # as a ship
            if CONFIG.get('SHIPS_ENABLED') and raw_name in ship_keys:
                ship = Ship(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                if "Template" not in ship.raw_name and ship.distance < 1740:
                    continue
                else:
                    self.display_objects.append(ship)

            # If we have Shipwreck ESP enabled in helpers.py, and the name of the
            # actor is in our mapping.py shipwreck_keys object, interpret the actor
            # as a shipwreck
            if CONFIG.get('SHIPWRECKS_ENABLED') and raw_name in shipwreck_keys:
                shipwreck = Shipwreck(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                self.display_objects.append(shipwreck)

            # --------------------------------- Other ------------------------------------#

            # Debug visual GUI for display all actors within 500m
            if CONFIG.get('DEBUG_ENABLED'):
                if "BP_" in raw_name:
                    # debug = Debug(self.rm, actor_id, actor_address, self.my_coords, raw_name)
                    # if debug.distance < 500:
                    #     self.display_objects.append(debug)
                    print(raw_name)
                    continue
