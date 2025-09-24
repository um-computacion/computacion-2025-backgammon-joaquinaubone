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
