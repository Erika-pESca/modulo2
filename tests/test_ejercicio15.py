import builtins
import pytest
import ejercicio15


def run_juego(monkeypatch, capsys, inputs, barco):
    """Ejecuta el juego con entradas simuladas y un barco fijo"""
    inputs_iter = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs_iter))
    monkeypatch.setattr(ejercicio15, "colocar_barco", lambda: barco)

    ejercicio15.jugar()
    return capsys.readouterr().out


def test_crear_tablero():
    tablero = ejercicio15.crear_tablero()
    assert len(tablero) == 5
    assert all(len(fila) == 5 for fila in tablero)
    assert all(celda == "~" for fila in tablero for celda in fila)


def test_convertir_coordenada_valida():
    assert ejercicio15.convertir_coordenada("A1") == (0, 0)
    assert ejercicio15.convertir_coordenada("C3") == (2, 2)


def test_convertir_coordenada_invalida():
    assert ejercicio15.convertir_coordenada("Z9") is None
    assert ejercicio15.convertir_coordenada("11") is None
    assert ejercicio15.convertir_coordenada("") is None


def test_colocar_barco():
    barco = ejercicio15.colocar_barco()
    assert len(barco) == 3
    for fila, col in barco:
        assert 0 <= fila < 5
        assert 0 <= col < 5


def test_ganar(monkeypatch, capsys):
    barco = [(0, 0), (0, 1), (0, 2)]
    salida = run_juego(monkeypatch, capsys, ["A1", "A2", "A3"], barco)
    assert "¡Felicidades! Hundiste el barco." in salida


def test_perder(monkeypatch, capsys):
    barco = [(0, 0), (0, 1), (0, 2)]
    jugadas = ["B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "D3", "E1"]
    salida = run_juego(monkeypatch, capsys, jugadas, barco)
    assert "Te quedaste sin turnos" in salida


def test_disparo_repetido(monkeypatch, capsys):
    barco = [(0, 0), (0, 1), (0, 2)]
    jugadas = ["A1", "A1", "A2", "A3"]
    salida = run_juego(monkeypatch, capsys, jugadas, barco)
    assert "Ya disparaste aquí." in salida


def test_entrada_invalida(monkeypatch, capsys):
    barco = [(0, 0), (0, 1), (0, 2)]
    jugadas = ["Z9", "A1", "A2", "A3"]
    salida = run_juego(monkeypatch, capsys, jugadas, barco)
    assert "Entrada inválida" in salida
    assert "¡Felicidades! Hundiste el barco." in salida
