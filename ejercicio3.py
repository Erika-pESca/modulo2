"""
ejercicio 3  validador de contraseñas, Escribe un programa que pida al usuario crear una contraseña
y la valide usando un bucle while. El bucle solo terminará cuando la contraseña cumpla todos los criterios:
"""
def main():
    print("Crea una contraseña que cumpla con los siguientes requisitos:")
    print("- Mínimo 8 caracteres de longitud.")
    print("- Al menos una letra mayúscula.")
    print("- Al menos un número.\n")

    while True:
        contraseña = input("Ingrese su contraseña: ")
        lista_errores = validar_contraseña(contraseña) # llama a la funcion para ver si la contaseña cum´ple con lo requerido

        if not lista_errores:  # si no hay errores
            print("Contraseña creada exitosamente.")
            break
        else:
            print("La contraseña no cumple con los siguientes requisitos:")
            for i, error in enumerate(lista_errores, start=1):# entra a la lista y enumera y verifica cada error
                print(f"{i}. {error}")
            print("Intenta nuevamente.\n")

def validar_contraseña(contraseña):
    """
    lista_errores: lista de errores vacia
    (len)= cuenta cuantos caracteres debe tener la contraseña

    :params
     - (el for c in contraseña) recorre cada caracter de la contraseña
     - c.isupper() devuelve true si es un caractaer de la contraseña tiene mayusculas y
     -(any) devuelve true si almenos tiene un valor mayuscula
     -(isdigit) devuelve true si un caracter es un numero
    """
    lista_errores = []  # lista de errores vacía
    if len(contraseña) < 8: #(len) ceunta cuantos caracteres debe tener
        lista_errores.append("La contraseña debe tener al menos 8 caracteres.")
    if not any(c.isupper() for c in contraseña): # el for c in contraseña recorre cada caracter de la contraseña
        lista_errores.append("La contraseña debe contener al menos una letra mayúscula.")
    if not any(c.isdigit() for c in contraseña):
        lista_errores.append("La contraseña debe contener al menos un número.")

    return lista_errores
if __name__ == "__main__":
    main()