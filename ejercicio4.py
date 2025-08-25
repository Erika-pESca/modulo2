"""
ejercicio 4 Juego de Piedra, Papel o Tijeras
Implementa el clásico juego para jugar contra la computadora.
•	El usuario elige una opción y la computadora elige una al azar.
•	El programa determina el ganador basándose en las reglas (piedra vence a tijeras, tijeras a papel, papel a piedra).
•	Se debe llevar un conteo de las victorias del jugador y de la computadora. El juego termina cuando uno de los dos llegue a 3 victorias.

"""
import random
def main():
 juego()
def juego():
    """
    Args: victorias_usuario y victorias_pc son contadores que cuenta cuantas rondas ha ganado
    -opciones: lista con las jugada que puede hacer el computador
    """
    victorias_usuario = 0
    victorias_pc = 0

    opciones = ["piedra", "papel", "tijeras"]

    while victorias_usuario < 3 and victorias_pc < 3:
        print("---"*10)
        print("JUEGO DE PIEDRA PAPEL Y TIJERAS")
        print("---" *10)
        print("1. papel")
        print("2. tijeras")
        print("3. piedra")

        comandos = input("escoja la opcion que desea jugar: ").lower().strip()

        match comandos:
            case "1" | "papel":
                jugada_usuario = "papel"
            case "2" | "tijeras":
                jugada_usuario = "tijeras"
            case "3" | "piedra":
                jugada_usuario = "piedra"
            case _:
                print("Opción inválida, intente nuevamente.")
                continue

        jugada_pc = random.choice(opciones) # random.choice para que el computador eloja aleatoriamnete entre las opciones que tiene
        print(f"elegiste {jugada_usuario} y tu computadora eligio {jugada_pc}")

        if jugada_usuario == jugada_pc:
            print("empate")
        elif (jugada_usuario == "piedra" and jugada_pc == "tijeras") or \
             (jugada_usuario == "tijeras" and jugada_pc == "papel") or \
             (jugada_usuario == "papel" and jugada_pc == "piedra"):
            victorias_usuario += 1
            print(f"Ganaste la primera {victorias_usuario}")

        else:
            victorias_pc += 1
            print(f"tu computador gana esta ronda {victorias_pc}")


    if victorias_usuario == 3:
        print("felicidades ganaste")
    else:
        print("tu computadora gano, suerte para la aproxima")

if __name__ == "__main__":
    main()