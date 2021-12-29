# example for using API without providing username and password

from playninjalegends import NinjaLegendsAPI

nlapi = NinjaLegendsAPI()



user = nlapi.loginUser(username="xxx", password="xxx")
allChar = nlapi.systemLogin.getAllCharacters(user=user)

char = nlapi.systemLogin.getCharacterData(allChar[0].cid, user=user)

