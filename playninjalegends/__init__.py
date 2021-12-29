from .service import Christmas2021Event, HuntingHouse, BattleSystem, SystemLogin, HuntingHouse, CharacterService
from .utils import AMFClient

from .storage import enemies, missions, calc_real_enemy_stat
from .storage import Enemy, Mission
from .store import User


class NinjaLegendsAPI:
    client: AMFClient
    battleSystem: BattleSystem
    systemLogin: SystemLogin
    huntingHouse: HuntingHouse
    christmas2021Event: Christmas2021Event
    characterService: CharacterService

    def __init__(self, username: str = None, password: str = None) -> None:
        self.client = AMFClient("https://playninjalegends.com/amf_nl/")

        user = None
        if username is not None and password is not None:
            user = self.loginUser(username, password)
            if user is None:
                raise Exception("Invalid username or password")

        self.systemLogin = SystemLogin(self.client, user)
        self.battleSystem = BattleSystem(self.client, user)
        self.huntingHouse = HuntingHouse(self.client, user)
        self.christmas2021Event = Christmas2021Event(self.client, user)
        self.characterService = CharacterService(self.client, user)

    def loginUser(self, username: str, password: str) -> User:
        ev = self.client.createEnvelope("SystemLogin.loginUser",
                                        [username, password])
        resEv = self.client.sendEnvelope(ev)
        if "status" in resEv.bodies[0][1].body and resEv.bodies[0][1].body["status"] != 1:
            return None
        return User(resEv.bodies[0][1].body)
