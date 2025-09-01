"""
Ejercicio 9: Transformación de Datos con Dictionary Comprehensions
Tienes una lista de productos, donde cada producto es un diccionario: [{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]:
•	Usa una dictionary comprehension para crear un nuevo diccionario donde los nombres de los productos sean las claves y los precios con un 19% de IVA incluido sean los valores.

"""

productos = [
    {"nombre": "Camisa", "precio": 50000},
    {"nombre": "Pantalón", "precio": 80000}
]
def main():
    print("---" * 15)
    productos_iva = valor_iva()
    print("Sus productos con IVA son: ")
    print("---" * 15)
    for nombre, precio in productos_iva.items():
        print(f"{nombre}: {precio:.0f}")




def valor_iva ():
    """
    ejecuta en diccionario con su clave y valor
        args: for p in productos: recorre cada producto de la lsita
        p["nombre"] → se usa como clave.

        p["precio"] * 1.19 → precio con IVA (precio + 19%).

        Se recorre la lista productos con for p in productos.
    """
    productos_iva = {p["nombre"]: p["precio"]*1.19 for p in productos}
    return productos_iva

if __name__ == "__main__":
    main()