
""" Módulo de pruebas unitarias para la clase Tablero del juego de backgammon."""
import unittest
from core.board import Tablero
from core.checker import Checker
from exceptions import ColorInvalidoException, PosNoExistenteException

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

        punto_0 = tablero.get_point(0)
        self.assertEqual(len(punto_0), 2)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_0))

        punto_11 = tablero.get_point(11)
        self.assertEqual(len(punto_11), 5)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_11))

        punto_16 = tablero.get_point(16)
        self.assertEqual(len(punto_16), 3)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_16))

        punto_18 = tablero.get_point(18)
        self.assertEqual(len(punto_18), 5)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_18))

        punto_23 = tablero.get_point(23)
        self.assertEqual(len(punto_23), 2)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_23))

        punto_12 = tablero.get_point(12)
        self.assertEqual(len(punto_12), 5)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_12))

        punto_7 = tablero.get_point(7)
        self.assertEqual(len(punto_7), 3)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_7))

        punto_5 = tablero.get_point(5)
        self.assertEqual(len(punto_5), 5)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_5))
    
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
        with self.assertRaises(ColorInvalidoException):
            tablero.obtener_bar('X')
    
    def test_obtener_off_color_invalido(self):
        """Verifica excepción al pedir off con color inválido."""
        tablero = Tablero()
        with self.assertRaises(ColorInvalidoException):
            tablero.obtener_off('X')

    def test_obtener_off_blanca(self): 
        """Verifica que el off blanca esté vacío al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('B'), [])

    def test_obtener_off_negra(self): 
        """Verifica que el off negra esté vacío al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('N'), [])
    
    def test_mostrar_con_fichas_en_barra_blanca(self):
        tablero = Tablero()
        tablero.obtener_bar('B').append(Checker('B'))  # Una ficha blanca en barra
        tablero.mostrar()  # Si no rompe, se ejecutó OK


    def test_mostrar_con_fichas_en_barra_negra(self):
        tablero = Tablero()
        tablero.obtener_bar('N').append(Checker('N'))  # Una ficha negra en barra
        tablero.mostrar()  # Si no rompe, se ejecutó OK


    

    


if __name__ == '__main__':
    unittest.main()