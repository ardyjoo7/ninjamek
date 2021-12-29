from playninjalegends import NinjaLegendsAPI
from random import randint

nlapi = NinjaLegendsAPI(username='xxx', password='xxx')

allChar = nlapi.systemLogin.getAllCharacters()
char = nlapi.systemLogin.getCharacterData(allChar[0].cid)

energy = int(nlapi.christmas2021Event.getData(char)["energy"])
print(energy)
for _ in range(3):
    bossNum = randint(1, 6)
    bc = nlapi.christmas2021Event.startEvent(char, bossNum)
    res = nlapi.christmas2021Event.finishEvent(char, bossNum, bc)
    print(res)
