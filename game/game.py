"""Módulo Game: Coordina la lógica general del flujo del juego de Backgammon."""

class Juego:
    """Clase principal que controla la lógica general del juego de Backgammon."""

    def __init__(self, tablero, dados, jugador_blanco, jugador_negro):
        self.tablero = tablero
        self.turno_actual = 'B'  # Blanco empieza
        self.dados = dados
        self.jugadores = {'B': jugador_blanco, 'N': jugador_negro}


    def cambiar_turno(self): 
        """Alterna el turno entre los jugadores blanco y negro."""
        if self.turno_actual == 'N':
            self.turno_actual = 'B'  
        else:
            self.turno_actual = "N"
    
    def obtener_jugador_actual(self): 
        """Devuelve el jugador correspondiente al turno actual."""
        return self.jugadores[self.turno_actual]

    def verificar_fin_del_juego(self): 
        """Verifica si el jugador actual ha ganado la partida."""
        return self.tablero.gano(self.turno_actual)

    def hay_movimientos_disponibles(self, tirada): 
        """Verifica si existen movimientos válidos para el jugador actual."""
        return self.tablero.hay_movimientos_posibles(self.turno_actual, tirada)

    def intentar_jugada(self, origen, pasos):
        """Intenta realizar una jugada, lanzando excepción si no es válida."""
        self.tablero.mover(origen, pasos, self.turno_actual)

    def interpretar_tirada(self, dado1, dado2): 
        """Interpreta una tirada de dados, considerando dobles o normales."""
        return self.tablero.interpretar_tirada(dado1, dado2)