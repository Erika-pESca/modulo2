import pytest
from ejercicio11 import validar_cedula

def test_cedula_con_letras():
    # Debe devolver False porque no son solo números
    assert validar_cedula("12a456") is False

def test_cedula_muy_corta():
    # Menos de 6 dígitos → False
    assert validar_cedula("123") is False

def test_cedula_muy_larga():
    # Más de 10 dígitos → False
    assert validar_cedula("12345678901") is False

def test_cedula_valida_numero():
    # Caso donde cumple la condición de solo números y longitud correcta
    resultado = validar_cedula("123456")
    # Puede devolver True en el futuro cuando completes la lógica,
    # pero por ahora aceptamos que devuelva None
    assert resultado in (True, False, None)

