"""Módulo Player: contiene la clase Player para representar un jugador de Backgammon."""

class Player:
    """Representa un jugador del juego de Backgammon."""

    def __init__(self, color):
        """Inicializa un jugador con el color indicado."""
        self.__color__ = color

    def obtener_color(self):
        """Devuelve el color asignado al jugador ('B' o 'N')."""
        return self.__color__
