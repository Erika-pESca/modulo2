import pytest
from ejercicio14 import validar_entrada, jugar

def test_validar_entrada_valida():
    assert validar_entrada("a", set(), set()) == True

def test_validar_entrada_invalida_no_letra(capsys):
    assert validar_entrada("1", set(), set()) == False
    salida = capsys.readouterr().out
    assert "Ingresa solo una letra válida" in salida

def test_validar_entrada_repetida(capsys):
    letras_correctas = {"a"}
    assert validar_entrada("a", letras_correctas, set()) == False
    salida = capsys.readouterr().out
    assert "Ya intentaste esa letra" in salida

def test_perder_juego(monkeypatch, capsys):
    # Fuerzo la palabra secreta a "python"
    monkeypatch.setattr("ejercicio14.elegir_palabra", lambda: "python")

    # El jugador ingresa letras equivocadas para perder
    entradas = iter(["a", "b", "c", "d", "e", "f"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugar()
    salida = capsys.readouterr().out
    assert "Te quedaste sin vidas" in salida
    assert "python" in salida  # Debe mostrar la palabra secreta

def test_ganar_juego(monkeypatch, capsys):
    # Fuerzo la palabra secreta a "hi"
    monkeypatch.setattr("ejercicio14.elegir_palabra", lambda: "hi")

    # El jugador adivina las letras correctas
    entradas = iter(["h", "i"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    jugar()
    salida = capsys.readouterr().out
    assert "¡Felicidades!" in salida
