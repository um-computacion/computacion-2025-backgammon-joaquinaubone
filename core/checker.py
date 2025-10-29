class Checker:
    """Representa una ficha del juego."""
    
    def __init__(self, color):
        """Inicializa una ficha con su color."""
        self.__color__ = color
    
    def obtener_color(self):
        """Devuelve el color de la ficha."""
        return self.__color__
    
    def __str__(self):
        """Representación en string de la ficha."""
        return 'X' if self.__color__ == 'B' else 'O'
    
    def __repr__(self):
        """Representación para debugging."""
        return f"Checker('{self.__color__}')"