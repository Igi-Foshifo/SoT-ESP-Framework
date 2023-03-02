from utils.helpers import CONFIG
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
    crew_keys, \
    mermaid_keys, \
 \
    rowboat_keys, \
    ship_keys, \
    shipwreck_keys

# AI
from modules.AI.ai_common_drop import AICommonDrop
from modules.AI.ashen_lord import AshenLord
from modules.AI.landai import LandAI
from modules.AI.oceanai import OceanAI
from modules.AI.statue import Statue

# Loot
from modules.Loot.animal_container import AnimalContainer
from modules.Loot.ashen_key import AshenKey
from modules.Loot.emissary_flag import EmissaryFlag
from modules.Loot.event_key import EventKey
from modules.Loot.gem import Gem
from modules.Loot.general_key import GeneralKey
from modules.Loot.gh_chests import GHChest
from modules.Loot.gh_relics import GHRelic
from modules.Loot.gifts import Gift
from modules.Loot.gunpowder import Gunpowder
from modules.Loot.medallion import Medallion
from modules.Loot.merchant_loot import MerchLoot
from modules.Loot.rare_loot import RareLoot
from modules.Loot.reaper_loot import ReaperLoot
from modules.Loot.resource import Resource
from modules.Loot.seafort_gold import SeaFortGold
from modules.Loot.skull import Skull
from modules.Loot.tome import Tome
from modules.Loot.trident import Trident

# Map
from modules.Map.event import Event
from modules.Map.island import Island
from modules.Map.loot_mermaid import LootMermaid
from modules.Map.megs import Meg
from modules.Map.outpost import Outpost
from modules.Map.storm import Storm

# Players
from modules.Players.crews import Crews
from modules.Players.mermaid import Mermaid

# Ships
from modules.Ships.rowboat import Rowboat
from modules.Ships.ship import Ship
from modules.Ships.shipwreck import Shipwreck

# UI
from modules.UI.compass import Compass
from modules.UI.oxygen import Oxygen


class ModuleParser:
    """
    Class to handle the parsing of all modules within the module package
    """

    def __init__(self, u_local_player, player_controller, my_athena_player_character):
        """
        Initialize the ModuleParser class with the LocalPlayer, the PlayerController and
        the player's AthenaPlayerCharacter class
        """
        self.u_local_player = u_local_player
        self.player_controller = player_controller
        self.my_athena_player_character = my_athena_player_character

        self.compass_init = False
        self.oxygen_init = False

    def parse_static_modules(self, rm, my_coords):
        # region UI
        # If we have Compass ESP enabled in helpers.py, create the
        # compass static object and add to display array to update
        if not self.compass_init and CONFIG.get('COMPASS_ENABLED'):
            compass = Compass(rm, my_coords)
            self.compass_init = True
            return compass

        # If we have Oxygen ESP enabled in helpers.py, create the
        # compass static object and add to display array to update
        if not self.oxygen_init and CONFIG.get('OXYGEN_ENABLED'):
            oxygen = Oxygen(rm, self.my_athena_player_character)
            self.oxygen_init = True
            return oxygen
        # endregion

    def parse_dynamic_modules(self, rm, raw_name, actor_id, actor_address, my_coords):
        # region AI
        # If we have Enemy AI Drops ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py ai_common_drops_keys object, interpret the actor
        # as a drop
        if CONFIG.get('AIDROPS_ENABLED') and raw_name in ai_common_drops_keys:
            ai_drop = AICommonDrop(rm, actor_id, actor_address, my_coords, raw_name)
            if ai_drop.distance < 500:
                return ai_drop

        # If we have Ashen Lord ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py ashenlord_keys object, interpret the actor
        # as a drop
        if CONFIG.get('ASHEN_LORD_ENABLED') and raw_name in ashlord_keys:
            ashen_lord = AshenLord(rm, actor_id, actor_address, my_coords, raw_name)
            if ashen_lord.distance < 500:
                return ashen_lord

        # If we have Land Enemy ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py landai_keys object, interpret the actor
        # as a drop
        if CONFIG.get('LANDAI_ENABLED') and raw_name in landai_keys:
            landai = LandAI(rm, actor_id, actor_address, my_coords, raw_name)
            if landai.distance < 1000:
                return landai

        # If we have Ocean Enemy ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py oceanai_keys object, interpret the actor
        # as a drop
        if CONFIG.get('OCEANAI_ENABLED') and raw_name in oceanai_keys:
            oceanai = OceanAI(rm, actor_id, actor_address, my_coords, raw_name)
            if oceanai.distance < 1000:
                return oceanai

        # If we have Statue ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py statue_keys object, interpret the actor
        # as a drop
        if CONFIG.get('STATUES_ENABLED') and raw_name in statue_keys:
            statue = Statue(rm, actor_id, actor_address, my_coords, raw_name)
            if statue.distance < 500:
                return statue
        # endregion

        # region Loot
        # If we have Animal Container ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py animalcontain_keys object, interpret the actor
        # as an animal container
        if CONFIG.get('ANIMAL_CONTAINER_ENABLED') and raw_name in animalcontain_keys:
            animal_container = AnimalContainer(rm, actor_id, actor_address, my_coords, raw_name)
            if animal_container.distance < 500:
                return animal_container

        # If we have Ashen Key ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py ashenkey_keys object, interpret the actor
        # as an ashen key
        if CONFIG.get('ASHEN_KEY_ENABLED') and raw_name in ashenkey_keys:
            ashen_key = AshenKey(rm, actor_id, actor_address, my_coords, raw_name)
            if ashen_key.distance < 500:
                return ashen_key

        # If we have Emissary Flag ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py emflags_keys object, interpret the actor
        # as an emissary flag
        if CONFIG.get('EMISSARY_FLAGS_ENABLED') and raw_name in emflags_keys:
            emissary_flag = EmissaryFlag(rm, actor_id, actor_address, my_coords, raw_name)
            if emissary_flag.distance < 4000:
                return emissary_flag

        # If we have Event Keys ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py eventkeys_keys object, interpret the actor
        # as an Event Key
        if CONFIG.get('EVENT_KEYS_ENABLED') and raw_name in eventkeys_keys:
            event_key = EventKey(rm, actor_id, actor_address, my_coords, raw_name)
            if event_key.distance < 500:
                return event_key

        # If we have Gem ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py gem_keys object, interpret the actor
        # as a gem
        if CONFIG.get('GEMS_ENABLED') and raw_name in gem_keys:
            gem = Gem(rm, actor_id, actor_address, my_coords, raw_name)
            if gem.distance < 500:
                return gem

        # If we have General Key ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py genkey_keys object, interpret the actor
        # as a general key
        if CONFIG.get('GENERAL_KEYS_ENABLED') and raw_name in genkey_keys:
            general_key = GeneralKey(rm, actor_id, actor_address, my_coords, raw_name)
            if general_key.distance < 500:
                return general_key

        # If we have Gold Hoarder Chests ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py ghchests_keys object, interpret the actor
        # as a gold hoarder chest
        if CONFIG.get('GH_CHESTS_ENABLED') and raw_name in ghchests_keys:
            gh_chest = GHChest(rm, actor_id, actor_address, my_coords, raw_name)
            if gh_chest.distance < 500:
                return gh_chest

        # If we have Gold Hunter Relic ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py ghrelics_keys object, interpret the actor
        # as a gold hunter relic
        if CONFIG.get('GH_RELICS_ENABLED') and raw_name in ghrelics_keys:
            gh_relic = GHRelic(rm, actor_id, actor_address, my_coords, raw_name)
            if gh_relic.distance < 500:
                return gh_relic

        # If we have Gift ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py gifts_keys object, interpret the actor
        # as a gift
        if CONFIG.get('GIFTS_ENABLED') and raw_name in gifts_keys:
            gift = Gift(rm, actor_id, actor_address, my_coords, raw_name)
            if gift.distance < 500:
                return gift

        # If we have Gunpowder ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py gunpowder_keys object, interpret the actor
        # as a gunpowder
        if CONFIG.get('GUNPOWDER_ENABLED') and raw_name in gunpowder_keys:
            gunpowder = Gunpowder(rm, actor_id, actor_address, my_coords, raw_name)
            if gunpowder.distance < 1000:
                return gunpowder

        # If we have Medallion ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py medallions_keys object, interpret the actor
        # as a medallion
        if CONFIG.get('MEDALLIONS_ENABLED') and raw_name in medallions_keys:
            medallion = Medallion(rm, actor_id, actor_address, my_coords, raw_name)
            if medallion.distance < 500:
                return medallion

        # If we have Merchant Loot ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py merchantcrates_keys object, interpret the actor
        # as a merchant loot item
        if CONFIG.get('MERCHANT_LOOT_ENABLED') and raw_name in merchantcrates_keys:
            merchant_loot = MerchLoot(rm, actor_id, actor_address, my_coords, raw_name)
            if merchant_loot.distance < 500:
                return merchant_loot

        # If we have Rare Loot ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py rareloot_keys object, interpret the actor
        # as a rare loot item
        if CONFIG.get('RARE_LOOT_ENABLED') and raw_name in rareloot_keys:
            rare_loot = RareLoot(rm, actor_id, actor_address, my_coords, raw_name)
            if rare_loot.distance < 500:
                return rare_loot

        # If we have Reaper Loot ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py reaploot_keys object, interpret the actor
        # as a reaper loot item
        if CONFIG.get('REAPER_LOOT_ENABLED') and raw_name in reaploot_keys:
            reaper_loot = ReaperLoot(rm, actor_id, actor_address, my_coords, raw_name)
            if reaper_loot.distance < 500:
                return reaper_loot

        # If we have Resource ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py resource_keys object, interpret the actor
        # as a resource
        if CONFIG.get('RESOURCES_ENABLED') and raw_name in resource_keys:
            resource = Resource(rm, actor_id, actor_address, my_coords, raw_name)
            if resource.distance < 500:
                return resource

        # If we have Sea Fort Gold Pouch ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py sfgold_keys object, interpret the actor
        # as a sea fort gold pouch
        if CONFIG.get('SEA_FORT_POUCH_ENABLED') and raw_name in sfgold_keys:
            sfgold = SeaFortGold(rm, actor_id, actor_address, my_coords, raw_name)
            if sfgold.distance < 100:
                return sfgold

        # If we have Skull ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py skull_keys object, interpret the actor
        # as a skull
        if CONFIG.get('SKULLS_ENABLED') and raw_name in skull_keys:
            skull = Skull(rm, actor_id, actor_address, my_coords, raw_name)
            if skull.distance < 500:
                return skull

        # If we have Tome ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py tomes_keys object, interpret the actor
        # as a tome
        if CONFIG.get('TOMES_ENABLED') and raw_name in tomes_keys:
            tome = Tome(rm, actor_id, actor_address, my_coords, raw_name)
            if tome.distance < 500:
                return tome

        # If we have Trident ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py trident_keys object, interpret the actor
        # as a trident
        if CONFIG.get('TRIDENTS_ENABLED') and raw_name in trident_keys:
            trident = Trident(rm, actor_id, actor_address, my_coords, raw_name)
            if trident.distance < 500:
                return trident
        # endregion

        # region Map
        # If we have Event ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py event_keys object, interpret the actor
        # as an event
        if CONFIG.get('EVENTS_ENABLED') and raw_name in event_keys:
            event = Event(rm, actor_id, actor_address, my_coords, raw_name)
            return event

        # If we have Island ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py island_keys object, interpret the actor
        # as an island
        if CONFIG.get('ISLANDS_ENABLED') and raw_name in island_keys:
            island = Island(rm, actor_id, actor_address, my_coords, raw_name)
            return island

        # If we have Loot Mermaid ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py lootmermaid_keys object, interpret the actor
        # as a loot mermaid
        if CONFIG.get('LOOT_MERMAIDS_ENABLED') and raw_name in lootmermaid_keys:
            lootmermaid = LootMermaid(rm, actor_id, actor_address, my_coords, raw_name)
            if lootmermaid.distance < 800:
                return lootmermaid

        # If we have Megalodon ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py meg_keys object, interpret the actor
        # as a meg
        if CONFIG.get('MEGS_ENABLED') and raw_name in meg_keys:
            meg = Meg(rm, actor_id, actor_address, my_coords, raw_name)
            if meg.distance < 1000:
                return meg

        # If we have Outpost ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py outpost_keys object, interpret the actor
        # as an outpost
        if CONFIG.get('OUTPOSTS_ENABLED') and raw_name in outpost_keys:
            outpost = Outpost(rm, actor_id, actor_address, my_coords, raw_name)
            return outpost

        # If we have Storm ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py statue_keys object, interpret the actor
        # as a storm
        if CONFIG.get('STORM_ENABLED') and raw_name in storm_keys:
            storm = Storm(rm, actor_id, actor_address, my_coords, raw_name)
            return storm
        # endregion

        # region Players
        # If we have the crews data enabled in helpers.py and the name
        # of the actor is CrewService, we create a class based on that Crew
        # data to generate information about people on the server
        if CONFIG.get('CREWS_ENABLED') and raw_name in crew_keys:
            crew = Crews(rm, actor_id, actor_address)
            return crew

        # If we have mermaid ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py mermaid_keys object, interpret the actor
        # as a mermaid
        if CONFIG.get('MERMAIDS_ENABLED') and raw_name in mermaid_keys:
            mermaid = Mermaid(rm, actor_id, actor_address, my_coords, raw_name)
            if mermaid.distance < 800:
                return mermaid
        # endregion

        # region Ships
        # If we have Rowboat ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py rowboat_keys object, interpret the actor
        # as a rowboat
        if CONFIG.get('ROWBOATS_ENABLED') and raw_name in rowboat_keys:
            rowboat = Rowboat(rm, actor_id, actor_address, my_coords, raw_name)
            if rowboat.distance < 500:
                return rowboat

        # If we have Ship ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py ship_keys object, interpret the actor
        # as a ship
        if CONFIG.get('SHIPS_ENABLED') and raw_name in ship_keys:
            ship = Ship(rm, actor_id, actor_address, my_coords, raw_name)
            if "Template" not in ship.raw_name and ship.distance < 1720:
                pass
            else:
                return ship

        # If we have Shipwreck ESP enabled in helpers.py, and the name of the
        # actor is in our mapping.py shipwreck_keys object, interpret the actor
        # as a shipwreck
        if CONFIG.get('SHIPWRECKS_ENABLED') and raw_name in shipwreck_keys:
            shipwreck = Shipwreck(rm, actor_id, actor_address, my_coords, raw_name)
            return shipwreck
        # endregion

        # region UI
        # endregion

        # region Other
        # Debug visual GUI for display all actors within 500m
        if CONFIG.get('DEBUG_ENABLED'):
            if "BP_" in raw_name:
                print(raw_name)
                pass  # TODO: dump this into a log file rather than print
        # endregion
