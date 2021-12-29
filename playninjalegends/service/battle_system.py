from typing import Dict, Union
from hashlib import sha256
from random import randint

from ..utils import AMFClient
from ..store import Element, User, Character
from ..storage.MissionInfo import Mission, missions
from ..storage import calc_real_enemy_stat


class BattleSystem:
    __client: AMFClient
    user: User

    def __init__(self, client: AMFClient, user: User) -> None:
        self.__client = client
        self.user = user

    def startMission(
        self,
        character: Union[Character, int],
        mission: Union[Mission, int],
        charAgility: int = None,
        user: User = None
    ) -> Union[str, None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if type(character) == Character:
            # TODO: move this somewhere else
            if charAgility is None:
                charAgility = character.attributes[Element.WIND] + character.level + 10
            character = character.cid
        if charAgility is None:
            raise ValueError("charAgility must be set")

        if type(mission) == int:
            mission = missions[f"msn_{mission}"]

        enemiesIdStr = ",".join([enemy.id for enemy in mission.enemies])

        enemiesStat = []
        for enemy in mission.enemies:
            enemy = calc_real_enemy_stat(enemy, mission=mission)
            enemiesStat.append(f"id:{enemy.id}|hp:{enemy.hp}|agility:{enemy.agility}")

        enemiesStatStr = "#".join(enemiesStat)
        _hash = sha256(f"{enemiesIdStr}{enemiesStatStr}{charAgility}".encode())

        ev = self.__client.createEnvelope(
            target="BattleSystem.startMission",
            body=[
                f"{character}",
                mission.id,
                enemiesIdStr,
                enemiesStatStr,
                f"{charAgility}",
                _hash.hexdigest(),
                user.SessionKey,
            ],
        )
        resEv = self.__client.sendEnvelope(ev)
        if (
            "status" in resEv.bodies[0][1].body
            and resEv.bodies[0][1].body["status"] != 1
        ):
            return None
        battleCode = resEv.bodies[0][1].body
        return battleCode

    def finishMission(
        self,
        character: Union[Character, int],
        mission: Union[Mission, int],
        battleCode: str,
        user: User = None
    ) -> Dict:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if type(character) == Character:
            character = character.cid

        if type(mission) == int:
            mission = missions[f"msn_{mission}"]

        total_damage = 0
        for enemy in mission.enemies:
            total_damage += enemy.hp + randint(0, 200)

        _hash = sha256(f"{mission.id}{character}{battleCode}{total_damage}".encode())
        ev = self.__client.createEnvelope(
            target="BattleSystem.finishMission",
            body=[
                f"{character}",
                mission.id,
                battleCode,
                _hash.hexdigest(),
                f"{total_damage}",
                user.SessionKey,
            ],
        )
        resEv = self.__client.sendEnvelope(ev)
        if (
            "status" in resEv.bodies[0][1].body
            and resEv.bodies[0][1].body["status"] != 1
        ):
            return None
        return resEv.bodies[0][1].body
