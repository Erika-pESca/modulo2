import pytest
from ejercicio13 import aventura

def test_camino_perder(monkeypatch, capsys):
    # Simulamos que el jugador escribe "ir al este" para caer en la trampa
    inputs = iter(["ir al este"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    aventura()
    salida = capsys.readouterr().out
    assert "GAME OVER" in salida
    assert "Gracias por jugar" in salida

def test_ganar_aventura(monkeypatch, capsys):
    # Camino para ganar:
    # 1. ir al norte (tesoro)
    # 2. ir al oeste (llave)
    # 3. tomar llave
    # 4. ir al este (volver al tesoro)
    # 5. abrir cofre (ganar)
    inputs = iter(["ir al norte", "ir al oeste", "tomar llave", "ir al este", "abrir cofre"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    aventura()
    salida = capsys.readouterr().out
    assert "GANASTE" in salida
    assert "Gracias por jugar" in salida

def test_accion_invalida(monkeypatch, capsys):
    # Camino donde se ingresa una acción inválida primero
    inputs = iter(["saltar", "ir al este"])  # "saltar" es inválido, luego cae en trampa
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    aventura()
    salida = capsys.readouterr().out
    assert "No entiendo esa acción" in salida
    assert "GAME OVER" in salida
