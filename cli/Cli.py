"""Módulo CLI para el juego de Backgammon.

Contiene la función principal `jugar` que maneja la interacción
con el usuario a través de la línea de comandos.
"""
from game.game import Juego

def jugar(tablero, dados, jugador_blanco, jugador_negro):
    """Ejecuta el flujo principal del juego Backgammon desde la línea de comandos."""
    
    juego = Juego(tablero, dados, jugador_blanco, jugador_negro)

    while not juego.verificar_fin_del_juego():
        color = juego.obtener_jugador_actual().obtener_color()
        print(f"Turno del jugador {color}")

        dados.tirar()
        tirada = tablero.interpretar_tirada(*dados.obtener_valores())
        print(f"Dados: {tirada}")

        if not tablero.hay_movimientos_posibles(color, tirada):
            print("No hay movimientos posibles. Pierdes el turno.")
            juego.cambiar_turno()
            continue

        while tirada:
            print("\n📍 Estado actual del tablero:")
            tablero.mostrar()
            print(f"Valores disponibles: {tirada}")
            try:
                origen = int(input("Ingresá la casilla de origen (0 si estás en barra): "))
                pasos = int(input("Ingresá la cantidad de pasos: "))

                if pasos not in tirada:
                    print("Ese valor no está en la tirada. Intentá con otro.")
                    continue

                if tablero.obtener_bar(color) and origen != 0:
                    print("Tenés fichas en la barra. Primero debés moverlas (origen = 0).")
                    continue

                tablero.mover(origen, pasos, color)
                tirada.remove(pasos)

            except ValueError as e:
                print(f"Error: {e}")
                continue
        if tablero.gano(color):
            break

        juego.cambiar_turno()

    print(f"\n ¡El jugador {juego.obtener_jugador_actual().obtener_color()} ha ganado!")
