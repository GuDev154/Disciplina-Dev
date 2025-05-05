#Realizei a inclusão dos codigos da main para tests pois estava ocorrendo um erro na importação das funções criadas na main (src.main)
import random
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError
import pytest
from unittest.mock import patch

app = FastAPI()


class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/helloworld")
async  def root():
    return  {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,57000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0

@pytest.mark.asyncio
async def test_create_estudante_ativo():
    estudante_teste = Estudante(name="Maria", curso="Engenharia", ativo=True)
    result = await create_estudante(estudante_teste)
    assert result.name == "Maria"
    assert result.curso == "Engenharia"
    assert result.ativo is True

@pytest.mark.asyncio
async def test_create_estudante_invalido_tipo():
    with pytest.raises(ValidationError):
        # 'ativo' deve ser bool, aqui está como string
        Estudante(name="João", curso="Biologia", ativo="sim")

@pytest.mark.asyncio
async def test_update_estudante_zero():
    result = await update_estudante(0)
    assert not result  # 0 não é maior que 0

@pytest.mark.asyncio
async def test_delete_estudante_zero():
    result = await delete_estudante(0)
    assert not result

@pytest.mark.asyncio
async def test_funcaoteste_range():
    # Verifica se o número retornado está dentro do intervalo esperado
    result = await funcaoteste()
    assert 0 <= result["num_aleatorio"] <= 57000
