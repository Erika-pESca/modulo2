"""
ejercicio 2 Desarrolla un programa que simule un menú de consola
 usando la estructura match-case. El programa mostrará una lista de
comandos disponibles ("guardar", "cargar", "salir") y el usuario ingresará uno
"""
lista = []


def main():
    while True:
        print("\n--- MENÚ DE COMANDOS ---")
        print("1. guardar")
        print("2. cargar")
        print("3. salir")

        comandos = input("Ingrese un comando: ").lower().strip() #convierte en minusculas y sin espacios

        match comandos:
            case "guardar" | "1":
                guardar()
            case "cargar" | "2":
                cargar()
            case "salir" | "3":
                salir()
                break
            case _:
                print("comando no reconocido")

#funcion para guardar
def guardar():
    while True:
        texto = input("Ingrese el texto que desea guardar: ")
        if not texto.strip():
            print("no puedes guardar nada vacio, porfavor ingrese un texto que desea guardar")
        else:
            lista.append(texto)
            print(f"el {texto} fue guardado correctamente")
            break

#funcion para cargar
def cargar():
    if lista:
        print("Lista de guardados")
        for i, texto in enumerate(lista, start=1): #recorre la lista y la enumera
            print(f"{i}. {texto}")
    else:
        print("La lista esta vacia")

#funcion para salir
def salir():
    print("Saliendo")

if __name__ == "__main__":
    main()