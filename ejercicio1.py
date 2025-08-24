"""
Ejercicio 1 Crea un programa que calcule el precio de una entrada de cine
basándose en la edad del cliente y si es estudiante.
"""

def main():
    edad = pedir_edad()
    estudiante = pedir_estudiante()

    # Llamar a la función que calcula el precio
    total = calcular_precio(edad, estudiante)
    print(f"Su entrada tiene un costo de: ${total:,.0f}")


# Función para pedir la edad
def pedir_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if 0 <= edad <= 90:
                return edad
            else:
                print("La edad debe estar entre 0 y 90 años.")
        except ValueError:
            print("Ingresa solo números")

# Función para pedir si es estudiante
def pedir_estudiante():
    while True:
        tipo_persona = input("¿Eres estudiante? (si/no): ").lower()
        if tipo_persona in ["si", "no"]:
            return tipo_persona
        else:
            print("Ingresa 'SI' o 'NO'.")


# Función para calcular el precio
def calcular_precio(edad, es_estudiante):
    if edad < 12:
        precio = 10000
    elif edad <= 17:
        precio = 15000
    else:
        precio = 20000

    # Si es estudiante aplica 10% de descuento
    if es_estudiante == "si":
        precio *= 0.9

    return precio

if __name__ == "__main__":
    main()
