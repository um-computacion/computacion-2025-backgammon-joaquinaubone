
""" Módulo de pruebas unitarias para la clase Tablero del juego de backgammon."""
import unittest
from board.board import Tablero, PosNoExistenteException

class TestTablero(unittest.TestCase):
    """Clase de pruebas para Tablero."""

    def setUp(self):
        """Inicializa un tablero configurado antes de cada test."""
        self.tablero = Tablero()
        self.tablero.setup()
    
    def test_setup_inicial(self): 
        """Verifica que se coloque cada pieza en su posición inicial."""
        tablero = Tablero()
        tablero.setup()
        self.assertEqual(tablero.get_point(0), ['B', 'B'])
        self.assertEqual(tablero.get_point(11), ['B'] * 5)
        self.assertEqual(tablero.get_point(16), ['B'] * 3)
        self.assertEqual(tablero.get_point(18), ['B'] * 5)
        self.assertEqual(tablero.get_point(23), ['N'] * 2)
        self.assertEqual(tablero.get_point(12), ['N'] * 5)
        self.assertEqual(tablero.get_point(7), ['N'] * 3)
        self.assertEqual(tablero.get_point(5), ['N'] * 5)
    
    def test_mostrar_no_falla(self):
        """Verifica que el método mostrar() no lance excepciones."""
        tablero = Tablero()
        tablero.setup()
        tablero.mostrar()

    def test_get_point_valido(self): 
        """Verifica que get_point retorne una lista para posición válida."""
        tablero = Tablero()
        tablero.setup()
        punto = tablero.get_point(0)
        self.assertIsInstance(punto, list)

    def test_get_point_no_existe(self): 
        """Verifica que get_point lance excepción para posición inválida."""
        tablero = Tablero()
        with self.assertRaises(PosNoExistenteException):
            tablero.get_point(30)  

    def test_obtener_bar_blanca_inicio(self): 
        """Verifica que la barra blanca esté vacía al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_bar('B'), [])
    
    def test_obtener_bar_negra(self): 
        """Verifica que la barra negra esté vacía al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_bar('N'), [])

    def test_obtener_bar_color_invalido(self): 
        """Verifica excepción al pedir barra con color inválido."""
        tablero = Tablero()
        with self.assertRaises(ValueError):
            tablero.obtener_bar('X')
    
    def test_obtener_off_color_invalido(self):
        """Verifica excepción al pedir off con color inválido."""
        tablero = Tablero()
        with self.assertRaises(ValueError):
            tablero.obtener_off('X')

    def test_obtener_off_blanca(self): 
        """Verifica que el off blanca esté vacío al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('B'), [])

    def test_obtener_off_negra(self): 
        """Verifica que el off negra esté vacío al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('N'), [])

if __name__ == '__main__':
    unittest.main()