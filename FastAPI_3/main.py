from fastapi import FastAPI

app = FastAPI()

# Debemos decorar el método y un endpoint
@app.get("/")
#creamos un método que se llama metodoRoot
def metodoRoot():
    return {"data": "FastAPI is working!"}