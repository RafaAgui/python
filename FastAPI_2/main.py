from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

import json

app = FastAPI()

@app.get("/players")
def readPlayers():
    info = open("./data/jugadores.json")
    data = json.load(info)
    #creamos una lista de jugadores
    salida = []
    #recorremos los jugadores
    for row in data["jugadores"]:
        item = jsonable_encoder(row)
        salida.append(item)  
    return{"players": salida}


### hacemos lo mismo pero con BaseMOdel
import services.ServicesJugadores as services

@app.get("/players2")
def readPlayers():
    players = services.getPlayers()
    return{"players": players}

@app.get("/players/{numero}")
def findPlayer(numero: int):
    player = services.findPlayer(numero)
    return  player
    # if player:
    #     return {"player": player}
    # else:
    #     return {"error": "Player not found"}