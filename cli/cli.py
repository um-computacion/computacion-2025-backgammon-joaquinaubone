"""Módulo CLI para el juego de Backgammon.

Contiene la función principal `jugar` que maneja la interacción
con el usuario a través de la línea de comandos.
"""
from core.game import Juego
from exceptions import PosicionInvalida

def jugar(juego):
    """Ejecuta el flujo principal del juego Backgammon desde la línea de comandos."""
    
    color_ganador = None

    while not juego.gano('B') and not juego.gano('N'):
        jugador_actual = juego.obtener_jugador_actual()
        color = jugador_actual.obtener_color()
        simbolo = jugador_actual.obtener_simbolo()
        print(f"Turno del jugador {color}")

        juego.dados.tirar()
        tirada = juego.interpretar_tirada()
        print(f"Dados: {tirada}")

        if not juego.hay_movimientos_posibles(color, tirada):
                print("No hay movimientos posibles. Pierdes el turno.")
                juego.cambiar_turno()
                continue
            

        while tirada:

            print("\n📍 Estado actual del tablero:")
            juego.tablero.mostrar()
            print(f"Valores disponibles: {tirada}")

            try:
                origen = int(input("Ingresá la casilla de origen (-1 si estás en barra): "))
                pasos = int(input("Ingresá la cantidad de pasos: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingresá números enteros.")
                continue
            try:
                juego.mover(origen, pasos)
                if juego.gano(color):
                    ganador = juego.obtener_jugador_actual()
                    print(f"\n🎉 ¡El jugador {ganador.obtener_simbolo()} (color: {ganador.obtener_color()}) ha ganado!")

                    return
                if pasos in tirada:
                    tirada.remove(pasos)
            except ValueError as e:
                print(f"movimiento inválido:")
                continue
            if not tirada:
                print("No quedan más movimientos en esta tirada.")
                break

            if juego.gano(color):
                color_ganador = color
                break

        juego.cambiar_turno()
    
    if color_ganador is None:
        if juego.gano('B'):
            color_ganador = 'B'
        elif juego.gano('N'):
            color_ganador = 'N'
    jugador_ganador = juego.jugadores[color_ganador]
    simbolo_ganador = jugador_ganador.obtener_simbolo()

    print(f" ¡El jugador {simbolo_ganador} (color: {color_ganador}) ha ganado! ")

