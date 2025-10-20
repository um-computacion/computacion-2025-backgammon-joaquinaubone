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

    def interpretar_tirada(self):
        """Interpreta la tirada de dados actual: 4 valores si dobles, 2 si no."""
        dado1, dado2 = self.dados.obtener_valores()
        if dado1 == dado2:
            return [dado1] * 4
        return [dado1, dado2]
    
    def gano(self):
        """Verifica si el jugador actual ha ganado (15 fichas borneadas)."""
        color = self.turno_actual
        return len(self.tablero.obtener_off(color)) == 15
    
    def puede_sacar_ficha(self, color):
        """Verifica si el jugador puede empezar a sacar fichas (bornear)."""
        # No puede sacar si tiene fichas en la barra
        if self.tablero.obtener_bar(color):
            return False

        # Verificar que todas las fichas estén en casa
        if color == 'B':
            rango_prohibido = range(0, 18)  # Casa de blancas: 18-23
        else:
            rango_prohibido = range(6, 24)  # Casa de negras: 0-5

        for i in rango_prohibido:
            punto = self.tablero.get_point(i)
            if punto and punto[0] == color:
                return False
        return True
    
    def hay_movimientos_posibles(self, color, valores_dado):
        """Verifica si el jugador tiene movimientos válidos disponibles."""
        if self.tablero.obtener_bar(color):
            return self.__puede_salir_de_barra(color, valores_dado)

        direccion = self.__obtener_direccion(color)
        return self.__puede_mover_ficha_en_tablero(color, valores_dado, direccion)

    def mover(self, origen, pasos):
        """Ejecuta un movimiento aplicando todas las reglas del juego."""
        color = self.turno_actual

        # Validar que tenga fichas en barra y solo pueda mover desde ahí
        if self.tablero.obtener_bar(color) and origen != -1:
            raise ValueError("Debe mover primero las fichas en la barra.")

        # Sacar ficha del origen
        if origen == -1:
            ficha = self.__sacar_de_barra(color)
            destino = self.__calcular_destino_desde_barra(color, pasos)
            origen_real = -1
        else:
            ficha = self.__sacar_de_tablero(origen, color)
            destino = self.__calcular_destino(origen, pasos, color)
            origen_real = origen

        # Intentar ejecutar el movimiento
        try:
            if self.__es_movimiento_fuera_de_tablero(color, destino):
                if self.puede_sacar_ficha(color):
                    self.tablero.obtener_off(color).append(ficha)
                else:
                    raise ValueError(
                        "No se puede mover fuera del tablero sin poder bornearse."
                    )
            else:
                self.__mover_a_destino(destino, ficha, color)

        except ValueError:
            # Si falla, devolver la ficha al origen
            if origen_real == -1:
                self.tablero.obtener_bar(color).append(ficha)
            else:
                self.tablero.get_point(origen_real).append(ficha)
            raise

    def __obtener_direccion(self, color):
        """Determina la dirección de movimiento según el color."""
        if color == "B":
            return 1
        return -1

    def __calcular_destino_desde_barra(self, color, valor):
        """Calcula el destino al mover una ficha desde la barra."""
        if color == 'B':
            return valor - 1
        return 24 - valor

    def __calcular_destino(self, origen, pasos, color):
        """Calcula el destino desde una posición del tablero."""
        if color == 'B':
            return origen + pasos
        return origen - pasos

    def __es_movimiento_fuera_de_tablero(self, color, destino):
        """Determina si un movimiento sale del tablero."""
        return (color == 'B' and destino >= 24) or (color == 'N' and destino < 0)

    def __es_movimiento_valido(self, casilla, color):
        """Evalúa si una casilla es válida para mover una ficha."""
        return (
            not casilla                    # casilla vacía
            or casilla[0] == color         # primera ficha del mismo color
            or len(casilla) == 1           # solo una ficha rival
        )

    def __sacar_de_barra(self, color):
        """Saca una ficha de la barra."""
        bar = self.tablero.obtener_bar(color)
        if not bar:
            raise ValueError(f"No hay fichas {color} en la barra.")
        return bar.pop()

    def __sacar_de_tablero(self, origen, color):
        """Saca una ficha desde el tablero."""
        if not 0 <= origen <= 23:
            raise ValueError("Posición de origen fuera del tablero.")

        punto = self.tablero.get_point(origen)
        if not punto:
            raise ValueError("No hay fichas en la casilla de origen.")
        if punto[0] != color:
            raise ValueError("La ficha no pertenece al jugador.")

        return punto.pop()

    def __mover_a_destino(self, destino, ficha, color):
        """Coloca la ficha en la casilla destino, manejando capturas."""
        casilla = self.tablero.get_point(destino)

        if not casilla or casilla[0] == color:
            # Casilla vacía o del mismo color
            casilla.append(ficha)

        elif len(casilla) == 1 and casilla[0] != color:
            # Capturar ficha rival
            rival = casilla.pop()
            color_rival = 'B' if color == 'N' else 'N'
            self.tablero.obtener_bar(color_rival).append(rival)
            casilla.append(ficha)

        else:
            raise ValueError(
                "No se puede mover a una casilla ocupada por 2+ fichas rivales."
            )

    def __puede_salir_de_barra(self, color, valores_dado):
        """Verifica si puede mover fichas desde la barra."""
        for valor in valores_dado:
            destino = self.__calcular_destino_desde_barra(color, valor)
            if 0 <= destino <= 23:
                casilla = self.tablero.get_point(destino)
                if self.__es_movimiento_valido(casilla, color):
                    return True
        return False

    def __puede_mover_ficha_en_tablero(self, color, valores_dado, direccion):
        """Verifica si alguna ficha en el tablero puede moverse."""
        for i in range(24):
            casilla = self.tablero.get_point(i)
            if casilla and casilla[0] == color:
                for valor in valores_dado:
                    destino = i + valor * direccion

                    if self.__es_movimiento_fuera_de_tablero(color, destino):
                        if self.puede_sacar_ficha(color):
                            return True
                        continue

                    if 0 <= destino <= 23:
                        casilla_destino = self.tablero.get_point(destino)
                        if self.__es_movimiento_valido(casilla_destino, color):
                            return True
        return False
