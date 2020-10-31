import json

loadedGameData = {}
gameMap = []
symbols = {
}
spawnLocation = []

playerLocation = []
pastLocation = []

playerStatus = {
    "DEAD": False
}

with open("mapFile.json", 'r') as f:
    loadedGameData = json.load(f)

symbols = loadedGameData["mapSymbols"]

for row in loadedGameData["map"]:
    gameMap.append(list(row))

for x,row in enumerate(gameMap):
    for y,symbol in enumerate(row):
        if gameMap[x][y] == symbols["Spawn Location"]:
            spawnLocation = [x,y]

gameMap[spawnLocation[0]][spawnLocation[1]] = symbols["Player"]
playerLocation = spawnLocation

# Collision detection
def isBlocked (wantedCoords=[]):
    if gameMap[wantedCoords[0]][wantedCoords[1]] == "|" or gameMap[wantedCoords[0]][wantedCoords[1]] == "-":
        return True
    else:
        return False

def update():
    global pastLocation
    if loadedGameData["map"][pastLocation[0]][pastLocation[1]] != symbols["Spawn Location"] and loadedGameData["map"][pastLocation[0]][pastLocation[1]] != symbols["Player"]:
        gameMap[pastLocation[0]][pastLocation[1]] = loadedGameData["map"][pastLocation[0]][pastLocation[1]]
    else:
        gameMap[pastLocation[0]][pastLocation[1]] = " "
    if playerStatus["DEAD"] == False and loadedGameData["map"][playerLocation[0]][playerLocation[1]] == symbols["Death"]:
        playerStatus["DEAD"] = True
        gameMap[playerLocation[0]][playerLocation[1]] = symbols["Spawn Location"]
    else:
        gameMap[playerLocation[0]][playerLocation[1]] = symbols["Player"]



# Movement engine
while True:
    for row in gameMap:
        print("".join(row))
    if playerStatus["DEAD"] == True:
        print("Player is DEAD")
        break
    direction = input(">")
    direction = direction.lower()
    if direction == "w":
        pastLocation = playerLocation
        print([playerLocation[0] + 1, playerLocation[1]])
        if not isBlocked([playerLocation[0] - 1, playerLocation[1]]):
            playerLocation = [playerLocation[0] - 1, playerLocation[1]]
            update()
    if direction == "a":
        pastLocation = playerLocation
        if not isBlocked([playerLocation[0], playerLocation[1] - 1]):
            playerLocation = [playerLocation[0], playerLocation[1] - 1]
            update()
    if direction == "s":
        pastLocation = playerLocation
        if not isBlocked([playerLocation[0] + 1, playerLocation[1]]):
            playerLocation = [playerLocation[0] + 1, playerLocation[1]]
            update()
    if direction == "d":
        pastLocation = playerLocation
        if not isBlocked([playerLocation[0], playerLocation[1] + 1]):
            playerLocation = [playerLocation[0], playerLocation[1] + 1]
            update()