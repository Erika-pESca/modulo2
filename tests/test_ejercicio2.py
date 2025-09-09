import pytest
from ejercicio2 import guardar, cargar, salir, lista

# Prueba guardar con texto válido
def test_guardar_valido(monkeypatch, capsys):# remplaza y captura lo que se emprime en la consola
    # remplaza la entrada de usuario
    monkeypatch.setattr('builtins.input', lambda _: "Hola mundo") #funcion anonima y el _  indicar que un valor de una variable es intencionalmente ignorado o no se va a usar

    guardar()

    captured = capsys.readouterr() #temporalmente
    assert "Hola mundo" in lista                # se guardó en la lista
    assert "Hola mundo fue guardado" in captured.out  # mensaje correcto


# Prueba guardar con texto vacío (primero vacío, luego válido)
def test_guardar_vacio(monkeypatch, capsys):# remplaza y captura lo que se emprime en la consola
    inputs = iter(["   ", "holiii"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    guardar()

    captured = capsys.readouterr()
    assert "no puedes guardar nada vacio" in captured.out
    assert "holiii" in lista


# Prueba cargar cuando hay elementos
def test_cargar_con_datos(capsys):
    lista.clear()
    lista.extend(["dato1", "dato2"])

    cargar()

    captured = capsys.readouterr()
    assert "1. dato1" in captured.out
    assert "2. dato2" in captured.out


# Prueba cargar con lista vacía
def test_cargar_sin_datos(capsys):
    lista.clear()

    cargar()

    captured = capsys.readouterr()
    assert "La lista esta vacia" in captured.out


# Prueba salir
def test_salir(capsys):
    salir()
    captured = capsys.readouterr()
    assert "Saliendo" in captured.out
