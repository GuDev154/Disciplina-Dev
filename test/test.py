
from main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello World"}


def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Fulano", curso ="Curso 1", ativo=False)
    assert estudante_teste == create_estudante()

def test_update_estudante_negativo(id_estudante: int):
    assert not update_estudante(-5)

def test_update_estudante_positivo(id_estudante: int):
    assert update_estudante(10)


def test_delete_estudante_negativo(id_estudante: int):
    assert not update_estudante(-5)

def test_delete_estudante_positivo(id_estudante: int):
    assert update_estudante(5)