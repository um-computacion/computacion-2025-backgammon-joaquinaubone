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
    
    def test_interpretar_tirada_no_doble(self):
        tablero = Tablero()
        resultado = tablero.interpretar_tirada(3, 5)
        self.assertEqual(resultado, [3, 5])
    
    def test_interpretar_tirada_doble(self):
        tablero = Tablero()
        resultado = tablero.interpretar_tirada(4, 4)
        self.assertEqual(resultado, [4, 4, 4, 4])

    def test_es_movimiento_valido_casilla_vacia(self):
        self.assertTrue(self.tablero._Tablero__es_movimiento_valido([], 'B'))

    def test_es_movimiento_valido_mismo_color(self):
        self.assertTrue(self.tablero._Tablero__es_movimiento_valido(['B'], 'B'))

    def test_es_movimiento_valido_una_ficha_rival(self):
        self.assertTrue(self.tablero._Tablero__es_movimiento_valido(['N'], 'B'))

    def test_es_movimiento_invalido_varias_fichas_rivales(self):
        self.assertFalse(self.tablero._Tablero__es_movimiento_valido(['N', 'N'], 'B'))

    def test_es_movimiento_fuera_de_tablero_blancas(self):
        self.assertTrue(self.tablero._Tablero__es_movimiento_fuera_de_tablero('B', 25))

    def test_es_movimiento_fuera_de_tablero_negras(self):
        self.assertTrue(self.tablero._Tablero__es_movimiento_fuera_de_tablero('N', -1))

    def test_puede_sacar_ficha_false(self):
        # Aún hay fichas fuera del último cuarto para blancas
        self.assertFalse(self.tablero.puede_sacar_ficha('B'))

    def test_puede_sacar_ficha_true(self):
        # Simular que blancas tienen todas sus fichas en el último cuarto (18–23)
        self.tablero = Tablero()
        self.tablero._Tablero__contenedor__ = [[] for _ in range(24)]
        self.tablero._Tablero__contenedor__[18] = ['B'] * 15
        self.assertTrue(self.tablero.puede_sacar_ficha('B'))

    def test_gano_true_blancas(self):
        self.tablero._Tablero__off_blanco__ = ['B'] * 15
        self.assertTrue(self.tablero.gano('B'))

    def test_gano_false_blancas(self):
        self.tablero._Tablero__off_blanco__ = ['B'] * 14
        self.assertFalse(self.tablero.gano('B'))

    def test_gano_true_negras(self):
        self.tablero._Tablero__off_negro__ = ['N'] * 15
        self.assertTrue(self.tablero.gano('N'))

    def test_gano_false_negras(self):
        self.tablero._Tablero__off_negro__ = ['N'] * 10
        self.assertFalse(self.tablero.gano('N'))
      
        

if __name__ == '__main__':
    unittest.main()