import pytest
from ejercicio12 import simulador_dados

def test_resultados_son_diccionario():
    # Verifica que la función devuelve un diccionario
    resultado = simulador_dados(1000)
    assert isinstance(resultado, dict)

def test_claves_en_rango():
    # Todas las sumas deben estar entre 2 y 12
    resultado = simulador_dados(1000)
    for clave in resultado.keys():
        assert 2 <= clave <= 12

def test_total_intentos():
    # La suma de todas las frecuencias debe ser igual al número de intentos
    intentos = 5000
    resultado = simulador_dados(intentos)
    total = sum(resultado.values())
    assert total == intentos

def test_valores_positivos():
    # Todas las frecuencias deben ser mayores que 0
    resultado = simulador_dados(2000)
    for frecuencia in resultado.values():
        assert frecuencia > 0
