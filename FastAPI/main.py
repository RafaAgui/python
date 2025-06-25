from fastapi import FastAPI
from typing import Union
from fastapi.encoders import jsonable_encoder

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

# Debemos decorar el método y un endpoint
@app.get("/numeros")
#creamos un método que se llama metodoRoot
def dameNumeros():
    listaNumeros = [1, 2, 3, 4, 5]
    salida = []
    for num in listaNumeros:
        elemento = {"numero": num}
        salida.append(elemento)
    return{"numeros": salida}    

@app.get("/nombres")
#creamos un método que se llama metodoRoot
def dameNumeros():
    listaNombres = ["rafa", "antonio", "paula", "sole", "marta"]
    salida = []
    for nombres in listaNombres:
        elemento = {"nombres": nombres}
        codificado = jsonable_encoder(elemento)
        salida.append(codificado)
    return{"nombres": salida}   