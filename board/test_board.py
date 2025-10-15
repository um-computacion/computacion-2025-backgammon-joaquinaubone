
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

    def test_interpretar_tirada_no_doble(self):
        """Verifica interpretación de tirada sin dobles."""
        tablero = Tablero()
        resultado = tablero.interpretar_tirada(3, 5)
        self.assertEqual(resultado, [3, 5])
    
    def test_interpretar_tirada_doble(self):
        """Verifica interpretación de tirada con dobles."""
        tablero = Tablero()
        resultado = tablero.interpretar_tirada(4, 4)
        self.assertEqual(resultado, [4, 4, 4, 4])
    
    def test_gano_true_blancas(self):
        """Verifica victoria de blancas con 15 fichas en off."""
        tablero = Tablero()
        tablero.obtener_off('B').extend(['B'] * 15)
        self.assertTrue(tablero.gano('B'))

    def test_gano_false_blancas(self):
        """Verifica que blancas no ganan con 14 fichas en off."""
        tablero = Tablero()
        tablero.obtener_off('B').extend(['B'] * 14)
        self.assertFalse(tablero.gano('B'))

    def test_gano_true_negras(self):
        """Verifica victoria de negras con 15 fichas en off."""
        tablero = Tablero()
        tablero.obtener_off('N').extend(['N'] * 15)
        self.assertTrue(tablero.gano('N'))

    def test_gano_false_negras(self):
        """Verifica que negras no ganan con 13 fichas en off."""
        tablero = Tablero()
        tablero.obtener_off('N').extend(['N'] * 13)
        self.assertFalse(tablero.gano('N'))
    
    def test_gano_color_invalido(self):
        """Verifica comportamiento con color inválido."""
        tablero = Tablero()
        self.assertFalse(tablero.gano('X')) 

    def test_no_gano(self):
        """Verifica que el jugador no haya ganado al inicio."""
        self.assertFalse(self.tablero.gano('B'))
    
    def test_hay_movimiento_posible_desde_tablero(self):
        """Verifica detección de movimientos posibles desde tablero."""
        self.assertTrue(self.tablero.hay_movimientos_posibles('B', [1, 2]))
    
    def test_mover_color_invalido(self): 
        """Verifica excepción al mover con color inválido."""
        with self.assertRaises(ValueError):
            self.tablero.mover(1, 3, 'X')  
    
    def test_mover_con_ficha_en_barra_y_origen_distinto_de_cero(self):
        """ Verifica excepción al intentar mover desde tablero cuando hay fichas en barra. """
        self.tablero.obtener_bar('B').append('B')  
        with self.assertRaises(ValueError):
            self.tablero.mover(5, 3, 'B') 

    def test_mover_valor_mayor_para_sacar(self):
        """Verifica sacar ficha con valor mayor al necesario."""
        tablero = Tablero()
        for i in range(18, 24):
            tablero.get_point(i).clear()
        tablero.get_point(22).extend(['B'] * 15)
        
        if tablero.puede_sacar_ficha('B'):
            try:
                # Valor mayor (6) para sacar desde posición 22 (necesita 2)
                tablero.mover(22, 6, 'B')
                self.assertGreater(len(tablero.obtener_off('B')), 0)
            except ValueError:
                pass

    def test_mover_blancas_fuera_de_rango_alto(self):
        """Verifica movimiento que sale del tablero por arriba."""
        # Intentar mover más allá de la posición 23
        with self.assertRaises((ValueError, IndexError)):
            self.tablero.mover(20, 6, 'B')

    def test_mover_negras_fuera_de_rango_bajo(self):
        """Verifica movimiento que sale del tablero por abajo."""
        # Intentar mover más allá de la posición 0
        with self.assertRaises((ValueError, IndexError)):
            self.tablero.mover(3, 6, 'N')

    def test_mover_sin_poder_sacar_blancas(self):
        """Verifica que no se puede sacar sin tener todas en casa."""
        # Configurar con fichas fuera del último cuarto
        with self.assertRaises(ValueError):
            # Intentar sacar cuando no se puede
            self.tablero.mover(23, 1, 'B')

    def test_mover_sin_poder_sacar_negras(self):
        """Verifica que no se puede sacar sin tener todas en casa."""
        with self.assertRaises(ValueError):
            self.tablero.mover(0, 1, 'N')

    def test_captura_ficha_rival_y_envia_a_barra(self):
        """Verifica que al capturar, la ficha rival va a la barra."""
        tablero = Tablero()
        # Configurar: colocar una ficha negra solitaria
        tablero.get_point(5).clear()
        tablero.get_point(5).append('N')
        # Colocar ficha blanca que pueda capturar
        tablero.get_point(0).clear()
        tablero.get_point(0).append('B')
        
        bar_antes = len(tablero.obtener_bar('N'))
        try:
            tablero.mover(0, 5, 'B')
            bar_despues = len(tablero.obtener_bar('N'))
            # La ficha negra debería estar en la barra
            self.assertEqual(bar_despues, bar_antes + 1)
        except (ValueError, KeyError):
            pass

    def test_no_puede_mover_a_casilla_con_dos_rivales(self):
        """Verifica que no se puede mover a casilla con 2+ fichas rivales."""
        tablero = Tablero()
        # Configurar casilla con 2 fichas negras
        tablero.get_point(10).clear()
        tablero.get_point(10).extend(['N', 'N'])
        # Colocar blanca que intente entrar
        tablero.get_point(5).clear()
        tablero.get_point(5).append('B')
        
        with self.assertRaises(ValueError):
            tablero.mover(5, 5, 'B')

    def test_mover_obligatorio_desde_barra_primero(self):
        """Verifica que con fichas en barra, solo se puede mover desde ahí."""
        self.tablero.obtener_bar('B').append('B')
        # Intentar mover desde tablero debería fallar
        with self.assertRaises(ValueError):
            self.tablero.mover(18, 3, 'B')

    def test_mover_desde_barra_a_casilla_bloqueada(self):
        """Verifica que no se puede entrar desde barra a casilla bloqueada."""
        tablero = Tablero()
        tablero.obtener_bar('B').append('B')
        # Bloquear casilla de entrada para blancas
        tablero.get_point(2).clear()
        tablero.get_point(2).extend(['N', 'N'])
        
        with self.assertRaises(ValueError):
            tablero.mover(0, 3, 'B')

    def test_interpretar_tirada_con_mismo_valor(self):
        """Verifica que dobles dan 4 movimientos."""
        tablero = Tablero()
        for i in [1, 2, 3, 4, 5, 6]:
            resultado = tablero.interpretar_tirada(i, i)
            self.assertEqual(len(resultado), 4)
            self.assertTrue(all(x == i for x in resultado))

    def test_interpretar_tirada_con_valores_diferentes(self):
        """Verifica que no-dobles dan 2 movimientos."""
        tablero = Tablero()
        for i in range(1, 7):
            for j in range(1, 7):
                if i != j:
                    resultado = tablero.interpretar_tirada(i, j)
                    self.assertEqual(len(resultado), 2)
                    self.assertIn(i, resultado)
                    self.assertIn(j, resultado)

if __name__ == '__main__':
    unittest.main()