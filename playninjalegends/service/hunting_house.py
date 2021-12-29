from typing import Any, Dict, Union
from hashlib import sha256

from ..utils import AMFClient
from ..store import Character, User


class HuntingHouse:
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

        if type(character) is Character:
            character = character.cid

        ev = self.__client.createEnvelope(
            target="HuntingHouse.getData", body=[f"{user.SessionKey}", f"{character}"]
        )
        resEv = self.__client.sendEnvelope(ev)
        if (
            "status" in resEv.bodies[0][1].body
            and resEv.bodies[0][1].body["status"] != 1
        ):
            return None
        return resEv.bodies[0][1].body

    def startHunting(
        self, character: Union[Character, int], bossNum: int, user: User = None
    ) -> Union[str, None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if type(character) is Character:
            character = character.cid

        ev = self.__client.createEnvelope(
            target="HuntingHouse.startHunting",
            body=[f"{character}", f"{bossNum}", user.SessionKey],
        )
        resEv = self.__client.sendEnvelope(ev)
        if (
            "status" in resEv.bodies[0][1].body
            and resEv.bodies[0][1].body["status"] != 1
        ):
            return None
        battleCode = resEv.bodies[0][1].body
        return battleCode

    def finishHunting(
        self,
        character: Union[Character, int],
        bossNum: int,
        battleCode: str,
        user: User = None,
    ) -> Union[Dict[str, Any], None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if type(character) is Character:
            character = character.cid

        _hash = sha256(f"{bossNum}{character}{battleCode}".encode())
        ev = self.__client.createEnvelope(
            target="HuntingHouse.finishHunting",
            body=[
                f"{character}",
                f"{bossNum}",
                battleCode,
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
        return resEv.bodies[0][1].body
