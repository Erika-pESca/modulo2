# test_ejercicio5.py
import pytest
from ejercicio5 import validar_par_impar

def test_par_no_multiplo5(capsys):
    validar_par_impar(8)  # número par pero no múltiplo de 5
    salida = capsys.readouterr().out # captura y almacenar cualquier texto que el código imprime
    assert "El numero es par" in salida
    assert "múltiplo de 5" not in salida

def test_par_multiplo5(capsys):
    validar_par_impar(10)  # número par y múltiplo de 5
    salida = capsys.readouterr().out
    assert "El numero es par" in salida
    assert "múltiplo de 5" in salida

def test_impar_no_multiplo5(capsys):
    validar_par_impar(7)  # número impar pero no múltiplo de 5
    salida = capsys.readouterr().out
    assert "El numero es impar" in salida
    assert "múltiplo de 5" not in salida

def test_impar_multiplo5(capsys):
    validar_par_impar(15)  # número impar y múltiplo de 5
    salida = capsys.readouterr().out
    assert "El numero es impar" in salida
    assert "múltiplo de 5" in salida
