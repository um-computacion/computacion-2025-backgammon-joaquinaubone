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
