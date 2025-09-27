from Board.board import Tablero
from Dice.dice import Dice
from Player.player import Player
from Cli.Cli import jugar

def main():
    # Crear instancias de los componentes del juego
    tablero = Tablero()
    tablero.setup()

    dados = Dice()
    jugador_blanco = Player('B')
    jugador_negro = Player('N')

    jugar(tablero, dados, jugador_blanco, jugador_negro)
    
if __name__ == '__main__':
    main()