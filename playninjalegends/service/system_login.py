from typing import List, Union

from ..store import Character, User
from ..utils import AMFClient


class SystemLogin:
    __client: AMFClient
    user: User

    def __init__(self, client: AMFClient, user: User) -> None:
        self.__client = client
        self.user = user

    def getAllCharacters(self, user: User = None) -> Union[List[Character], None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        ev = self.__client.createEnvelope(
            "SystemLogin.getAllCharacters", body=[user.AccountID, user.SessionKey]
        )
        resEv = self.__client.sendEnvelope(ev)
        if (
            "status" in resEv.bodies[0][1].body
            and resEv.bodies[0][1].body["status"] != 1
        ):
            return None
        chars = []
        for char in resEv.bodies[0][1].body["account_data"]:
            chars.append(Character(char))
        return chars

    def getCharacterData(
        self, characterId: int, user: User = None
    ) -> Union[Character, None]:
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        ev = self.__client.createEnvelope(
            "SystemLogin.getCharacterData", body=[f"{characterId}", user.SessionKey]
        )
        resEv = self.__client.sendEnvelope(ev)
        if (
            "status" in resEv.bodies[0][1].body
            and resEv.bodies[0][1].body["status"] != 1
        ):
            return None
        char = Character(resEv.bodies[0][1].body)
        char.cid = characterId
        return char
