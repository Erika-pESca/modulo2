import pytest
from ejercicio10 import bucles

def test_transpuesta_matriz_2x3():
    matriz = [[1, 2, 3], [4, 5, 6]]
    resultado = bucles(matriz)
    assert resultado == [[1, 4], [2, 5], [3, 6]]

def test_transpuesta_matriz_3x2():
    matriz = [[1, 2], [3, 4], [5, 6]]
    resultado = bucles(matriz)
    assert resultado == [[1, 3, 5], [2, 4, 6]]

def test_transpuesta_matriz_1x4():
    matriz = [[10, 20, 30, 40]]
    resultado = bucles(matriz)
    assert resultado == [[10], [20], [30], [40]]

def test_transpuesta_matriz_4x1():
    matriz = [[10], [20], [30], [40]]
    resultado = bucles(matriz)
    assert resultado == [[10, 20, 30, 40]]
