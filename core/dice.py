"""Módulo para gestionar los dados en el juego de Backgammon."""
import random

class Dice:
    """Clase que representa un par de dados en el juego de Backgammon."""

    def __init__(self): 
        """Inicializa los valores de los dados como lista vacía."""
        self.__values__ = []

    def tirar(self):    
        """Lanza los dos dados y guarda los valores obtenidos."""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        self.__values__ = [dado1, dado2]
    
    def obtener_valores(self): 
        """Devuelve la lista de valores actuales de los dados."""
        return self.__values__
    