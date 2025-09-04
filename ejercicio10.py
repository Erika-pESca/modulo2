"""
Ejercicio 10: Transposición de una Matriz
Crea una función que reciba una matriz (lista de listas) y devuelva su transpuesta. La transpuesta se logra intercambiando filas por columnas.
•	Ejemplo: [[1, 2, 3], [4, 5, 6]] se convierte en [[1, 4], [2, 5], [3, 6]].
•	Resuelve este problema usando bucles for anidados y luego intenta resolverlo con una list comprehension anidada.
Conceptos aplicados: Listas anidadas (matrices), bucles anidados, list comprehensions anidadas.
"""



"""
Ejercicio 10: Transposición de una Matriz
Crea una función que reciba una matriz (lista de listas) y devuelva su transpuesta. La transpuesta se logra intercambiando filas por columnas.
•	Ejemplo: [[1, 2, 3], [4, 5, 6]] se convierte en [[1, 4], [2, 5], [3, 6]].
•	Resuelve este problema usando bucles for anidados.
Conceptos aplicados: Listas anidadas (matrices), bucles anidados.
"""


def main():
    matriz = [[1, 2, 3], [4, 5, 6]]
    print("original:", matriz)
    print("resultado:", bucles(matriz))


def bucles(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for j in range(columnas):       # Recorremos columnas
        nueva_fila = []
        for i in range(filas):      # Recorremos filas
            nueva_fila.append(matriz[i][j])
        resultado.append(nueva_fila)

    return resultado


if __name__ == "__main__":
    main()
