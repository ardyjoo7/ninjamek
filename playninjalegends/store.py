from enum import Enum
from typing import Any, List, Dict


class User:
    SessionKey: str
    AccountID: str

    def __init__(self, data: Dict[str, Any]) -> None:
        self.AccountID = data["uid"]
        self.SessionKey = data["sessionkey"]

    def __repr__(self) -> str:
        return f"<User accountId={self.AccountID} sessionKey={self.SessionKey}>"


class Element(Enum):
    NOELEMENT: int = 0
    WIND: int = 1
    FIRE: int = 2
    LIGHTNING: int = 3
    WATER: int = 4
    EARTH: int = 5


class Gender(Enum):
    MALE: int = 0
    FEMALE: int = 1


class Character:
    cid: int
    name: str
    level: int
    xp: int
    gender: Gender
    rank: int
    elements: List[Element]
    gold: int
    tp: int
    attributes: Dict[Element, int]

    def __init__(self, data: Dict[str, Any]) -> None:
        charData = data
        if "character_data" in data:
            charData = data["character_data"]
        if "char_id" in data:
            self.cid = int(data["char_id"])
        if "character_points" in data:
            cp = data["character_points"]
            self.attributes = {}
            self.attributes[Element.WIND] = int(cp["atrrib_wind"])
            self.attributes[Element.FIRE] = int(cp["atrrib_fire"])
            self.attributes[Element.LIGHTNING] = int(cp["atrrib_lightning"])
            self.attributes[Element.WATER] = int(cp["atrrib_water"])
            self.attributes[Element.EARTH] = int(cp["atrrib_earth"])
        self.name = charData["character_name"]
        self.level = int(charData["character_level"])
        self.xp = int(charData["character_xp"])
        self.gender = Gender(int(charData["character_gender"]))
        self.rank = int(charData["character_rank"])
        self.elements = [
            Element(int(charData["character_element_1"])),
            Element(int(charData["character_element_2"])),
            Element(int(charData["character_element_3"])),
        ]
        self.gold = int(charData["character_gold"])
        self.tp = int(charData["character_tp"])

    def __repr__(self) -> str:
        return f"<Character ID={self.cid}>"
