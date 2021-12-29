from typing import Dict, List, Union

from ..utils import AMFClient
from ..store import Element, User, Character


class CharacterService:
    __client: AMFClient
    user: User

    def __init__(self, client: AMFClient, user: User) -> None:
        self.__client = client
        self.user = user

    def setPoints(self, character: Union[Character, int], points: Union[List[int], Dict[Element, int]], user: User = None):
        if self.user is None and user is None:
            raise ValueError("user must be set")
        if user is None:
            user = self.user

        if type(character) == Character:
            character = character.cid

        if type(points) == dict:
            points = [points[Element.WIND], points[Element.FIRE],
                       points[Element.LIGHTNING], points[Element.WATER],
                       points[Element.EARTH], points[Element.NOELEMENT]]

        ev = self.__client.createEnvelope("CharacterService.setPoints", [
            character, user.SessionKey, *points])
        resEv = self.__client.sendEnvelope(ev)
        return resEv.bodies[0][1].body
