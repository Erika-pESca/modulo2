import pytest
from ejercicio9 import valor_iva

def test_valor_iva_diccionario():
    productos_iva = valor_iva()
    assert isinstance(productos_iva, dict)  # Debe devolver un diccionario

def test_valor_iva_camisa():
    productos_iva = valor_iva()
    # 50000 + 19% = 59500
    assert productos_iva["Camisa"] == 50000 * 1.19

def test_valor_iva_pantalon():
    productos_iva = valor_iva()
    # 80000 + 19% = 95200
    assert productos_iva["Pantalón"] == 80000 * 1.19

def test_valor_iva_cantidad_claves():
    productos_iva = valor_iva()
    # Debe tener el mismo número de claves que la lista original
    assert len(productos_iva.keys()) == 2
