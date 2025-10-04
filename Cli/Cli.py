from Game.game import Game

def jugar(tablero, dados, jugador_blanco, jugador_negro):
    juego = Game(tablero, dados, jugador_blanco, jugador_negro)

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

            except Exception as e:
                print(f"Error: {e}")
                continue
        if tablero.gano(color):
            break

        juego.cambiar_turno()

    print(f"\n🏆 ¡El jugador {juego.obtener_jugador_actual().obtener_color()} ha ganado!")
