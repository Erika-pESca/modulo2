import pytest
from ejercicio8 import lista_nuevas

def test_lista_nuevas_positivos():
    positivos, negativos, cuadrados = lista_nuevas()
    assert positivos == [10, 20, 30]

def test_lista_nuevas_negativos():
    positivos, negativos, cuadrados = lista_nuevas()
    assert negativos == [-5, -15, -25]

def test_lista_nuevas_cuadrados():
    positivos, negativos, cuadrados = lista_nuevas()
    assert cuadrados == [25, 100, 225, 400, 625, 900]

def test_lista_nuevas_longitudes():
    positivos, negativos, cuadrados = lista_nuevas()
    # Los cuadrados deben tener la misma longitud que la lista original
    assert len(cuadrados) == 6
    # Positivos + Negativos deben sumar la longitud original
    assert len(positivos) + len(negativos) == 6
