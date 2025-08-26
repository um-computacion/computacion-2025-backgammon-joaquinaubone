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
        
if __name__ == '__main__':
    unittest.main()