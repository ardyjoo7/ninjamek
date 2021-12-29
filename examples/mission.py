from playninjalegends import NinjaLegendsAPI


nlapi = NinjaLegendsAPI(username='xxx', password='xxx')

allChar = nlapi.systemLogin.getAllCharacters()
char = nlapi.systemLogin.getCharacterData(allChar[0].cid)

missionId = 11

while True:
    try:
        bc = nlapi.battleSystem.startMission(char, missionId)
        res = nlapi.battleSystem.finishMission(char, missionId, bc)
        print(res)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"[!] Got Error", e)
