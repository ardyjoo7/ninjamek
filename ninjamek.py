from playninjalegends import NinjaLegendsAPI
import time

print("")
username = input("Username : ")
password = input("Password : ")
lvlmission = int(input("Level Mission : "))
print("")
nlapi = NinjaLegendsAPI(username=username, password=password)

allChar = nlapi.systemLogin.getAllCharacters()
char = nlapi.systemLogin.getCharacterData(allChar[0].cid)

missionId = lvlmission

while True:
    try:
        bc = nlapi.battleSystem.startMission(char, missionId)
        res = nlapi.battleSystem.finishMission(char, missionId, bc)
        dat = nlapi.systemLogin.getCharacterData(allChar[0].cid)
        print("Level :",res["level"], "|| XP :",res["xp"], "|| Gold :",dat.gold)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"[!] Got Error", e)