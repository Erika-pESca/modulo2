"""
Ejercicio 8: Filtrado de Datos con List Comprehensions
Dada una lista de números [-5, 10, -15, 20, -25, 30], utiliza una list comprehension para crear tres nuevas listas:
•	Una lista con solo los números positivos.
•	Una lista con los cuadrados de todos los números.
•	Una lista de strings que diga "positivo" o "negativo" para cada número, usando un ternario dentro de la comprensión.
•	Conceptos aplicados: List comprehensions, operador ternario.
"""
lista = [-5, 10, -15, 20, -25, 30]


def main():
    print("---"*17)
    print(f"tienes una lista con : {lista}")
    print("---"*17)
    numeros_positivos, numeros_negativos, cuadrados = lista_nuevas()
    print("Los números positivos de tu lista son:")
    print(numeros_positivos)

    print("los numeros negativos de tu lista son:")
    print(numeros_negativos)

    print("los cuadrados de tu lista son:")
    print(cuadrados)


def lista_nuevas():
    """
    ejecuta el list comprehension para crear nuevas listas
        Args:
        for n in lista → recorre cada número de la lista.

       if n > 0 → filtra solo los que son positivos.

       n → lo que se guarda en la nueva lista.
    """
    numeros_positivos = [n for n in lista if n > 0]
    numeros_negativos = [n for n in lista if n < 0]
    cuadrados= [n ** 2 for n in lista]
    return numeros_positivos, numeros_negativos, cuadrados



if __name__ == "__main__":
    main()
