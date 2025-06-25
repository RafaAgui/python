import json
from models.player import Player

def getPlayers():
    info = open("./data/jugadores.json")
    data = json.load(info)
    #creamos una lista de jugadores
    salida = []
    #recorremos los jugadores
    for row in data["jugadores"]:
        player = Player()
        player.numero = int(row["numero"])
        player.nombre = row["nombre"]
        player.edad = int(row["edad"])
        player.posicion = row["posicion"]
        # player.imagen = row["imagen"]
        salida.append(player)
    return salida

def findPlayer(numero: int):
    info = open("./data/jugadores.json")
    data = json.load(info)
    for player in data["jugadores"]:
        if player["numero"] == numero:
            player = Player()
            player.numero = int(player["numero"])
            player.nombre = player["nombre"]
            player.edad = int(player["edad"])
            player.posicion = player["posicion"]
            return player