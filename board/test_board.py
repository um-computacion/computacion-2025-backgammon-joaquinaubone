import unittest
from Board.board import Tablero, PosNoExistenteException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()
        self.tablero.setup()
    
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
    
    def test_mostrar_no_falla(self):
        tablero = Tablero()
        tablero.setup()
        try:
            tablero.mostrar()
        except Exception as e:
            self.fail(f"mostrar() lanzó una excepción: {e}")

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

    def test_movimiento_dentro_de_tablero(self):
        self.assertFalse(self.tablero._Tablero__es_movimiento_fuera_de_tablero('B', 5))

    def test_puede_sacar_ficha_false(self):  # Aún hay fichas fuera del último cuarto para blancas
        self.assertFalse(self.tablero.puede_sacar_ficha('B'))

    def test_puede_sacar_ficha_true(self): # Simular que blancas tienen todas sus fichas en el último cuarto (18–23)
        self.tablero = Tablero()
        self.tablero._Tablero__contenedor__ = [[] for _ in range(24)]
        self.tablero._Tablero__contenedor__[18] = ['B'] * 15
        self.assertTrue(self.tablero.puede_sacar_ficha('B'))
    
    def test_puede_sacar_ficha_inicio_negras(self): #hola
        tablero = Tablero()
        tablero.setup()  
        self.assertFalse(tablero.puede_sacar_ficha('N')) 

    def test_gano_true_blancas(self):
        tablero = Tablero()
        tablero.obtener_off('B').extend(['B'] * 15)
        self.assertTrue(tablero.gano('B'))

    def test_gano_false_blancas(self):
        tablero = Tablero()
        tablero.obtener_off('B').extend(['B'] * 14)
        self.assertFalse(tablero.gano('B'))

    def test_gano_true_negras(self):
        tablero = Tablero()
        tablero.obtener_off('N').extend(['N'] * 15)
        self.assertTrue(tablero.gano('N'))

    def test_gano_false_negras(self):
        tablero = Tablero()
        tablero.obtener_off('N').extend(['N'] * 13)
        self.assertFalse(tablero.gano('N'))
    
    def test_gano_color_invalido(self):
        tablero = Tablero()
        self.assertFalse(tablero.gano('X'))  
    
    
    def test_no_gano(self):
        self.assertFalse(self.tablero.gano('B'))
    
    def test_hay_movimiento_posible_desde_tablero(self):
        self.assertTrue(self.tablero.hay_movimientos_posibles('B', [1, 2]))

    def test_hay_movimiento_posible_desde_barra(self):
        self.tablero.obtener_bar('B').append('B')
        self.tablero._Tablero__contenedor = [[] for _ in range(24)]
        self.assertTrue(self.tablero.hay_movimientos_posibles('B', [1]))

    def test_no_hay_movimiento_posible(self):
        tablero = Tablero()
        tablero._Tablero__contenedor__ = [[] for _ in range(24)]
        self.assertFalse(tablero.hay_movimientos_posibles('B', [1, 2]))

    def test_sacar_de_barra_blancas(self):
        self.tablero.obtener_bar('B').append('B')
        ficha, destino = self.tablero._Tablero__sacar_de_barra('B', 3)
        self.assertEqual(ficha, 'B')
        self.assertEqual(destino, 2)

    def test_sacar_de_barra_negras(self):
        self.tablero.obtener_bar('N').append('N')
        ficha, destino = self.tablero._Tablero__sacar_de_barra('N', 5)
        self.assertEqual(ficha, 'N')
        self.assertEqual(destino, 19)

    def test_sacar_de_tablero_blancas(self):
        ficha, destino = self.tablero._Tablero__sacar_de_tablero(0, 3, 'B')
        self.assertEqual(ficha, 'B')
        self.assertEqual(destino, 3)

    def test_sacar_de_tablero_negras(self):
        ficha, destino = self.tablero._Tablero__sacar_de_tablero(23, 2, 'N')
        self.assertEqual(ficha, 'N')
        self.assertEqual(destino, 21)
    
    def test_sacar_de_tablero_sin_fichas(self):
        tablero = Tablero()
        tablero._Tablero__contenedor__ = [[] for _ in range(24)]  # tablero vacío
        with self.assertRaises(ValueError) as context:
            tablero._Tablero__sacar_de_tablero(5, 3, 'B')  # casilla vacía
        self.assertEqual(str(context.exception), "No hay fichas en la casilla de origen.")


    def test_calcular_destino_desde_barra_blanco(self):
        destino = self.tablero._Tablero__calcular_destino_desde_barra('B', 2)
        self.assertEqual(destino, 1)

    def test_calcular_destino_desde_barra_negro(self):
        destino = self.tablero._Tablero__calcular_destino_desde_barra('N', 2)
        self.assertEqual(destino, 22)
    
    def test_obtener_direccion_negro(self):
        direccion = self.tablero._Tablero__obtener_direccion('N')
        self.assertEqual(direccion, -1)
    
    def test_obtener_direccion_blanco(self):
        direccion = self.tablero._Tablero__obtener_direccion('B')
        self.assertEqual(direccion, 1)

    def test_puede_mover_ficha_en_tablero_true(self):
        valores = [1]
        direccion = self.tablero._Tablero__obtener_direccion('B')
        self.assertTrue(self.tablero._Tablero__puede_mover_ficha_en_tablero('B', valores, direccion))

    def test_puede_mover_ficha_en_tablero_false(self):
        tablero = Tablero()
        tablero._Tablero__contenedor__ = [[] for _ in range(24)]
        direccion = tablero._Tablero__obtener_direccion('B')
        self.assertFalse(tablero._Tablero__puede_mover_ficha_en_tablero('B', [1], direccion))
    
    def test_agregar_a_off_blanco(self):
        self.tablero._Tablero__agregar_a_off('B', 'B')
        self.assertEqual(self.tablero.obtener_off('B'), ['B'])

    def test_agregar_a_off_negro(self):
        self.tablero._Tablero__agregar_a_off('N', 'N')
        self.assertEqual(self.tablero.obtener_off('N'), ['N'])

    def test_mover_color_invalido(self): 
        with self.assertRaises(ValueError):
            self.tablero.mover(1, 3, 'X')  
    
    def test_mover_con_ficha_en_barra_y_origen_distinto_de_cero(self):
        self.tablero.obtener_bar('B').append('B')  
        with self.assertRaises(ValueError):
            self.tablero.mover(5, 3, 'B') 

    def test_mover_desde_barra_blanca(self):
        self.tablero.obtener_bar('B').append('B')
        self.tablero._Tablero__contenedor__ = [[] for _ in range(24)]  
        self.tablero.mover(0, 3, 'B')  
        self.assertEqual(self.tablero.get_point(2), ['B'])  
        
    def test_mover_fuera_de_tablero_sin_poder_bornear(self):
        self.tablero._Tablero__contenedor__ = [[] for _ in range(24)]
        self.tablero._Tablero__contenedor__[10].append('B')  
        with self.assertRaises(ValueError):
            self.tablero.mover(10, 15, 'B')  


if __name__ == '__main__':
    unittest.main()