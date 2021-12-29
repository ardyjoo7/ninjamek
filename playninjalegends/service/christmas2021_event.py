from typing import Any, Dict, Union
from hashlib import sha256
from random import randint

from ..utils import AMFClient
from ..store import Character, Element, User
from ..storage import enemies, calc_real_enemy_stat


class Christmas2021Event:
    __client: AMFClient
    user: User

    def __init__(self, client: AMFClient, user: User) -> None:
        self.__client = client
        self.user = user

    def getData(
        self, character: Union[Character, int], user: User = None
    ) -> Union[Dict[str, Any], None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if type(character) == Character:
            character = character.cid

        ev = self.__client.createEnvelope(
            "ChristmasEvent2021.getData", body=[f"{user.SessionKey}", f"{character}"]
        )
        resEv = self.__client.sendEnvelope(ev)
        if (
            "status" in resEv.bodies[0][1].body
            and resEv.bodies[0][1].body["status"] != 1
        ):
            return None
        return resEv.bodies[0][1].body

    def startEvent(
        self,
        character: Union[int, Character],
        bossNum: int,
        charLevel: int = None,
        charAgility: int = None,
        user: User = None,
    ) -> Union[str, None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if bossNum < 1 or bossNum > 6:
            raise IndexError("Ivalid christmas boss number")

        if type(character) is Character:
            # TODO: move this somewhere else
            if charAgility is None:
                charAgility = character.attributes[Element.WIND] + character.level + 10
            charLevel = character.level
            character = character.cid

        if charAgility is None:
            raise ValueError("charAgility must be set")
        if charLevel is None:
            raise ValueError("charLevel must be set")

        boss = enemies[f"ene_10{bossNum}"]
        boss = calc_real_enemy_stat(boss, charLevel)
        fmtBoss = f"id:{boss.id}|hp:{boss.hp}|agility:{boss.agility}"
        _hash = sha256(f"{boss.id}{fmtBoss}{charAgility}".encode())
        # "ChristmasEvent2021.startEvent",[Character.char_id,Character.christmas_boss_num,bossId,fmt,agiStats,_loc8_,Character.sessionkey]
        ev = self.__client.createEnvelope(
            "ChristmasEvent2021.startEvent",
            [
                f"{character}",
                f"{bossNum-1}",
                boss.id,
                fmtBoss,
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

    def finishEvent(
        self,
        characterId: Union[int, Character],
        bossNum: int,
        battleCode: str,
        user: User = None,
    ) -> Union[Dict[str, Any], None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if bossNum < 1 or bossNum > 6:
            raise IndexError("Ivalid christmas boss number")

        if type(characterId) is Character:
            characterId = characterId.cid

        boss = enemies[f"ene_10{bossNum}"]
        boss = calc_real_enemy_stat(boss, characterId)
        total_damage = boss.hp + randint(0, 200)

        _hash = sha256(f"{bossNum-1}{characterId}{battleCode}{total_damage}".encode())
        ev = self.__client.createEnvelope(
            "ChristmasEvent2021.finishEvent",
            [
                f"{characterId}",
                f"{bossNum-1}",
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
