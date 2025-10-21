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
    tablero = Tablero()
    tablero.setup()

    dados = Dice()
    jugador_blanco = Player('B')
    jugador_negro = Player('N')

    jugar(tablero, dados, jugador_blanco, jugador_negro)
    
if __name__ == '__main__':
    main()