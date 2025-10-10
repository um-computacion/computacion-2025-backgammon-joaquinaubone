"""Módulo que define la clase Ficha del juego Backgammon."""
class Ficha:
    """Representa una ficha de Backgammon con un color asociado."""
    def __init__(self, color):
        """Inicializa una nueva ficha. """
        self.__color__ = color

    def obtener_color(self):
        """Devuelve el color de la ficha."""
        return self.__color__