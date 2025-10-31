"""Módulo Board: gestiona el estado del tablero de Backgammon.

Contiene toda la lógica relacionada con las posiciones, movimientos,
borneado, barra y verificación de condiciones de victoria.
"""
from core.checker import Checker
from exceptions import ColorInvalidoException, PosNoExistenteException

class Tablero:
    """Clase principal que representa el tablero y su estado."""
    def __init__(self): 
        """Inicializa el tablero, las barras y las zonas de borneado."""
        self.__contenedor__ = [
            [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [] 
        ]
        self.__bar_blanco__ = []
        self.__bar_negro__ = []
        self.__off_blanco__ = []
        self.__off_negro__ = []
        self.setup()

    def setup(self): 
        """Configura el tablero con la posición inicial estándar de Backgammon."""
        self.__contenedor__ = [[] for _ in range(24)]

        self.__contenedor__[0] = [Checker('B') for _ in range(2)]
        self.__contenedor__[11] = [Checker('B') for _ in range(5)]
        self.__contenedor__[16] = [Checker('B') for _ in range(3)]
        self.__contenedor__[18] = [Checker('B') for _ in range(5)]

        self.__contenedor__[23] = [Checker('N') for _ in range(2)]
        self.__contenedor__[12] = [Checker('N') for _ in range(5)]
        self.__contenedor__[7] = [Checker('N') for _ in range(3)]
        self.__contenedor__[5] = [Checker('N') for _ in range(5)]
      

    def mostrar(self): 
        """Muestra el tablero con fichas apiladas verticalmente usando métodos públicos."""
        
        bar_blanco = self.obtener_bar('B')
        bar_negro = self.obtener_bar('N')
        off_blanco = self.obtener_off('B')
        off_negro = self.obtener_off('N')
        
        # Encontrar la altura máxima
        max_height = max([len(self.get_point(i)) for i in range(24)] + [5])
        
        print("\n┌" + "─" * 37 + "┬" + "─" * 5 + "┬" + "─" * 37 + "┐")
        
        # Números superiores (11-0 de izq a der)
        print("│ 11  10   9   8   7   6 │ BAR │  5   4   3   2   1   0 │")
        
        # Parte superior (fichas que van hacia abajo desde arriba)
        for nivel in range(max_height):
            linea = "│"
            
            # Posiciones 11-6
            for i in range(11, 5, -1):
                punto = self.get_point(i)
                if nivel < len(punto):
                    ficha = punto[nivel]
                    linea += f"  {ficha}  "
                else:
                    linea += "    "
            
            linea += " │"
            
            # BARRA - mostrar fichas negras arriba
            if nivel < len(bar_negro):
                ficha = bar_negro[nivel]
                linea += f"  {str(ficha)}  "
            else:
                linea += "     "
            
            linea += "│"
            
            # Posiciones 5-0
            for i in range(5, -1, -1):
                punto = self.get_point(i)
                if nivel < len(punto):
                    ficha = punto[nivel]
                    linea += f"  {ficha}"
                else:
                    linea += "    "
            
            linea += " │"
            print(linea)
        
        # Línea divisoria
        print("├" + "─" * 37 + "┼" + "─" * 5 + "┼" + "─" * 37 + "┤")
        
        # Parte inferior (fichas que van hacia arriba desde abajo)
        for nivel in range(max_height - 1, -1, -1):
            linea = "│"
            
            # Posiciones 12-17
            for i in range(12, 18):
                punto = self.get_point(i)
                if nivel < len(punto):
                    ficha = punto[nivel]
                    linea += f"  {ficha} "
                else:
                    linea += "    "
            
            linea += " │"
            
            # BARRA - mostrar fichas blancas abajo
            if nivel < len(bar_blanco):
                ficha = bar_blanco[nivel]
                linea += f" {str(ficha)}  "
            else:
                linea += "     "
            
            linea += "│"
            
            # Posiciones 18-23
            for i in range(18, 24):
                punto = self.get_point(i)
                if nivel < len(punto):
                    ficha = punto[nivel]
                    linea += f"  {ficha} "
                else:
                    linea += "    "
            
            linea += " │"
            print(linea)
        
        # Números inferiores (12-23)
        print("│ 12  13  14  15  16  17 │     │ 18  19  20  21  22  23 │")
        print("└" + "─" * 37 + "┴" + "─" * 5 + "┴" + "─" * 37 + "┘")
        
        # Información adicional
        print(f"\nBarra: X={len(bar_blanco)} O={len(bar_negro)}  | "
              f"OFF: X={len(off_blanco)} O={len(off_negro)}")
        print()


    def get_point(self, indice):
        """Devuelve la lista de fichas en una posición específica."""
        if 0 <= indice < len(self.__contenedor__):
            return self.__contenedor__[indice]
        raise PosNoExistenteException("El punto no existe en el tablero.")
            
    def obtener_bar(self, color):
        """Devuelve la barra correspondiente al color indicado."""
        if color == 'B':
            return self.__bar_blanco__
        if color == 'N':
            return self.__bar_negro__
        raise ColorInvalidoException("Color no válido. Use B para blanco o N para negro")
            
    def obtener_off(self, color): 
        """Devuelve la lista de fichas borneadas (fuera del tablero)."""
        if color == 'B':
            return self.__off_blanco__
        if color == 'N':
            return self.__off_negro__
        raise ColorInvalidoException("Color no válido. Use B para blanco o N para negro")
    
    
