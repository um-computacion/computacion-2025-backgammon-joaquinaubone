"""Módulo CLI para el juego de Backgammon.

Contiene la función principal `jugar` que maneja la interacción
con el usuario a través de la línea de comandos.
"""
from game.game import Juego

def jugar(tablero, dados, jugador_blanco, jugador_negro):
    """Ejecuta el flujo principal del juego Backgammon desde la línea de comandos."""
    
    juego = Juego(tablero, dados, jugador_blanco, jugador_negro)

    while not juego.gano('B') and not juego.gano('N'):
        color = juego.obtener_jugador_actual().obtener_color()
        print(f"Turno del jugador {color}")

        dados.tirar()
        tirada = juego.interpretar_tirada()
        print(f"Dados: {tirada}")

        if not juego.hay_movimientos_posibles(color, tirada):
                print("No hay movimientos posibles. Pierdes el turno.")
                juego.cambiar_turno()
                continue
            

        while tirada:

            if not juego.hay_movimientos_posibles(color, tirada):
                print("No hay más movimientos posibles para los dados restantes.")
                break 

            print("\n📍 Estado actual del tablero:")
            tablero.mostrar()
            print(f"Valores disponibles: {tirada}")


            try:
                origen = int(input("Ingresá la casilla de origen (-1 si estás en barra): "))
                pasos = int(input("Ingresá la cantidad de pasos: "))

                if pasos not in tirada:
                    print("Ese valor no está en la tirada. Intentá con otro.")
                    continue

                if tablero.obtener_bar(color) and origen != -1:
                    print("Tenés fichas en la barra. Primero debés moverlas (origen = -1).")
                    continue

                juego.mover(origen, pasos)
                tirada.remove(pasos)

            except ValueError as e:
                print(f"Error: {e}")
                continue

        if juego.gano(color):
            color_ganador = color
            break

        juego.cambiar_turno()

    print(f"\n ¡El jugador {color_ganador} ha ganado!")
