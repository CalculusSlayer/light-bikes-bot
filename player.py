import requests

base = "http://light-bikes.inseng.net/"

class Game:
    def create(self, serverBotDifficulty):
        return requests.post(base + "games?addServerBot=true&boardSize=26&numPlayers=2&serverBotDifficulty=" + str(serverBotDifficulty))

    def joinGame(self, gameId, name):
        return requests.post(base + f"games/{gameId}/join?name={name}")

    def move(self, gameId, playerId, x, y):
        return requests.post(base + f"games/{gameId}/move?playerId={playerId}&x={x}&y={y}")

