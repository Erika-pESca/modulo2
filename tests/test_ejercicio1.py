import pytest
from ejercicio1 import pedir_edad, pedir_estudiante, calcular_precio

# prueba de logica
def test_nino():
    # Prueba para un niño sin descuento
    assert calcular_precio(10, "no") == 10000
    # Prueba para un niño con descuento de estudiante
    assert calcular_precio(8, "si") == 9000


def test_adolescente():
    # Prueba para un adolescente sin descuento
    assert calcular_precio(12, "no") == 15000
    # Prueba para un adolescente con descuento de estudiante
    assert calcular_precio(17, "si") == 13500


def test_adulto():
    # Prueba para un adulto sin descuento
    assert calcular_precio(30, "no") == 20000
    # Prueba para un adulto con descuento de estudiante
    assert calcular_precio(22, "si") == 18000


#Pruebas con Validaciones

def test_pedir_edad_valida(monkeypatch): # remplaza un valor en el input temporalmente para validar el test
    """Prueba que pedir_edad retorna un valor válido."""
    # Simula la entrada de "25"
    monkeypatch.setattr('builtins.input', lambda _: '25') #.setatrr-> se usa para estabablecer un valor en un atributo
    assert pedir_edad() == 25


def test_pedir_edad_invalida(monkeypatch, capsys):
    """Prueba que pedir_edad maneja entradas inválidas."""
    # Simula varias entradas: texto, fuera de rango, y finalmente una válida
    inputs = iter(['abc', '-10', '95', '30'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    edad = pedir_edad()

    captured = capsys.readouterr()
    assert "Ingresa solo números" in captured.out
    assert "La edad debe estar entre 0 y 90 años" in captured.out
    assert edad == 30


def test_pedir_estudiante_valido(monkeypatch):
    """Prueba que pedir_estudiante retorna 'si' o 'no'."""
    # Simula la entrada de "si"
    monkeypatch.setattr('builtins.input', lambda _: 'si')
    assert pedir_estudiante() == 'si'


def test_pedir_estudiante_invalido(monkeypatch, capsys):
    """Prueba que pedir_estudiante maneja entradas inválidas."""
    # Simula entradas como "quizas" y luego una válida "no"
    inputs = iter(['quizas', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    estudiante = pedir_estudiante()

    captured = capsys.readouterr()
    assert "Ingresa 'SI' o 'NO'." in captured.out
    assert estudiante == 'no'