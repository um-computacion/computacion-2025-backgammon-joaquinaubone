"""Módulo de excepciones personalizadas para el juego Backgammon.

Define una jerarquía de excepciones específicas del dominio que facilitan
el manejo de errores y mejoran la claridad del código.
"""


class BackgammonException(Exception):
    """Excepción base para todos los errores del juego Backgammon.
    
    Todas las excepciones específicas del juego heredan de esta clase, permitiendo capturar cualquier error del juego con un único except. """
    pass


class PosNoExistenteException(BackgammonException):
    """Excepción lanzada cuando se intenta acceder a una posición inválida del tablero.
    """
    pass


class ColorInvalidoException(BackgammonException):
    """Excepción lanzada cuando se usa un color de jugador inválido."""
    pass

class PosicionInvalida(BackgammonException):
    """Excepción lanzada cuando se usa una posición inválida en el tablero."""
    pass