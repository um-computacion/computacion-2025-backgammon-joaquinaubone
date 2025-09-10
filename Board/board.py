class PosNoExistenteException(Exception):
    pass

class Tablero:
    def __init__(self): 
        self.__contenedor__ = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
        self.__bar_blanco__ = []
        self.__bar_negro__ = []
        self.__off_blanco__ = []
        self.__off_negro__ = []

    def setup(self): 
        self.__contenedor__[0] = ['B'] * 2         
        self.__contenedor__[11] = ['B'] * 5         
        self.__contenedor__[16] = ['B'] * 3         
        self.__contenedor__[18] = ['B'] * 5         

        self.__contenedor__[23] = ['N'] * 2        
        self.__contenedor__[12] = ['N'] * 5         
        self.__contenedor__[7] = ['N'] * 3          
        self.__contenedor__[5] = ['N'] * 5  

    def mostrar(self): 
        print("Tablero:")
        print(self.__contenedor__)
        print(f"Barra Blancas: {self.__bar_blanco__}")
        print(f"Barra Negras: {self.__bar_negro__}")
        print(f"Borneadas Blancas: {self.__off_blanco__}")
        print(f"Borneadas Negras: {self.__off_negro__}")

    def get_point(self, indice):
        if 0 <= indice < len(self.__contenedor__):
            return self.__contenedor__[indice]
        else:
            raise PosNoExistenteException("El punto no existe en el tablero.")
        
    def obtener_bar(self, color):
        if color == 'B':
            return self.__bar_blanco__
        elif color == 'N':
            return self.__bar_negro__
        else:
            raise ValueError("Color no válido. Use B para blanco o N para negro")
        
    def obtener_off(self, color): 
        if color == 'B':
            return self.__off_blanco__
        elif color == 'N':
            return self.__off_negro__
        else:
            raise ValueError("Color no válido. Use B para blanco o N para negro")
        
    def interpretar_tirada(self, dado1, dado2):
        if dado1 == dado2:
            return [dado1] * 4
        return [dado1, dado2]
            
    def __es_movimiento_valido(self, casilla, color):
        return (
            not casilla                         # casilla vacía
            or casilla[-1] == color             # última ficha del mismo color
            or len(casilla) == 1                # solo una ficha rival
        )

    def __es_movimiento_fuera_de_tablero(self, color, destino):
        return (color == 'B' and destino >= 24) or (color == 'N' and destino < 0)

    def puede_sacar_ficha(self, color):
        if color == 'B':
            rango_prohibido = range(0, 18)  
        else:
            rango_prohibido = range(6, 24)
        for i in rango_prohibido:
            if self.__contenedor__[i] and self.__contenedor__[i][-1] == color:
                return False
        return True
    
    def gano(self, color):
        if color == 'B':
            return len(self.__off_blanco__) == 15
        elif color == 'N':
            return len(self.__off_negro__) == 15
        return False

    def mover(self, origen, pasos, color):
        # Ejecuta un movimiento desde una posición hacia otra.
        if color not in ('B', 'N'):
            raise ValueError("Color inválido. Use 'B' o 'N'.")

        if self.obtener_bar(color) and origen != 0:
            raise ValueError("Debe mover primero las fichas en la barra.")

        if origen == 0:
            ficha, destino = self.__sacar_de_barra(color, pasos)
        else:
            ficha, destino = self.__sacar_de_tablero(origen, pasos, color)

        if self.__es_movimiento_fuera_de_tablero(color, destino):
            if self.puede_sacar_ficha(color):
                self.__agregar_a_off(color, ficha)
            else:
                raise ValueError("No se puede mover fuera del tablero sin poder bornearse.")
            return

        self.__mover_a_destino(destino, ficha, color)
    
    def __sacar_de_barra(self, color, pasos):
        # Saca una ficha de la barra y calcula el destino. Usado en mover()
        if color == 'B':
            if not self.__bar_blanco__:
                raise ValueError("No hay fichas blancas en la barra.")
            return self.__bar_blanco__.pop(), pasos - 1
        else:
            if not self.__bar_negro__:
                raise ValueError("No hay fichas negras en la barra.")
            return self.__bar_negro__.pop(), 24 - pasos
        
    def __sacar_de_tablero(self, origen, pasos, color):
        # Saca una ficha del tablero y calcula el destino. Usado en mover()
        if not (0 <= origen <= 23):
            raise ValueError("Posición de origen fuera del tablero.")
        if not self.__contenedor__[origen]:
            raise ValueError("No hay fichas en la casilla de origen.")
        if self.__contenedor__[origen][-1] != color:
            raise ValueError("La ficha no pertenece al jugador.")
        ficha = self.__contenedor__[origen].pop()
        if color == 'B':
            destino = origen + pasos    
        else:
            destino= origen - pasos
        return ficha, destino
    
    def __agregar_a_off(self, color, ficha):
    # Agrega la ficha a la zona de borneados. Usado en mover().
        if color == 'B':
            self.__off_blanco__.append(ficha)
        else:
            self.__off_negro__.append(ficha)

    def __mover_a_destino(self, destino, ficha, color):
    # Mueve una ficha a una casilla destino. Maneja golpes y validaciones.
        casilla = self.__contenedor__[destino]
        if not casilla or casilla[-1] == color:
            casilla.append(ficha)
        elif len(casilla) == 1:
            rival = casilla.pop()
            self.obtener_bar('B' if color == 'N' else 'N').append(rival)
            casilla.append(ficha)
        else:
            raise ValueError("No se puede mover a una casilla ocupada por 2+ fichas rivales.")
    
    def hay_movimientos_posibles(self, color, valores_dado): 
        if self.obtener_bar(color):
            return self.__puede_salir_de_barra(color, valores_dado)
        direccion = self.__obtener_direccion(color)
        return self.__puede_mover_ficha_en_tablero(color, valores_dado, direccion)

    def __obtener_direccion(self, color): #si ficha se mueve para izquierda o derecha
        if color == "B":
            return 1
        else:
            return -1

    def __calcular_destino_desde_barra(self, color, valor): # calcula movimiento desde barra
        if color == 'B':
            return valor - 1
        else:
            return 24 - valor
        return valor - 1 if color == 'B' else 24 - valor

    def __puede_salir_de_barra(self, color, valores_dado):  # Verifica movimiento desde barra
        for valor in valores_dado:
            destino = self.__calcular_destino_desde_barra(color, valor)
            if 0 <= destino <= 23 and self.__es_movimiento_valido(self.__contenedor__[destino], color):
                return True
        return False

    def __puede_mover_ficha_en_tablero(self, color, valores_dado, direccion): # Verifica si alguna ficha puede moverse.
        for i in range(24):
            casilla = self.__contenedor__[i]
            if casilla and casilla[-1] == color:
                for valor in valores_dado:
                    destino = i + valor * direccion
                    if self.__es_movimiento_fuera_de_tablero(color, destino):
                        if self.puede_sacar_ficha(color):
                            return True
                        continue
                    if 0 <= destino <= 23 and self.__es_movimiento_valido(self.__contenedor__[destino], color):
                        return True
        return False
