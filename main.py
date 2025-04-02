from fastapi import FastAPI
import random
from pydantic import BaseModal

app = FastAPI()

class Estudante(BaseModal):
    name: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async  def root():
    return  {"message": "Hello World"}

@app.get("/funcaoteste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,20000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_item(id_estudante: int):
    return id_estudante > 0