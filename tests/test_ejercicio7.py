import pytest
from ejercicio7 import cantidad_estudiantes, validar_nombres_notas

# cantidad_estudiantes
def test_cantidad_estudiantes_valido(monkeypatch):
    inputs = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert cantidad_estudiantes() == 3

def test_cantidad_estudiantes_vacio_luego_valido(monkeypatch):
    inputs = iter(["", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert cantidad_estudiantes() == 2

def test_cantidad_estudiantes_invalido_luego_valido(monkeypatch):
    inputs = iter(["abc", "0", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert cantidad_estudiantes() == 4


# validar_nombres_notas
def test_validar_nombres_notas_valido(monkeypatch):
    nombres, notas = [], []
    inputs = iter(["Ana", "4.5", "Luis", "3.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    validar_nombres_notas(nombres, notas, 2)

    assert nombres == ["Ana", "Luis"]
    assert notas == [4.5, 3.0]

def test_validar_nombres_notas_nombre_vacio(monkeypatch):
    nombres, notas = [], []
    inputs = iter(["", "Carlos", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    validar_nombres_notas(nombres, notas, 1)

    assert nombres == ["Carlos"]
    assert notas == [5.0]

def test_validar_nombres_notas_nota_invalida(monkeypatch):
    nombres, notas = [], []
    inputs = iter(["Maria", "", "10", "abc", "4.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    validar_nombres_notas(nombres, notas, 1)

    assert nombres == ["Maria"]
    assert notas == [4.0]
