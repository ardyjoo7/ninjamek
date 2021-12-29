from dataclasses import dataclass
from typing import Dict, List
from .EnemyInfo import Enemy, enemies


@dataclass
class Mission:
    enemies: List[Enemy]
    id: str
    grade: str
    name: str
    level: str
    premium: bool
    daily: bool
    campaign: bool
    reward_tp: int
    reward_xp: int
    reward_gold: int


missions: Dict[str, Mission] = {
    "msn_1": Mission(
        [enemies["ene_01"]], "msn_1", "c", "Hardworking Ninja", "1", False, False, False, 0, 15, 20),
    "msn_2": Mission(
        [enemies["ene_03"]], "msn_2", "c", "Blacksmith\'s Request", "2", False, False, False, 0, 30, 40),
    "msn_3": Mission(
        [enemies["ene_04"]], "msn_3", "c", "Confidential Document", "3", False, False, False, 0, 45, 60),
    "msn_4": Mission(
        [enemies["ene_05"]], "msn_4", "c", "Weaver\'s Request", "4", False, False, False, 0, 60, 80),
    "msn_5": Mission(
        [enemies["ene_07"]], "msn_5", "c", "Conflicts with the Samurai", "5", False, False, False, 0, 70, 80),
    "msn_6": Mission(
        [enemies["ene_04"]], "msn_6", "c", "Michi\'s Request", "6", False, False, False, 0, 75, 60),
    "msn_7": Mission(
        [enemies["ene_04"]], "msn_7", "c", "Yuna\'s Request", "7", False, False, False, 0, 150, 90),
    "msn_8": Mission([enemies["ene_08"], enemies["ene_09"]], "msn_8", "c",
                     "Find the Antidote", "8", False, False, False, 0, 150, 90),
    "msn_9": Mission(
        [enemies["ene_03"]], "msn_9", "c", "Grandmother\'s Gift", "9", False, False, False, 0, 260, 105),
    "msn_10": Mission([enemies["ene_14"], enemies["ene_15"]], "msn_10", "c",
                      "Fake Worshippers", "10", False, False, False, 0, 335, 150),
    "msn_11": Mission([enemies["ene_10"], enemies["ene_11"], enemies["ene_12"]], "msn_11", "c",
                      "Attack from Ninja Pirates", "11", False, False, False, 0, 350, 165),
    "msn_12": Mission([enemies["ene_47"], enemies["ene_47"]], "msn_12", "c",
                      "Kusuma\'s Request", "12", False, False, False, 0, 370, 180),
    "msn_13": Mission([enemies["ene_04"], enemies["ene_05"]], "msn_13",
                      "c", "Kage\'s Son", "13", False, False, False, 0, 420, 210),
    "msn_14": Mission([enemies["ene_07"], enemies["ene_07"]], "msn_14", "c",
                      "It\'s the Samurai Again", "14", False, False, False, 0, 450, 225),
    "msn_15": Mission([enemies["ene_38"], enemies["ene_03"]], "msn_15", "c",
                      "Assassinate the Ninja Spy Leader", "15", False, False, False, 0, 480, 240),
    # FIXME: Enemies should be ene_02, but we don't have any data for it
    "msn_16": Mission(
        [], "msn_16", "c", "Undead Marionette", "16", False, False, False, 0, 540, 240),
    "msn_17": Mission([enemies["ene_28"], enemies["ene_28"]], "msn_17", "c",
                      "Kenta\'s Favor", "17", False, False, False, 0, 570, 270),
    "msn_18": Mission([enemies["ene_47"], enemies["ene_60"]], "msn_18", "c",
                      "Trouble from Hooligans", "18", False, False, False, 0, 600, 285),
    "msn_19": Mission([enemies["ene_04"], enemies["ene_05"]], "msn_19", "c",
                      "Clear Main Artery", "19", False, False, False, 0, 630, 300),
    "msn_20": Mission([enemies["ene_29"], enemies["ene_31"]], "msn_20", "c",
                      "Troublesome Water Ninja", "20", False, False, False, 0, 660, 315),
}
