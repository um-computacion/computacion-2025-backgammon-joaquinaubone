class PosNoExistenteException(Exception):
    pass

class Tablero:
    def _init_(self): 
        self._contenedor_ = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
        self._bar_blanco_ = []
        self._bar_negro_ = []
        self._off_blanco_ = []
        self._off_negro_ = []

    def setup(self): 
        self._contenedor_[0] = ['B'] * 2         
        self._contenedor_[11] = ['B'] * 5         
        self._contenedor_[16] = ['B'] * 3         
        self._contenedor_[18] = ['B'] * 5         

        self._contenedor_[23] = ['N'] * 2        
        self._contenedor_[12] = ['N'] * 5         
        self._contenedor_[7] = ['N'] * 3          
        self._contenedor_[5] = ['N'] * 5  

    def mostrar(self): 
        print("Tablero:")
        print(self._contenedor_)
        print(f"Barra Blancas: {self._bar_blanco_}")
        print(f"Barra Negras: {self._bar_negro_}")
        print(f"Borneadas Blancas: {self._off_blanco_}")
        print(f"Borneadas Negras: {self._off_negro_}")

    def get_point(self, indice):
        if 0 <= indice < len(self._contenedor_):
            return self._contenedor_[indice]
        else:
            raise PosNoExistenteException("El punto no existe en el tablero.")
        
    def obtener_bar(self, color):
        if color == 'B':
            return self._bar_blanco_
        elif color == 'N':
            return self._bar_negro_
        else:
            raise ValueError("Color no válido. Use B para blanco o N para negro")
        
    def obtener_off(self, color): 
        if color == 'B':
            return self._off_blanco_
        elif color == 'N':
            return self._off_negro_
        else:
            raise ValueError("Color no válido. Use B para blanco o N para negro")
        
