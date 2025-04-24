from fastapi import FastAPI
import random
import pydantic

app = FastAPI()

class Estudante(pydantic.BaseModal):
    nome: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async  def root():
    return  {"message": "Hello World"}

@app.get("/funcaoteste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,50000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0