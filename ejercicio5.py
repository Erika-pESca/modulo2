"""
ejercicio 5 Crea un programa que pida un número y, usando un operador ternario,
asigne a una variable el texto "Par" o "Impar". Luego, imprime el resultado. Adicionalmente,
si el número es múltiplo de 5, debe imprimir un mensaje extra.
"""
def main ():
    numero=int(input("Ingrese un numero: "))
    validar_par_impar(numero)

def validar_par_impar(numero):
    """
    la funcion valida si el nunero ingresado es par o impar y adicional verefica si es multiplico de 5
    Args:
        param numero: numero ingresado

    """
    if numero % 2 == 0:
        print("El numero es par")
        if numero %5 ==0:
         print("Además, el número es múltiplo de 5.")
    else :
        print("El numero es impar")
        if numero %5 ==0:
            print("Además, el número es múltiplo de 5.")

if __name__ == "__main__":
    main()