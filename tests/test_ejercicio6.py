import pytest
from ejercicio6 import encontrar_indices, validacion_frase, validacion_letra

# encontrar_indices
def test_encontrar_indices_existe():
    assert encontrar_indices("Hola SENA", "a") == [3, 8]

def test_encontrar_indices_no_existe():
    assert encontrar_indices("Hola", "z") == []

def test_encontrar_indices_mayus_minus():
    assert encontrar_indices("AaAa", "a") == [0, 1, 2, 3]


# validacion_frase
def test_validacion_frase_valida(monkeypatch):
    inputs = iter(["Hola mundo"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert validacion_frase("Ingrese una frase: ") == "Hola mundo"

def test_validacion_frase_vacia(monkeypatch):
    inputs = iter(["", "Hola"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert validacion_frase("Ingrese una frase: ") == "Hola"

def test_validacion_frase_caracteres_invalidos(monkeypatch):
    inputs = iter(["Hola123", "Hola"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert validacion_frase("Ingrese una frase: ") == "Hola"


# validacion_letra
def test_validacion_letra_valida(monkeypatch):
    inputs = iter(["a"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert validacion_letra("Ingrese una letra: ") == "a"

def test_validacion_letra_invalida(monkeypatch):
    inputs = iter(["12", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert validacion_letra("Ingrese una letra: ") == "b"

def test_validacion_letra_vacia(monkeypatch):
    inputs = iter(["", "c"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert validacion_letra("Ingrese una letra: ") == "c"
