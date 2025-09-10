# test_juego.py
import builtins #acceso a print(), len(), str()y range()
import random
import pytest
from ejercicio4 import juego

def test_usuario_gana_con_piedra(monkeypatch):
    # Simulamos que el usuario escribe "piedra" y el PC juega "tijeras"
    inputs = iter(["piedra", "piedra", "piedra"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras") #El nombre de la función a reemplazar.

    # Ejecutamos el juego (terminará cuando usuario gane 3 veces)
    juego()

def test_pc_gana_con_papel(monkeypatch):
    # Simulamos que el usuario siempre juega "piedra" y el PC siempre "papel"
    inputs = iter(["piedra", "piedra", "piedra"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda _: "papel")

    juego()

def test_empate(monkeypatch, capsys):
    # Simulamos jugadas iguales, pero limitamos la cantidad de entradas
    inputs = iter(["tijeras", "tijeras", "tijeras"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras")


    try:
        juego()
    except StopIteration: #para que el iterador se quede sin elementos
        pass  # Se acaba porque ya no hay más jugadas simuladas

    # Capturamos la salida del programa
    salida = capsys.readouterr().out

    # Verificamos que haya habido empates
    assert "empate" in salida

def test_opcion_invalida(monkeypatch):
    # Primero mete una opción inválida, luego una válida
    inputs = iter(["invalido", "piedra", "piedra", "piedra", "piedra"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    monkeypatch.setattr(random, "choice", lambda _: "tijeras")

    juego()
