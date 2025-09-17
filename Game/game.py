from Dice.dice import Dado
from Board.board import Tablero
from Player.player import Player

class Juego:
    def __init__(self, tablero, dados, jugador_blanco, jugador_negro):
        self.tablero = tablero
        self.turno_actual = 'B'  # Blanco empieza
        self.dados = dados
        self.jugadores = {'B': jugador_blanco, 'N': jugador_negro}


    def cambiar_turno(self): #maneja cambios de turno
        if self.turno == 'N':
            self.turno = 'B'  
        else:
            self.turno = "N"
    
    def obtener_jugador_actual(self):   # Devuelve el jugador que tiene el turno actual
        return self.jugadores[self.turno_actual]

    def verificar_fin_del_juego(self):  # Verifica si el jugador actual ha ganado
        return self.tablero.gano(self.turno_actual)

    def hay_movimientos_disponibles(self, tirada):  # Verifica si hay movimientos disponibles para el jugador actual
        return self.tablero.hay_movimientos_posibles(self.turno_actual, tirada)

    def intentar_jugada(self, origen, pasos):# Intenta realizar una jugada, lanza excepción si falla
        self.tablero.mover(origen, pasos, self.turno_actual)

    def interpretar_tirada(self, dado1, dado2): # Interpreta una tirada (dobles o normales)
        return self.tablero.interpretar_tirada(dado1, dado2)