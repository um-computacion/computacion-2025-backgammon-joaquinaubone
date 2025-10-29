"""Módulo Player: contiene la clase Player para representar un jugador de Backgammon."""
from core.checker import Checker

class Player:
    """Representa un jugador del juego de Backgammon."""

    def __init__(self, color, nombre=None):
        """Inicializa un jugador con el color indicado."""
        self.__color__ = color
        if nombre is None:
            self.__nombre__ = "jugador_blanco" if color == "B" else "jugador_negro"
        else:
            self.__nombre__ = nombre

    def obtener_color(self):
        """Devuelve el color asignado al jugador ('B' o 'N')."""
        return self.__color__
    
    def obtener_nombre(self):
        return self.__nombre__
    
    def obtener_simbolo(self):
        """Devuelve el símbolo asociado al jugador según su color."""
        checker = Checker(self.__color__)
        return str(checker)
