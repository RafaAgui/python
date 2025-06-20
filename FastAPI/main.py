from fastapi import FastAPI
from typing import Union

app = FastAPI()

# Debemos decorar el método y un endpoint
@app.get("/")
#creamos un método que se llama metodoRoot
def metodoRoot():
    return {"data": "FastAPI is working!"}

@app.get("/hello")
def hello_world():
    return {"message": "Hello, World!"}

# Recibe datos por mapping
@app.get("/numero/{numero}")
def getNumeroDoble(numero: int):
    doble: int = numero * 2
    return {"numero": numero, "doble": doble}

# Recibe datos por query
@app.get("/saludito")
def saludito(nombre: str):
    return {"mensaje": "Hola," + nombre}

# Recibe datos opcionales por query con varios parametros
@app.get("/union")
def union(nombre: str, apellido: Union[str, None] = None):
    return {"mensaje": "Hola," + nombre + " " + (apellido if apellido else "")}