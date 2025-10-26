"""Módulo principal del juego Backgammon.

Inicializa los componentes principales del juego (tablero, dados y jugadores)
y ejecuta la interfaz CLI para comenzar la partida.
"""
from board.board import Tablero
from dice.dice import Dice
from player.player import Player
from cli.cli import jugar

def main():
    """Punto de entrada del programa. Configura los objetos principales y lanza el juego."""
    print("=" * 50)
    print("BACKGAMMON")
    print("=" * 50)
    print("Selecciona la interfaz:")
    print("1. CLI (texto)")
    print("2. GUI (gráfica con Pygame)")
    print("=" * 50)

    while True:
        opcion = input("Ingresa tu opción (1 o 2): ")
        if opcion in ['1', '2']:
            break
        print(" Opción inválida. Por favor ingresa 1 o 2.\n")
    
    tablero = Tablero()
    tablero.setup()
    dados = Dice()
    jugador_blanco = Player('B')
    jugador_negro = Player('N')

    

    if opcion == '2':
        try:
            from pygameUI.pygame_ui import jugar_pygame
            print("\nIniciando interfaz gráfica...\n")
            jugar_pygame(tablero, dados, jugador_blanco, jugador_negro)
        except ImportError:
            print("\n  Error: Pygame no está instalado.")
            print("Instalalo con: pip install pygame")
            print("\nIniciando CLI en su lugar...\n")
            jugar(tablero, dados, jugador_blanco, jugador_negro)
            
    else:
        print("\nIniciando interfaz CLI...\n")
        jugar(tablero, dados, jugador_blanco, jugador_negro)


if __name__ == '__main__':
    main()