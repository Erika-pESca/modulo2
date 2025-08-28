"""
ejercico 7  Combinador de Listas con zip
Dadas dos listas, una con nombres de estudiantes y otra con sus respectivas notas finales, crea una función que las combine
para generar un diccionario. Las claves serán los nombres y los valores las notas:
Luego, itera sobre el diccionario resultante para imprimir un reporte del tipo: "El estudiante [Nombre] tiene una nota de [Nota]".
"""



def main():
    nombres = []
    notas = []

    cantidad = cantidad_estudiantes()
    validar_nombres_notas(nombres, notas, cantidad)
    estudiantes = dict(zip(nombres, notas))

    # Reporte
    print("\n--- Reporte de Estudiantes ---")
    for nombre, nota in estudiantes.items(): #(items) devuelve pares clave y valor del diccionario
        print(f"El estudiante {nombre} tiene una nota de {nota}")


def cantidad_estudiantes():
    """
    pregunta la cintidad de estudiantes que desea ingresar

        Params:
            input: cantidad de estudiantes
            int: lo covierte a entero
            return estd: entrega ese numero a quien llame la funcion
    """
    while True:
        try:
            entrada = input("Ingrese la cantidad de estudiantes que desea agregar: ").strip()

            if not entrada:  # si el usuario no escribió nada (cadena vacía)
                print("No puede dejar el campo vacío.")
                continue

            estd = int(entrada)  # convertimos a número

            if estd > 0:
                return estd
            else:
                print("La cantidad debe ser un número mayor que 0.")

        except ValueError:
            print("Error: debe ingresar un número válido.")


def validar_nombres_notas(nombres, notas, cantidad):
    """
    digita los valores que desea ingresar
    Params:
        for: repite la cantidad de veces que desea ingresar
        nombre: pide el nombre del estudiante
        nota: nota del estudiante
    """
    for i in range(cantidad):
        while True:
            nombre = input(f"Ingrese el nombre del estudiante {i + 1}: ")
            if nombre:
                break
            else:
                print("el nombre no puede quedar vacio ")

        while True:
            nota = input(f"Ingrese la nota de {nombre} (0 a 5): ").strip()
            if not nota:
                print("el nota no puede quedar vacio ")
                continue

            try:
                nota=float(nota)
                if nota>0 and nota<=5:
                    break
                else:
                    print("la nota debe estar entre 0 y 5")
            except ValueError:
                print("la nota debe ser un numero valido")


        nombres.append(nombre)
        notas.append(nota)


if __name__ == "__main__":
    main()