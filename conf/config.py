import configparser
from os.path import exists, join


class Config:

    def __init__(self, conf_dir):
        self.CONF_DIR = conf_dir
        self.parser = configparser.ConfigParser()
        self.config = self.set_config()

    def build_config(self):
        # check if a config file exist
        # if not, create one
        # otherwise, load settings
        # create base config file

        self.parser["AI_ESP"] = {
            "AIDROPS_ENABLED": True,  # Y
            "ASHEN_LORD_ENABLED": False,  # Y
            "LANDAI_ENABLED": True,  # Y
            "OCEANAI_ENABLED": True,  # Y
            "STATUES_ENABLED": True,  # Y
        }
        self.parser["LOOT_ESP"] = {
            "ANIMAL_CONTAINER_ENABLED": False,  # Y
            "ASHEN_KEY_ENABLED": True,  # Y
            "EMISSARY_FLAGS_ENABLED": True,  # Y
            "EVENT_KEYS_ENABLED": True,  # Y
            "GEMS_ENABLED": True,  # Y
            "GENERAL_KEYS_ENABLED": True,  # Y
            "GH_CHESTS_ENABLED": True,  # Y
            "GH_RELICS_ENABLED": True,  # Y
            "GIFTS_ENABLED": True,  # Y
            "GUNPOWDER_ENABLED": True,  # Y
            "MEDALLIONS_ENABLED": True,  # Y
            "MERCHANT_LOOT_ENABLED": True,  # Y
            "RARE_LOOT_ENABLED": True,  # Y
            "REAPER_LOOT_ENABLED": True,  # Y
            "RESOURCES_ENABLED": True,  # Y
            "SEA_FORT_POUCH_ENABLED": True,  # Y
            "SKULLS_ENABLED": True,  # Y
            "TOMES_ENABLED": True,  # Y
            "TRIDENTS_ENABLED": False,  # Y
        }
        self.parser["MAP_ESP"] = {
            "EVENTS_ENABLED": False,  # Y
            "ISLANDS_ENABLED": False,  # N
            "LOOT_MERMAIDS_ENABLED": False,  # Y
            "MEGS_ENABLED": False,  # Y
            "OUTPOSTS_ENABLED": False,  # N
            "STORM_ENABLED": False,  # Y
        }
        self.parser["PLAYERS_ESP"] = {
            "CREWS_ENABLED": True,  # Y
            "MERMAIDS_ENABLED": True,  # Y
        }
        self.parser["SHIPS_ESP"] = {
            "ROWBOATS_ENABLED": True,  # Y
            "SHIPS_ENABLED": True,  # Y
            "SHIPWRECKS_ENABLED": True,  # Y
        }
        self.parser["UI_ESP"] = {
            "OXYGEN_ENABLED": True,  # Y
            "COMPASS_ENABLED": True,  # Y
        }
        self.parser["OTHER"] = {
            "DEBUG_ENABLED": False  # ~
        }

        with open(join(self.CONF_DIR, 'config.ini'), 'w') as configfile:
            self.parser.write(configfile)

    def set_config(self):
        if not exists(join(self.CONF_DIR, 'config.ini')):
            self.build_config()

        self.parser.read(join(self.CONF_DIR, 'config.ini'))

        # True=Enabled & False=Disabled for each relevant config items
        # Below denotes mappings exist but not necessarily the module
        # Y = implemented
        # N = to do
        # ~ = working but incomplete/unsatisfactory
        config_options = {

            # AI
            "AIDROPS_ENABLED": self.parser.getboolean("AI_ESP", "AIDROPS_ENABLED"),  # Y
            "ASHEN_LORD_ENABLED": self.parser.getboolean("AI_ESP", "ASHEN_LORD_ENABLED"),  # Y
            "LANDAI_ENABLED": self.parser.getboolean("AI_ESP", "LANDAI_ENABLED"),  # Y
            "OCEANAI_ENABLED": self.parser.getboolean("AI_ESP", "OCEANAI_ENABLED"),  # Y
            "STATUES_ENABLED": self.parser.getboolean("AI_ESP", "STATUES_ENABLED"),  # Y

            # Loot
            "ANIMAL_CONTAINER_ENABLED": self.parser.getboolean("LOOT_ESP", "ANIMAL_CONTAINER_ENABLED"),  # Y
            "ASHEN_KEY_ENABLED": self.parser.getboolean("LOOT_ESP", "ASHEN_KEY_ENABLED"),  # Y
            "EMISSARY_FLAGS_ENABLED": self.parser.getboolean("LOOT_ESP", "EMISSARY_FLAGS_ENABLED"),  # Y
            "EVENT_KEYS_ENABLED": self.parser.getboolean("LOOT_ESP", "EVENT_KEYS_ENABLED"),  # Y
            "GEMS_ENABLED": self.parser.getboolean("LOOT_ESP", "GEMS_ENABLED"),  # Y
            "GENERAL_KEYS_ENABLED": self.parser.getboolean("LOOT_ESP", "GENERAL_KEYS_ENABLED"),  # Y
            "GH_CHESTS_ENABLED": self.parser.getboolean("LOOT_ESP", "GH_CHESTS_ENABLED"),  # Y
            "GH_RELICS_ENABLED": self.parser.getboolean("LOOT_ESP", "GH_RELICS_ENABLED"),  # Y
            "GIFTS_ENABLED": self.parser.getboolean("LOOT_ESP", "GIFTS_ENABLED"),  # Y
            "GUNPOWDER_ENABLED": self.parser.getboolean("LOOT_ESP", "GUNPOWDER_ENABLED"),  # Y
            "MEDALLIONS_ENABLED": self.parser.getboolean("LOOT_ESP", "MEDALLIONS_ENABLED"),  # Y
            "MERCHANT_LOOT_ENABLED": self.parser.getboolean("LOOT_ESP", "MERCHANT_LOOT_ENABLED"),  # Y
            "RARE_LOOT_ENABLED": self.parser.getboolean("LOOT_ESP", "RARE_LOOT_ENABLED"),  # Y
            "REAPER_LOOT_ENABLED": self.parser.getboolean("LOOT_ESP", "REAPER_LOOT_ENABLED"),  # Y
            "RESOURCES_ENABLED": self.parser.getboolean("LOOT_ESP", "RESOURCES_ENABLED"),  # Y
            "SEA_FORT_POUCH_ENABLED": self.parser.getboolean("LOOT_ESP", "SEA_FORT_POUCH_ENABLED"),  # Y
            "SKULLS_ENABLED": self.parser.getboolean("LOOT_ESP", "SKULLS_ENABLED"),  # Y
            "TOMES_ENABLED": self.parser.getboolean("LOOT_ESP", "TOMES_ENABLED"),  # Y
            "TRIDENTS_ENABLED": self.parser.getboolean("LOOT_ESP", "TRIDENTS_ENABLED"),  # Y

            # Map
            "EVENTS_ENABLED": self.parser.getboolean("MAP_ESP", "EVENTS_ENABLED"),  # Y
            "ISLANDS_ENABLED": self.parser.getboolean("MAP_ESP", "ISLANDS_ENABLED"),  # N
            "LOOT_MERMAIDS_ENABLED": self.parser.getboolean("MAP_ESP", "LOOT_MERMAIDS_ENABLED"),  # Y
            "MEGS_ENABLED": self.parser.getboolean("MAP_ESP", "MEGS_ENABLED"),  # Y
            "OUTPOSTS_ENABLED": self.parser.getboolean("MAP_ESP", "OUTPOSTS_ENABLED"),  # N
            "STORM_ENABLED": self.parser.getboolean("MAP_ESP", "STORM_ENABLED"),  # Y

            # Players
            "CREWS_ENABLED": self.parser.getboolean("PLAYERS_ESP", "CREWS_ENABLED"),  # Y
            "MERMAIDS_ENABLED": self.parser.getboolean("PLAYERS_ESP", "MERMAIDS_ENABLED"),  # Y

            # Ships
            "ROWBOATS_ENABLED": self.parser.getboolean("SHIPS_ESP", "ROWBOATS_ENABLED"),  # Y
            "SHIPS_ENABLED": self.parser.getboolean("SHIPS_ESP", "SHIPS_ENABLED"),  # Y
            "SHIPWRECKS_ENABLED": self.parser.getboolean("SHIPS_ESP", "SHIPWRECKS_ENABLED"),  # Y

            # UI
            "OXYGEN_ENABLED": self.parser.getboolean("UI_ESP", "OXYGEN_ENABLED"),  # Y
            "COMPASS_ENABLED": self.parser.getboolean("UI_ESP", "COMPASS_ENABLED"),  # Y

            # Other
            "DEBUG_ENABLED": self.parser.getboolean("OTHER", "DEBUG_ENABLED")  # ~
        }

        return config_options

    def update_config(self):
        pass  # TODO: Add the ability to save changed settings. Will most likely require UI

    def save_loadout(self):
        pass  # TODO: Add ability to choose load-out set of settings
