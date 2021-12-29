from playninjalegends import NinjaLegendsAPI


nlapi = NinjaLegendsAPI(username='xxx', password='xxx')

allChar = nlapi.systemLogin.getAllCharacters()
char = nlapi.systemLogin.getCharacterData(allChar[0].cid)
res = nlapi.huntingHouse.getData(char)
print(res)

for i, val in enumerate(res['data'].split(',')):
    for _ in range(int(val)):
        bc = nlapi.huntingHouse.startHunting(char, i)
        print(nlapi.huntingHouse.finishHunting(char, i, bc))
