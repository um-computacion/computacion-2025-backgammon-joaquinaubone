from Dice.dice import Dado
from Board.board import Tablero

class Juego:
    def __init__(self):
        self.turno = 'B'  # Blanco empieza

    def cambiar_turno(self):
        self.turno = 'B' if self.turno == 'N' else 'N'