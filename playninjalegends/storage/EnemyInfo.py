from dataclasses import dataclass
from typing import Dict


@dataclass
class Enemy:
    id: str
    level: int
    name: str
    hp: int
    cp: int
    dodge: int
    critical: int
    purify: int
    accuracy: int
    agility: int
    size_x: float
    size_y: float


enemies: Dict[str, Enemy] = {
    "ene_01": Enemy("ene_01", 1, "Clone of Shin", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_03": Enemy("ene_03", 1, "Ninja Spy", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_04": Enemy("ene_04", 2, "Ninja Bandit", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_05": Enemy("ene_05", 3, "Female Ninja Bandit", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_07": Enemy("ene_07", 4, "Samurai", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_08": Enemy("ene_08", 6, "Ninja Ops", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_09": Enemy("ene_09", 6, "Ninja Ops", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_10": Enemy("ene_10", 8, "Captain Ninja Pirate", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_11": Enemy("ene_11", 8, "Ninja Pirate", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_12": Enemy("ene_12", 8, "Ninja Pirate", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_14": Enemy("ene_14", 7, "Wandering Monk", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_15": Enemy("ene_15", 7, "Wandering Monk", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_28": Enemy("ene_38", 13, "Fierce Cat", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_29": Enemy("ene_29", 18, "Water Village Genin", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_31": Enemy("ene_31", 18, "Toxic Village Genin", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_34": Enemy("ene_34", 19, "Lightning Village Genin", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_38": Enemy("ene_38", 13, "Ninja Assassin Leader", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_47": Enemy("ene_47", 10, "Crazy Hooligan", 0, 125, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_60": Enemy("ene_60", 10, "Iron Arm Hooligan", 0, 0, 0, 5, 5, 0, 8, 0.65, 0.65),
    "ene_81": Enemy("ene_81", 10, "Ginkotsu", 7293, 2800, 10, 10, 10, 10, 34, 0.5, 0.5),
    "ene_82": Enemy("ene_82", 20, "Shikigami Yanki", 12760, 2800, 10, 10, 10, 10, 59, 0.55, 0.55),
    "ene_101": Enemy("ene_101", 99, "Ancient Frost Demon", 9999, 9999, 10, 10, 10, 10, 8, 0.55, 0.55),
    "ene_102": Enemy("ene_102", 99, "Glacial Ward", 9999, 9999, 10, 10, 10, 10, 8, 0.55, 0.55),
    "ene_103": Enemy("ene_103", 99, "Snow Treant", 9999, 9999, 10, 10, 10, 10, 8, 0.55, 0.55),
    "ene_104": Enemy("ene_104", 99, "Poinsettia Wolf", 9999, 9999, 10, 10, 10, 10, 8, 0.55, 0.55),
    "ene_105": Enemy("ene_105", 99, "Ice Titan", 9999, 9999, 10, 10, 10, 10, 8, 0.55, 0.55),
    "ene_106": Enemy("ene_106", 99, "Yukidaruma", 9999, 9999, 10, 10, 10, 10, 8, 0.55, 0.55),
}
