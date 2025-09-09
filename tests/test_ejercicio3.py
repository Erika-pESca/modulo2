import pytest
from ejercicio3 import validar_contraseña

def test_contraseña_valida():
    # Cumple todos los requisitos: >= 8, tiene mayúscula, tiene número
    resultado = validar_contraseña("Password1")
    assert resultado == []  # no hay errores

def test_contraseña_corta():
    # Menos de 8 caracteres
    resultado = validar_contraseña("Pas1")
    assert "La contraseña debe tener al menos 8 caracteres." in resultado

def test_contraseña_sin_mayuscula():
    # No tiene mayúsculas
    resultado = validar_contraseña("password1")
    assert "La contraseña debe contener al menos una letra mayúscula." in resultado

def test_contraseña_sin_numero():
    # No tiene número
    resultado = validar_contraseña("Password")
    assert "La contraseña debe contener al menos un número." in resultado

def test_contraseña_varios_errores():
    # Corta, sin mayúscula y sin número
    resultado = validar_contraseña("abc")
    assert "La contraseña debe tener al menos 8 caracteres." in resultado
    assert "La contraseña debe contener al menos una letra mayúscula." in resultado
    assert "La contraseña debe contener al menos un número." in resultado
    assert len(resultado) == 3
