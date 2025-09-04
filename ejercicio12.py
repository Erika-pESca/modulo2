"""
Ejercicio 12: Simulador de Lanzamiento de Dados
•	Crea un programa que simule el lanzamiento de dos dados 10,000 veces.
•	Usa un diccionario para contar la frecuencia de cada posible suma de los dados (de 2 a 12).
•	Al final, imprime un reporte con la frecuencia de cada suma.
Conceptos aplicados: random.randint(), bucles, diccionarios como contadores, método get().
"""

import random

def simulador_dados(intentos=10000):
    frecuencias = {}

    for _ in range(intentos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        # Usamos get() para sumar frecuencias
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    return frecuencias


def main():
    intentos = 10000
    resultados = simulador_dados(intentos)

    print(f"Resultados después de {intentos} lanzamientos:\n")
    for suma in range(2, 13):  # posibles resultados 2 - 12
        print(f"Suma {suma}: {resultados.get(suma, 0)} veces")


if __name__ == "__main__":
    main()
