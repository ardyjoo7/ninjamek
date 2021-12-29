from typing import Union
from .EnemyInfo import Enemy, enemies
from .MissionInfo import Mission, missions
from ..store import Character


def calc_real_enemy_stat(enemy: Enemy, char: Union[Character, int, None] = None, mission: Union[Mission, int, None] = None) -> Enemy:
    if char is None and mission is None:
        raise ValueError("either char or mission must be set")

    if enemy.level == 99:
        if type(char) == Character:
            char = char.level
        enemy.hp = int(char) * 50
        enemy.cp = int(char) * 50
        enemy.agility = 11 + int(char)

    if enemy.hp == 0:
        if type(mission) == Mission:
            mission = int(mission.level)
        enemy.hp = 30 + int(mission) * 15
        enemy.cp = 30 + int(mission) * 15
        enemy.agility = 11 + int(mission)

    return enemy
