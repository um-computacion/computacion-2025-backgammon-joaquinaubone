from Board.board import Tablero
from Dice.dice import Dice
from Player.player import Player

def main():
    # Crear instancias de los componentes del juego
    tablero = Tablero()
    tablero.setup()

    dados = Dice()
    jugador_blanco = Player('B')
    jugador_negro = Player('N')

if __name__ == '__main__':
    main()