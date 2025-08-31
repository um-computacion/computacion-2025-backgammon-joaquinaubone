import unittest
from Board.board import Tablero, PosNoExistenteException

class TestTablero(unittest.TestCase):

    def test_setup_inicial(self): #verifica q se coloque cada pieza en su posicion
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

    def test_get_point_valido(self): 
        tablero = Tablero()
        tablero.setup()
        punto = tablero.get_point(0)
        self.assertIsInstance(punto, list)

    def test_get_point_no_existe(self): # si pedis una posicion q no existe, te tira error
        tablero = Tablero()
        with self.assertRaises(PosNoExistenteException):
            tablero.get_point(30)  

    def test_obtener_bar_blanca_inicio(self): # verifica q el bar blanca este vacia al inicio
        tablero = Tablero()
        self.assertEqual(tablero.obtener_bar('B'), [])
    
    def test_obtener_bar_negra(self): # verifica q el bar negra este vacia al inicio
        tablero = Tablero()
        self.assertEqual(tablero.obtener_bar('N'), [])

    def test_obtener_bar_color_invalido(self): # verifica q si se pide un color invalido, se tire error
        tablero = Tablero()
        with self.assertRaises(ValueError):
            tablero.obtener_bar('X')
    
    def test_obtener_off_color_invalido(self):
        tablero = Tablero()
        with self.assertRaises(ValueError):
            tablero.obtener_off('X')

    def test_obtener_off_blanca(self): # verifica q el off blanca este vacia al inicio
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('B'), [])

    def test_obtener_off_negra(self): # verifica q el off negra este vacia al inicio
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('N'), [])

    def test_mostrar_no_falla(self):
        tablero = Tablero()
        tablero.setup()
        try:
            tablero.mostrar()
        except Exception as e:
            self.fail(f"mostrar() lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()