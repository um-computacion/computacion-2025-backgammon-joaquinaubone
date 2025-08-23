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