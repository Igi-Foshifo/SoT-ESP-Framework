# store all dicts into a single dict
mapping_raw_name_comp = {}

# ---------------------------------------------------- Ships ---------------------------------------------------- #
crews = {
    "CrewService": {
        "Name": "CrewService",
    },
}

crew_keys = set(crews.keys())
mapping_raw_name_comp.update(crews)

# ---------------------------------------------------- Ships ---------------------------------------------------- #
ships = {
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "Sloop",
    },

    "BP_MediumShipTemplate_C": {
        "Name": "Brig",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "Brig",
    },

    "BP_LargeShipTemplate_C": {
        "Name": "Galleon",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "Galleon",
    },
    "BP_AISmallShipTemplate_C": {
        "Name": "Skeleton Sloop",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "Skeleton Sloop",
    },
    "BP_AILargeShipTemplate_C": {
        "Name": "Skeleton Galleon",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "Skeleton Galleon",
    },
}

ship_keys = set(ships.keys())
mapping_raw_name_comp.update(ships)

# ---------------------------------------------------- Gems ---------------------------------------------------- #
gems = {
    "BP_MermaidGem_ItemInfo_Ruby_C": {
        "Name": "Ruby Mermaid Gem",
    },
    "BP_SirenGem_ItemInfo_Ruby_C": {
        "Name": "Ruby Siren Gem",
    },
    "BP_SK_SirenEssence_Ruby_ItemInfo_C": {
        "Name": "Ruby Breath of the Sea",
    },
    "BP_MermaidGem_ItemInfo_Emerald_C": {
        "Name": "Emerald Mermaid Gem",
    },
    "BP_SirenGem_ItemInfo_Emerald_C": {
        "Name": "Emerald Siren Gem",
    },
    "BP_SK_SirenEssence_Emerald_ItemInfo_C": {
        "Name": "Emerald Breath of the Sea",
    },
    "BP_MermaidGem_ItemInfo_Sapphire_C": {
        "Name": "Sapphire Mermaid Gem",
    },
    "BP_SirenGem_ItemInfo_Sapphire_C": {
        "Name": "Sapphire Siren Gem",
    },
    "BP_SK_SirenEssence_Sapphire_ItemInfo_C": {
        "Name": "Sapphire Breath of the Sea",
    },
}

gem_keys = set(gems.keys())
mapping_raw_name_comp.update(gems)

# ---------------------------------------------------- Skulls ---------------------------------------------------- #
skulls = {
    "BP_AshenWindsSkull_ItemInfo_C": {
        "Name": "Ashen Winds Skull",
    },
    "BP_BountyRewardSkullItemInfo_Fort_C": {
        "Name": "Stronghold Skull",
    },
    "BP_BountyRewardSkullItemInfo_Ghost_Captain_C": {
        "Name": "Captain Skull of the Damned",
    },
    "BP_BountyRewardSkullItemInfo_Ghost_Common_C": {
        "Name": "Skull of the Damned",
    },
    "BP_BountyRewardSkullItemInfo_AIShip_C": {
        "Name": "Skeleton Captain's Skull",
    },
    "BP_BountyRewardSkullItemInfo_Mythical_DVR_C": {
        "Name": "Ashen Villainous Bounty Skull",
    },
    "BP_BountyRewardSkullItemInfo_Mythical_C": {
        "Name": "Villainous Bounty Skull",
    },
    "BP_SKLostCapSkullItemInfo_Mythical_C": {
        "Name": "Villainous Coral Skull",
    },
    "BP_BountyRewardSkullItemInfo_Legendary_DVR_C": {
        "Name": "Ashen Hateful Bounty Skull",
    },
    "BP_BountyRewardSkullItemInfo_Legendary_C": {
        "Name": "Hateful Bounty Skull",
    },
    "BP_SKLostCapSkullItemInfo_Legendary_C": {
        "Name": "Hateful Coral Skull",
    },
    "BP_BountyRewardSkullItemInfo_Rare_DVR_C": {
        "Name": "Ashen Disgraced Bounty Skull",
    },
    "BP_BountyRewardSkullItemInfo_Rare_C": {
        "Name": "Disgraced Bounty Skull",
    },
    "BP_SKLostCapSkullItemInfo_Rare_C": {
        "Name": "Disgraced Coral Skull",
    },
    "BP_BountyRewardSkullItemInfo_Common_DVR_C": {
        "Name": "Ashen Foul Bounty Skull",
    },
    "BP_BountyRewardSkullItemInfo_Common_C": {
        "Name": "Foul Bounty Skull",
    },
    "BP_SKLostCapSkullItemInfo_Common_C": {
        "Name": "Foul Coral Skull",
    },
    "BP_Ritual_Skull_ItemInfo_C": {
        "Name": "Ritual Skull",
    },
}

skull_keys = set(skulls.keys())
mapping_raw_name_comp.update(skulls)

# ---------------------------------------------------- Shipwrecks ---------------------------------------------------- #
shipwrecks = {
    "BP_Shipwreck_01_a_NetProxy_C": {
        "Name": "Shipwreck",
    },
    "BP_Seagull01_8POI_LostShipments_C": {
        "Name": "Shipwreck (Quest)",
    },
    "BP_MA_CabinDoorKey_ItemInfo_C": {
        "Name": "Captain's Key",
    },
    # "ShipWreckGraveyardKeyItemInfo_C": {
    #     "Name": "Shipwreck Graveyard Key",
    # },
}

shipwreck_keys = set(shipwrecks.keys())
mapping_raw_name_comp.update(shipwrecks)

# ---------------------------------------------------- Statues ---------------------------------------------------- #
statues = {
    "BP_SunkenCurseArtefact_Ruby_C": {
        "Name": "Ruby Mermaid Statue",
    },
    "BP_SunkenCurseArtefact_Emerald_C": {
        "Name": "Emerald Mermaid Statue",
    },
    "BP_SunkenCurseArtefact_Sapphire_C": {
        "Name": "Sapphire Mermaid Statue",
    },
}

statue_keys = set(statues.keys())
mapping_raw_name_comp.update(statues)

# ---------------------------------------------------- Events ---------------------------------------------------- #
events = {
    "BP_SkellyFort_RitualSkullCloud_C": {
        "Name": "Fort of the Damned Event",
    },
    "BP_LegendSkellyFort_SkullCloud_C": {
        "Name": "Fort of Fortune Event",
    },
    "BP_GhostShips_Signal_Flameheart_NetProxy_C": {
        "Name": "Ghost Fleet Event",
    },
    "BP_SkellyFort_SkullCloud_C": {
        "Name": "Skeleton Fort Event",
    },
    "BP_SkellyShip_ShipCloud_C": {
        "Name": "Skeleton Fleet Event",
    },
    "BP_AshenLord_SkullCloud_C": {
        "Name": "Ashen Lord Event",
    },
}

event_keys = set(events.keys())
mapping_raw_name_comp.update(events)

# -------------------------------------------------- Ocean Enemies -------------------------------------------------- #
oceanai = {
    "BP_Shark_C": {
        "Name": "Shark",
    },
    "BP_SirenGruntPawn_C": {
        "Name": "Siren",
    },
    "BP_SirenLeaderPawn_C": {
        "Name": "Siren Leader",
    },
}

oceanai_keys = set(oceanai.keys())
mapping_raw_name_comp.update(oceanai)

# -------------------------------------------------- Land Enemies -------------------------------------------------- #
landai = {
    "BP_SkeletonPawnBase_C": {
        "Name": "Skeleton",
    },
    "BP_PhantomPawnBase_C": {
        "Name": "Phantom",
    },
    "BP_OceanCrawlerCharacter_Hermit_C": {
        "Name": "Hermit",
    },
    "BP_OceanCrawlerCharacter_Eelectric_C": {
        "Name": "Eelectric",
    },
    "BP_OceanCrawlerCharacter_Crab_C": {
        "Name": "Crab",
    },
}

landai_keys = set(landai.keys())
mapping_raw_name_comp.update(landai)

# ---------------------------------------------------- Rowboats ---------------------------------------------------- #
rowboats = {
    "BP_Rowboat_WithFrontHarpoon_C": {
        "Name": "Harpoon Rowboat",
    },
    "BP_Rowboat_C": {
        "Name": "Rowboat",
    },
    "BP_SwampRowboat_C": {
        "Name": "Swamp Rowboat",
    },
}

rowboat_keys = set(rowboats.keys())
mapping_raw_name_comp.update(rowboats)

# ---------------------------------------------------- Storm ---------------------------------------------------- #
storm = {
    "BP_Storm_C": {
        "Name": "Eye of the Storm",
    },
}

storm_keys = set(storm.keys())
mapping_raw_name_comp.update(storm)

# ---------------------------------------------------- Resources ---------------------------------------------------- #
resources = {
    "BP_AshenChestCollectorsChest_ItemInfo_C": {
        "Name": "Ashen Collectors Chest",
    },
    "BP_AshenChestCollectorsChest_Unlocked_ItemInfo_C": {
        "Name": "Ashen Collectors Chest",
    },
    "BP_CollectorsChest_ItemInfo_C": {
        "Name": "Treasure Chest",
    },
    "BP_SK_CoralCollectorsChest_ItemInfo_C": {
        "Name": "Coral Treasure Chest",
    },
    "BP_LockedEquipmentChest_ItemInfo_C": {
        "Name": "Old Sailor's Chest",
    },
    "BP_UnLockedEquipmentChest_ItemInfo_C": {
        "Name": "Old Sailor's Chest",
    },
    "BP_MerchantCrate_AIShipAnyItemCrate_ItemInfo_C": {
        "Name": "Storage Crate",
    },
    "BP_MerchantCrate_AnyItemCrate_ItemInfo_C": {
        "Name": "Storage Crate",
    },
    "BP_MerchantCrate_GhostResourceCrate_ItemInfo_C": {
        "Name": "Storage Crate of the Damned",
    },
    "BP_MerchantCrate_GhostCannonballCrate_ItemInfo_C": {
        "Name": "Cannonball Crate of the Damned",
    },
    "BP_PortableAmmoCrate_ItemInfo_C": {
        "Name": "Ammo Chest",
    },
    "BP_MerchantCrate_FirebombCrate_ItemInfo_C": {
        "Name": "Firebomb Crate",
    },
    "BP_MerchantCrate_WoodCrate_FullyStocked_ItemInfo_C": {
        "Name": "Plank Crate",
    },
    "BP_MerchantCrate_WoodCrate_ItemInfo_C": {
        "Name": "Plank Crate",
    },
    "BP_MerchantCrate_CannonballCrate_FullyStocked_ItemInfo_C": {
        "Name": "Cannonball Crate",
    },
    "BP_MerchantCrate_CannonballCrate_ItemInfo_C": {
        "Name": "Cannonball Crate",
    },
    "BP_MerchantCrate_BananaCrate_FullyStocked_ItemInfo_C": {
        "Name": "Food Crate",
    },
    "BP_MerchantCrate_BananaCrate_ItemInfo_C": {
        "Name": "Food Crate",
    },
}

resource_keys = set(resources.keys())
mapping_raw_name_comp.update(resources)

# ---------------------------------------------------- AI Drops ---------------------------------------------------- #
ai_common_drops = {
    "BP_MessageInABottle_Clue_ItemInfo_C": {
        "Name": "Merchant Quest Bottle",
    },
    "BP_SkeletonOrdersRiddle_ItemInfo_C": {
        "Name": "Skeleton's Orders",
    },
    "BP_MessageInABottle_ItemInfo_C": {
        "Name": "Message in a Bottle",
    },
    "BP_MessageInABottle_Coral_ItemInfo_C": {
        "Name": "Coral Quest Bottle",
    },
    "BP_GoldPouches_Phantom_ItemInfo_C": {
        "Name": "Gold Pouch",
    },
    "BP_GoldPouches_ItemInfo_C": {
        "Name": "Gold Pouch",
    },
    "BP_AmmoPouch_ItemInfo_C": {
        "Name": "Ammo Pouch",
    },
}

ai_common_drops_keys = set(ai_common_drops.keys())
mapping_raw_name_comp.update(ai_common_drops)

# ---------------------------------------------------- Megalodons ---------------------------------------------------- #
megs = {
    "BP_TinyShark_C": {
        "Name": "Megalodon",
    },
    "BP_TinySharkExperience_C": {
        "Name": "Megalodon Respawn Zone",
    },
}

meg_keys = set(megs.keys())
mapping_raw_name_comp.update(megs)

# ---------------------------------------------------- Ashen Lord ---------------------------------------------------- #
ashlord = {
    "BP_GiantSkeletonPawnBase_C": {
        "Name": "Ashen Lord",
    },
}

ashlord_keys = set(ashlord.keys())
mapping_raw_name_comp.update(ashlord)

# ---------------------------------------------------- Mermaid ---------------------------------------------------- #
mermaid = {
    "BP_Mermaid_C": {
        "Name": "Mermaid",
    },
}

mermaid_keys = set(mermaid.keys())
mapping_raw_name_comp.update(mermaid)

# -------------------------------------------------- Loot Mermaid -------------------------------------------------- #
lootmermaid = {
    "BP_LootStorage_Retrieve_C": {
        "Name": "Loot Mermaid",
    },
}

lootmermaid_keys = set(lootmermaid.keys())
mapping_raw_name_comp.update(lootmermaid)

# ------------------------------------------------ Animal Container ------------------------------------------------ #
animalcontain = {
    "BP_MerchantCrate_SnakeBasket_ItemInfo_C": {
        "Name": "Snake Basket",
    },
    "BP_MerchantCrate_ChickenCrate_C": {
        "Name": "Chicken Coop",
    },
    "BP_MerchantCrate_PigCrate_ItemInfo_C": {
        "Name": "Pig Crate",
    },
}

animalcontain_keys = set(animalcontain.keys())
mapping_raw_name_comp.update(animalcontain)

# ------------------------------------------------ Gunpowder Barrels ------------------------------------------------ #
gunpowder = {
    "BP_MerchantCrate_BigGunpowderBarrel_ItemInfo_C": {
        "Name": "Stronghold Gunpowder Barrel",
    },
    "BP_MerchantCrate_GunpowderBarrel_ItemInfo_C": {
        "Name": "Gunpowder Barrel",
    },
    "BP_MerchantCrate_PigCrate_ItemInfo_C": {
        "Name": "Pig Crate",
    },
}

gunpowder_keys = set(gunpowder.keys())
mapping_raw_name_comp.update(gunpowder)

# ---------------------------------------------------- Gifts ---------------------------------------------------- #
gifts = {
    "BP_HighValueGift_ItemInfo_C": {
        "Name": "Generous Gift",
    },
    "BP_LowValueGift_ItemInfo_C": {
        "Name": "Humble Gift",
    },
    "BP_PL_HauntedBrazier_C": {
        "Name": "Ancient's Brazier",
    },
    "BP_HauntedIsalnd_FinalBeacon_C": {
        "Name": "Final Brazier",
    },
}

gifts_keys = set(gifts.keys())
mapping_raw_name_comp.update(gifts)

# --------------------------------------------------- Reaper Loot --------------------------------------------------- #
reaploot = {
    "BP_ReapersBounty_ItemInfo_C": {
        "Name": "Reapers Bounty",
    },
    "BP_FortReapersBountyChest_ItemInfo_C": {
        "Name": "Reapers Bounty",
    },
    "BP_ReapersChest_ItemInfo_C": {
        "Name": "Reapers Chest",
    },
    "BP_FortReapersChest_ItemInfo_C": {
        "Name": "Reapers Chest",
    },
}

reaploot_keys = set(reaploot.keys())
mapping_raw_name_comp.update(reaploot)

# --------------------------------------------------- Event Keys --------------------------------------------------- #
eventkeys = {
    "BP_FotD_StrongholdKey_ItemInfo_C": {
        "Name": "FoTD Key",
    },
    "BP_LegendaryFort_StrongholdKey_ItemInfo_C": {
        "Name": "Fort of Fortune Key",
    },
    "ShipWreckGraveyardKeyItemInfo_C": {
        "Name": "Shipwreck Graveyard Key",
    },
    "BP_SeaFort_Key_Vault_ItemInfo_C": {
        "Name": "Sea Fort Key",
    },
    "BP_SeaFort_Key_StoreRoom_ItemInfo_C": {
        "Name": "Sea Fort Store Room Key",
    },
    "BP_StrongholdKey_ItemInfo_C": {
        "Name": "Stronghold Key",
    },
    "BP_OldKey_Goblet2_ItemInfo_C": {
        "Name": "Old Sailor's Key",
    },
}

eventkeys_keys = set(eventkeys.keys())
mapping_raw_name_comp.update(eventkeys)

# --------------------------------------------------- Ashen Key --------------------------------------------------- #
ashenkey = {
    "BP_AshenKey_ItemInfo_C": {
        "Name": "Ashen Key",
    },
}

ashenkey_keys = set(ashenkey.keys())
mapping_raw_name_comp.update(ashenkey)

# -------------------------------------------------- General Keys -------------------------------------------------- #
genkey = {
    "BP_Totem_GoldShark_ItemInfo_C": {
        "Name": "Krakens Fall Gold Key",
    },
    "BP_Totem_SilverShark_ItemInfo_C": {
        "Name": "Krakens Fall Silver Key",
    },
    "BP_Totem_StoneShark_ItemInfo_C": {
        "Name": "Krakens Fall Stone Key",
    },
    "BP_Totem_GoldBoar_ItemInfo_C": {
        "Name": "Devils Ridge Gold Key",
    },
    "BP_Totem_SilverBoar_ItemInfo_C": {
        "Name": "Devils Ridge Silver Key",
    },
    "BP_Totem_StoneBoar_ItemInfo_C": {
        "Name": "Devils Ridge Stone Key",
    },
    "BP_Totem_GoldMoon_ItemInfo_C": {
        "Name": "Crescent Isle Gold Key",
    },
    "BP_Totem_SilverMoon_ItemInfo_C": {
        "Name": "Crescent Isle Silver Key",
    },
    "BP_Totem_StoneMoon_ItemInfo_C": {
        "Name": "Crescent Isle Stone Key",
    },
    "BP_Totem_GoldSnake_ItemInfo_C": {
        "Name": "Mermaids Hideaway Gold Key",
    },
    "BP_Totem_SilverSnake_ItemInfo_C": {
        "Name": "Mermaids Hideaway Silver Key",
    },
    "BP_Totem_StoneSnake_ItemInfo_C": {
        "Name": "Mermaids Hideaway Stone Key",
    },
    "BP_Totem_GoldScarab_ItemInfo_C": {
        "Name": "Crooks Hollow Gold Key",
    },
    "BP_Totem_SilverScarab_ItemInfo_C": {
        "Name": "Crooks Hollow Silver Key",
    },
    "BP_Totem_StoneScarab_ItemInfo_C": {
        "Name": "Crooks Hollow Stone Key",
    },
    "BP_Totem_GoldCrab_ItemInfo_C": {
        "Name": "N-13 Gold Key",
    },
    "BP_Totem_SilverCrab_ItemInfo_C": {
        "Name": "N-13 Silver Key",
    },
    "BP_Totem_StoneCrab_ItemInfo_C": {
        "Name": "N-13 Stone Key",
    },
    "BP_Totem_GoldEagle_ItemInfo_C": {
        "Name": "Fletcher's Rest Gold Key",
    },
    "BP_Totem_SilverEagle_ItemInfo_C": {
        "Name": "Fletcher's Rest Silver Key",
    },
    "BP_Totem_StoneEagle_ItemInfo_C": {
        "Name": "Fletcher's Rest Stone Key",
    },
    "BP_Totem_GoldSun_ItemInfo_C": {
        "Name": "Ashen Reaches Gold Key",
    },
    "BP_Totem_SilverSun_ItemInfo_C": {
        "Name": "Ashen Reaches Silver Key",
    },
    "BP_Totem_StoneSun_ItemInfo_C": {
        "Name": "Ashen Reaches Stone Key",
    },
}

genkey_keys = set(genkey.keys())
mapping_raw_name_comp.update(genkey)

# --------------------------------------------------- Tridents --------------------------------------------------- #
trident = {
    "BP_SirenTrident_ItemInfo_C": {
        "Name": "Trident of Dark Tides",
    },
}

trident_keys = set(trident.keys())
mapping_raw_name_comp.update(trident)

# -------------------------------------------------- Sea Fort Gold -------------------------------------------------- #
sfgold = {
    "BP_SeaFortGoldPouches_ItemInfo_C": {
        "Name": "Sea Fort Gold Pouch",
    },
}

sfgold_keys = set(sfgold.keys())
mapping_raw_name_comp.update(sfgold)

# -------------------------------------------------- Medallions -------------------------------------------------- #
medallions = {
    "BP_Medallion_Shark_ItemInfo_C": {
        "Name": "Shark Medallion",
    },
    "BP_Medallion_Boar_ItemInfo_C": {
        "Name": "Shark Medallion",
    },
    "BP_Medallion_Moon_ItemInfo_C": {
        "Name": "Moon Medallion",
    },
    "BP_Medallion_Snake_ItemInfo_C": {
        "Name": "Snake Medallion",
    },
    "BP_Medallion_Scarab_ItemInfo_C": {
        "Name": "Scarab Medallion",
    },
    "BP_Medallion_Crab_ItemInfo_C": {
        "Name": "Crab Medallion",
    },
    "BP_Medallion_Eagle_ItemInfo_C": {
        "Name": "Eagle Medallion",
    },
    "BP_Medallion_Sun_ItemInfo_C": {
        "Name": "Sun Medallion",
    },
}

medallions_keys = set(medallions.keys())
mapping_raw_name_comp.update(medallions)

# ---------------------------------------------------- Islands ---------------------------------------------------- #
islands = {
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop (Near)",
    },
}

island_keys = set(islands.keys())
mapping_raw_name_comp.update(islands)

# ---------------------------------------------------- Outposts ---------------------------------------------------- #
outposts = {
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop (Near)",
    },
}

outpost_keys = set(outposts.keys())
mapping_raw_name_comp.update(outposts)

# ---------------------------------------------------- Tomes ---------------------------------------------------- #
tomes = {
    "BP_AshenTomeVol1_05_ItemInfo_C": {
        "Name": "Tome of Curses V",
    },
    "BP_AshenTomeVol1_04_ItemInfo_C": {
        "Name": "Tome of Curses IV",
    },
    "BP_AshenTomeVol1_03_ItemInfo_C": {
        "Name": "Tome of Curses III",
    },
    "BP_AshenTomeVol1_02_ItemInfo_C": {
        "Name": "Tome of Curses II",
    },
    "BP_AshenTomeVol1_01_ItemInfo_C": {
        "Name": "Tome of Curses I",
    },
    "BP_AshenTomeVol2_05_ItemInfo_C": {
        "Name": "Tome of Power V",
    },
    "BP_AshenTomeVol2_04_ItemInfo_C": {
        "Name": "Tome of Power IV",
    },
    "BP_AshenTomeVol2_03_ItemInfo_C": {
        "Name": "Tome of Power III",
    },
    "BP_AshenTomeVol2_02_ItemInfo_C": {
        "Name": "Tome of Power II",
    },
    "BP_AshenTomeVol2_01_ItemInfo_C": {
        "Name": "Tome of Power I",
    },
    "BP_AshenTomeVol3_05_ItemInfo_C": {
        "Name": "Tome of Fire V",
    },
    "BP_AshenTomeVol3_04_ItemInfo_C": {
        "Name": "Tome of Fire IV",
    },
    "BP_AshenTomeVol3_03_ItemInfo_C": {
        "Name": "Tome of Fire III",
    },
    "BP_AshenTomeVol3_02_ItemInfo_C": {
        "Name": "Tome of Fire II",
    },
    "BP_AshenTomeVol3_01_ItemInfo_C": {
        "Name": "Tome of Fire I",
    },
    "BP_AshenTomeVol4_05_ItemInfo_C": {
        "Name": "Tome of Resurrection V",
    },
    "BP_AshenTomeVol4_04_ItemInfo_C": {
        "Name": "Tome of Resurrection IV",
    },
    "BP_AshenTomeVol4_03_ItemInfo_C": {
        "Name": "Tome of Resurrection III",
    },
    "BP_AshenTomeVol4_02_ItemInfo_C": {
        "Name": "Tome of Resurrection II",
    },
    "BP_AshenTomeVol4_01_ItemInfo_C": {
        "Name": "Tome of Resurrection I",
    },
}

tomes_keys = set(tomes.keys())
mapping_raw_name_comp.update(tomes)

# ------------------------------------------------- Emissary Flags ------------------------------------------------- #
emflags = {
    "BP_EmissaryFlotsam_OrderOfSouls_Rank5_ItemInfo_C": {
        "Name": "Order of Souls Flag Lvl5",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank4_ItemInfo_C": {
        "Name": "Order of Souls Flag Lvl4",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank3_ItemInfo_C": {
        "Name": "Order of Souls Flag Lvl3",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank2_ItemInfo_C": {
        "Name": "Order of Souls Flag Lvl2",
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank1_ItemInfo_C": {
        "Name": "Order of Souls Flag Lvl1",
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank5_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl5",
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank4_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl4",
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank3_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl3",
    },
    "BP_EmissaryFlotsam_GoldHoarders_Rank2_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl2",
    },
    "BP_EmissaryFlotsam_GoldHoarders_ItemInfo_C": {
        "Name": "Gold Hoarder Flag Lvl1",
    },
    "BP_EmissaryFlotsam_Reapers_Rank5_ItemInfo_C": {
        "Name": "Reaper's Bones Flag Lvl5",
    },
    "BP_EmissaryFlotsam_Reapers_Rank4_ItemInfo_C": {
        "Name": "Reaper's Bones Flag Lvl4",
    },
    "BP_EmissaryFlotsam_Reapers_Rank3_ItemInfo_C": {
        "Name": "Reaper's Bones Flag Lvl3",
    },
    "BP_EmissaryFlotsam_Reapers_Rank2_ItemInfo_C": {
        "Name": "Reaper's Bones Flag Lvl2",
    },
    "BP_EmissaryFlotsam_Reapers_ItemInfo_C": {
        "Name": "Reaper's Bones Flag Lvl1",
    },
    "BP_EmissaryFlotsam_AthenasFortune_Rank5_ItemInfo_C": {
        "Name": "Athena's Fortune Flag Lvl5",
    },
    "BP_EmissaryFlotsam_AthenasFortune_Rank4_ItemInfo_C": {
        "Name": "Athena's Fortune Flag Lvl4",
    },
    "BP_EmissaryFlotsam_AthenasFortune_Rank3_ItemInfo_C": {
        "Name": "Athena's Fortune Flag Lvl3",
    },
    "BP_EmissaryFlotsam_AthenasFortune_Rank2_ItemInfo_C": {
        "Name": "Athena's Fortune Flag Lvl2",
    },
    "BP_EmissaryFlotsam_AthenasFortune_ItemInfo_C": {
        "Name": "Athena's Fortune Flag Lvl1",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_Rank5_ItemInfo_C": {
        "Name": "Merchant Alliance Flag Lvl5",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_Rank4_ItemInfo_C": {
        "Name": "Merchant Alliance Flag Lvl4",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_Rank3_ItemInfo_C": {
        "Name": "Merchant Alliance Flag Lvl3",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_Rank2_ItemInfo_C": {
        "Name": "Merchant Alliance Flag Lvl2",
    },
    "BP_EmissaryFlotsam_MerchantAlliance_ItemInfo_C": {
        "Name": "Merchant Alliance Flag Lvl1",
    },
}

emflags_keys = set(emflags.keys())
mapping_raw_name_comp.update(emflags)

# ------------------------------------------------- Merchant Loot ------------------------------------------------- #
merchantcrates = {
    "BP_MerchantCrate_Commodity_GhostCrate_ItemInfo_C": {
        "Name": "Ashes of the Damned",
    },
    "BP_MerchantManifest_01a_ItemInfo_C": {
        "Name": "Manifest",
    },
    "BP_MerchantManifest_01b_ItemInfo_C": {
        "Name": "Esteemed Manifest",
    },
    "BP_MerchantManifest_01c_ItemInfo_C": {
        "Name": "Eminent Manifest",
    },
    "BP_MerchantManifest_01d_ItemInfo_C": {
        "Name": "Revered Merchant Manifest",
    },
    "BP_MerchantCrate_Commodity_Fort_ItemInfo_C": {
        "Name": "Crate of Ancient Bone Dust",
    },
    "BP_MerchantCrate_Commodity_Gemstones_ItemInfo_C": {
        "Name": "Crate of Precious Gemstones",
    },
    "BP_MerchantCrate_Commodity_Minerals_ItemInfo_C": {
        "Name": "Crate of Minerals",
    },
    "BP_SKMerchantCommodity_ForgottenJewels_ItemInfo_C": {
        "Name": "Casket of Forgotten Jewels",
    },
    "BP_SKMerchantCommodity_AntiCoffee_ItemInfo_C": {
        "Name": "Casket of Antiquated Coffee",
    },
    "BP_MerchantCrate_Commodity_SpiceCrate_ItemInfo_C": {
        "Name": "Crate of Exquisite Spices",
    },
    "BP_MerchantCrate_Commodity_Ore_ItemInfo_C": {
        "Name": "Crate of Fine Ore",
    },
    "BP_MerchantCrate_Commodity_SilkCrate_ItemInfo_C": {
        "Name": "Crate of Exotic Silks",
    },
    "BP_MerchantCrate_Commodity_VolcanicStone_ItemInfo_C": {
        "Name": "Crate of Volcanic Stone",
    },
    "BP_MerchantCrate_Commodity_TeaCrate_ItemInfo_C": {
        "Name": "Crate of Rare Tea",
    },
    "BP_MerchantCrate_Commodity_SugarCrate_ItemInfo_C": {
        "Name": "Crate of Fine Sugar",
    },
    "BP_UnsortedCommodity_Gemstones_ItemInfo_C": {
        "Name": "Crate of Unclassified Gemstones",
    },
    "BP_UnsortedCommodity_Minerals_ItemInfo_C": {
        "Name": "Crate of Unfiltered Minerals",
    },
    "BP_UnsortedCommodity_Stone_ItemInfo_C": {
        "Name": "Crate of Broken Stone",
    },
    "BP_UnsortedCommodity_Spices_ItemInfo_C": {
        "Name": "Crate of Unrefined Spices",
    },
    "BP_UnsortedCommodity_Silks_ItemInfo_C": {
        "Name": "Crate of Unsorted Silks",
    },
    "BP_UnsortedCommodity_Tea_ItemInfo_C": {
        "Name": "Crate of Ungraded Tea",
    },
    "BP_UnsortedCommodity_Sugar_ItemInfo_C": {
        "Name": "Crate of Raw Sugar",
    },
    "BP_CargoRunCrate_Cloth_ItemInfo_C": {
        "Name": "Crate of Luxurious Cloth",
    },
    "BP_CargoRunCrate_Plants_ItemInfo_C": {
        "Name": "Crate of Plants",
    },
    "BP_CargoRunCrate_Rum_ItemInfo_C": {
        "Name": "Crate of Rum",
    },
}

merchantcrates_keys = set(merchantcrates.keys())
mapping_raw_name_comp.update(merchantcrates)

# ------------------------------------------------- GH Relics ------------------------------------------------- #
ghrelics = {
    "BP_TreasureArtifact_ItemInfo_DVR_Mythical_C": {
        "Name": "Magma Grail",
    },
    "BP_TreasureArtifact_ItemInfo_DVR_Legendary_C": {
        "Name": "Devil's Remnant",
    },
    "BP_TreasureArtifact_Vault_impressive_01_a_ItemInfo_C": {
        "Name": "Opulent Curio",
    },
    "BP_TreasureArtifact_ItemInfo_impressive_01_a_C": {
        "Name": "Opulent Curio",
    },
    "BP_TreasureArtifact_Vault_impressive_02_a_ItemInfo_C": {
        "Name": "Adorned Receptacle",
    },
    "BP_TreasureArtifact_ItemInfo_impressive_02_a_C": {
        "Name": "Adorned Receptacle",
    },
    "BP_TreasureArtifact_Vault_impressive_03_a_ItemInfo_C": {
        "Name": "Peculiar Relic",
    },
    "BP_TreasureArtifact_ItemInfo_impressive_03_a_C": {
        "Name": "Peculiar Relic",
    },
    "BP_SKCoralTrinket_Mythical_ItemInfo_C": {
        "Name": "Peculiar Coral Relic",
    },
    "BP_TreasureArtifact_ItemInfo_DVR_Rare_C": {
        "Name": "Brimstone Casket",
    },
    "BP_TreasureArtifact_Vault_box_03_a_ItemInfo_C": {
        "Name": "Golden Reliquary",
    },
    "BP_TreasureArtifact_ItemInfo_box_03_a_C": {
        "Name": "Golden Reliquary",
    },
    "BP_SKCoralTrinket_Legendary_ItemInfo_C": {
        "Name": "Golden Coral Reliquary",
    },
    "BP_TreasureArtifact_Vault_goblet_03_a_ItemInfo_C": {
        "Name": "Gilded Chalice",
    },
    "BP_TreasureArtifact_ItemInfo_goblet_03_a_C": {
        "Name": "Gilded Chalice",
    },
    "BP_TreasureArtifact_Vault_vase_03_a_ItemInfo_C": {
        "Name": "Ornate Carafe",
    },
    "BP_TreasureArtifact_ItemInfo_vase_03_a_C": {
        "Name": "Ornate Carafe",
    },
    "BP_TreasureArtifact_ItemInfo_DVR_Common_C": {
        "Name": "Roaring Goblet",
    },
    "BP_TreasureArtifact_Vault_goblet_02_a_ItemInfo_C": {
        "Name": "Silvered Cup",
    },
    "BP_TreasureArtifact_ItemInfo_goblet_02_a_C": {
        "Name": "Silvered Cup",
    },
    "BP_SKCoralTrinket_Rare_ItemInfo_C": {
        "Name": "Silvered Coral Cup",
    },
    "BP_TreasureArtifact_Vault_vase_02_a_ItemInfo_C": {
        "Name": "Elaborate Flagon",
    },
    "BP_TreasureArtifact_ItemInfo_vase_02_a_C": {
        "Name": "Elaborate Flagon",
    },
    "BP_TreasureArtifact_Vault_box_02_a_ItemInfo_C": {
        "Name": "Decorative Coffer",
    },
    "BP_TreasureArtifact_ItemInfo_box_02_a_C": {
        "Name": "Decorative Coffer",
    },
    "BP_TreasureArtifact_Vault_vase_01_a_ItemInfo_C": {
        "Name": "Mysterious Vessel",
    },
    "BP_TreasureArtifact_ItemInfo_vase_01_a_C": {
        "Name": "Mysterious Vessel",
    },
    "BP_SKCoralTrinket_Common_ItemInfo_C": {
        "Name": "Mysterious Coral Vessel",
    },
    "BP_TreasureArtifact_Vault_box_01_a_ItemInfo_C": {
        "Name": "Bronze Secret-Keeper",
    },
    "BP_TreasureArtifact_ItemInfo_box_01_a_C": {
        "Name": "Bronze Secret-Keeper",
    },
    "BP_TreasureArtifact_Vault_goblet_01_a_ItemInfo_C": {
        "Name": "Ancient Goblet",
    },
    "BP_TreasureArtifact_ItemInfo_goblet_01_a_C": {
        "Name": "Ancient Goblet",
    },
}

ghrelics_keys = set(ghrelics.keys())
mapping_raw_name_comp.update(ghrelics)

# ------------------------------------------------- GH Chests ------------------------------------------------- #
ghchests = {
    "BP_TreasureChest_ItemInfo_Fort_C": {
        "Name": "Stronghold Chest",
    },
    "BP_TreasureChest_Vault_ItemInfo_C": {
        "Name": "Chest of Ancient Tributes",
    },
    "BP_TreasureChest_ItemInfo_Ghost_C": {
        "Name": "Chest of the Damned",
    },
    "BP_TreasureChest_ItemInfo_AIShip_C": {
        "Name": "Skeleton Captain's Chest",
    },
    "BP_TreasureChest_ItemInfo_Mythical_DVR_C": {
        "Name": "Ashen Captain's Chest",
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Mythical_C": {
        "Name": "Shipwrecked Captain's Chest",
    },
    "BP_TreasureChest_ItemInfo_Drunken_C": {
        "Name": "Chest of a Thousand Grogs",
    },
    "BP_TreasureChest_ItemInfo_ChestOfRage_C": {
        "Name": "Chest of Rage",
    },
    "BP_TreasureChest_ItemInfo_Weeping_C": {
        "Name": "Chest of Sorrow",
    },
    "BP_TreasureChest_ItemInfo_EverlastingSorrow_C": {
        "Name": "Chest of Everlasting Sorrow",
    },
    "BP_TreasureChest_Vault_Mythical_ItemInfo_C": {
        "Name": "Captain's Chest",
    },
    "BP_TreasureChest_ItemInfo_Mythical_C": {
        "Name": "Captain's Chest",
    },
    "BP_SK_CoralChest_ItemInfo_Mythical_C": {
        "Name": "Coral Captain's Chest",
    },
    "BP_TreasureChest_ItemInfo_Legendary_DVR_C": {
        "Name": "Ashen Marauder's Chest",
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Legendary_C": {
        "Name": "Shipwrecked Marauder's Chest",
    },
    "BP_TreasureChest_Vault_Legendary_ItemInfo_C": {
        "Name": "Marauder's Chest",
    },
    "BP_TreasureChest_ItemInfo_Legendary_C": {
        "Name": "Marauder's Chest",
    },
    "BP_SK_CoralChest_ItemInfo_Legendary_C": {
        "Name": "Coral Marauder Chest",
    },
    "BP_TreasureChest_ItemInfo_Rare_DVR_C": {
        "Name": "Ashen Seafarer's Chest",
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Rare_C": {
        "Name": "Shipwrecked Seafarer's Chest",
    },
    "BP_TreasureChest_Vault_Rare_ItemInfo_C": {
        "Name": "Seafarer's Chest",
    },
    "BP_TreasureChest_ItemInfo_Rare_C": {
        "Name": "Seafarer's Chest",
    },
    "BP_SK_CoralChest_ItemInfo_Rare_C": {
        "Name": "Coral Seafarer's Chest",
    },
    "BP_TreasureChest_ItemInfo_Common_DVR_C": {
        "Name": "Ashen Castaway's Chest",
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Common_C": {
        "Name": "Shipwrecked Castaway's Chest",
    },
    "BP_TreasureChest_Vault_Common_ItemInfo_C": {
        "Name": "Castaway's Chest",
    },
    "BP_TreasureChest_ItemInfo_Common_C": {
        "Name": "Castaway's Chest",
    },
    "BP_SK_CoralChest_ItemInfo_Common_C": {
        "Name": "Coral Castaway Chest",
    },
}

ghchests_keys = set(ghchests.keys())
mapping_raw_name_comp.update(ghchests)

# ------------------------------------------------- Rare Loot ------------------------------------------------- #
rareloot = {
    "BP_Wondrous_ItemInfo_C": {
        "Name": "Box of Wondrous Secrets",
    },
    "BP_TreasureChest_ItemInfo_PirateLegend_DVR_C": {
        "Name": "Ashen Chest of Legends",
    },
    "BP_TreasureChest_ItemInfo_PirateLegend_C": {
        "Name": "Chest of Legends",
    },
    "BP_trs_box_leg_01_a_ItemInfo_C": {
        "Name": "Offering of Legendary Goods",
    },
    "BP_trs_dark_shark_leg_01_a_ItemInfo_C": {
        "Name": "Artifact of Legendary Hunger",
    },
    "BP_trs_impressive_leg_01_a_ItemInfo_C": {
        "Name": "Athena's Relic",
    },
    "BP_trs_jar_leg_01_a_ItemInfo_C": {
        "Name": "Jar of Athena's Incense",
    },
    "BP_trs_jewellery_box_leg_01_a_ItemInfo_C": {
        "Name": "Legendary Fortune Keeper",
    },
    "BP_PL_StoneOfAncients_ItemInfo_C": {
        "Name": "Stone of Ancients",
    },
    "BP_trs_leg_crain__leg_01_a_ItemInfo_C": {
        "Name": "Skull of Athena's Blessing",
    },
    "BP_MerchantCrate_PirateLegendBigGunpowderBarrel_ItemInfo_C": {
        "Name": "Keg of Ancient Black Powder",
    },
    "BP_BountyRewardSkull_UncommonPirateLegend_C": {
        "Name": "Villainous Skull of Ancient Fortune",
    },
    "BP_BountyRewardSkull_PirateLegend_C": {
        "Name": "Skull of Ancient Fortune",
    },
    "BP_TreasureArtifact_ItemInfo_piratelegendimpressive_03_a_C": {
        "Name": "Gilded Relic of Ancient Fortune",
    },
    "BP_MerchantCrate_CommonPirateLegend_ItemInfo_C": {
        "Name": "Crate of Legendary Voyages",
    },
    "BP_TreasureArtifact_ItemInfo_piratelegend_goblet_02_a_C": {
        "Name": "Chalice of Ancient Fortune",
    },
}

rareloot_keys = set(rareloot.keys())
mapping_raw_name_comp.update(rareloot)

# ------------------------------------------------- Projectiles ------------------------------------------------- #
projectiles = {
    "BP_Projectile_CannonBall_C": {
        "Name": "Cannonball Projectile",
    },
    "BP_Projectile_SirenTrident_C": {
        "Name": "Siren Trident Projectile",
    },
    "BP_Projectile_SirenSong_C": {
        "Name": "Siren Song Projectile",
    },
}

projectiles_keys = set(projectiles.keys())
mapping_raw_name_comp.update(projectiles)

mapping_raw_name_keys = set(mapping_raw_name_comp.keys())
