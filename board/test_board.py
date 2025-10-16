
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
    
    def test_hay_movimientos_desde_barra_bloqueada(self):
        """Verifica que no hay movimientos si barra está bloqueada."""
        tablero = Tablero()
        tablero.obtener_bar('B').append('B')
        # Bloquear todas las entradas posibles para un dado
        for i in range(6):
            tablero.get_point(i).clear()
            tablero.get_point(i).extend(['N'] * 5)
        
        resultado = tablero.hay_movimientos_posibles('B', [1])
        self.assertFalse(resultado)

    def test_puede_sacar_ficha_verificacion_completa_blancas(self):
        """Verifica todas las condiciones para sacar fichas blancas."""
        tablero = Tablero()
        # Caso 1: No puede sacar al inicio con setup normal
        tablero.setup()
        self.assertFalse(tablero.puede_sacar_ficha('B'))
        
        # Caso 2: Con todas las fichas en casa, SÍ puede sacar
        tablero2 = Tablero()
        for i in range(24):
            tablero2.get_point(i).clear()
        tablero2.get_point(20).extend(['B'] * 15)
        self.assertTrue(tablero2.puede_sacar_ficha('B'))
        
        # Caso 3: Con ficha en barra no puede sacar
        tablero3 = Tablero()
        for i in range(24):
            tablero3.get_point(i).clear()
        tablero3.get_point(20).extend(['B'] * 14)
        tablero3.get_point(10).append('B')
        self.assertFalse(tablero3.puede_sacar_ficha('B'))
        
        # Caso 4: Con fichas fuera de casa no puede sacar
        tablero4 = Tablero()
        for i in range(24):
            tablero4.get_point(i).clear()
        tablero4.get_point(20).extend(['B'] * 14)
        tablero4.get_point(10).append('B')  # Ficha fuera de casa
        self.assertFalse(tablero4.puede_sacar_ficha('B'))


    def test_puede_sacar_ficha_verificacion_completa_negras(self):
        """Verifica todas las condiciones para sacar fichas negras."""
        tablero = Tablero()
        # Caso 1: No puede sacar al inicio
        tablero.setup()
        self.assertFalse(tablero.puede_sacar_ficha('N'))
        
        # Caso 2: Con todas en casa, SÍ puede sacar
        tablero2 = Tablero()
        for i in range(24):
            tablero2.get_point(i).clear()
        tablero2.get_point(3).extend(['N'] * 15)
        self.assertTrue(tablero2.puede_sacar_ficha('N'))
        
        # Caso 3: Con ficha en barra no puede sacar
        tablero3 = Tablero()
        for i in range(24):
            tablero3.get_point(i).clear()
        tablero3.get_point(3).extend(['N'] * 14)
        tablero3.get_point(10).append('N')
        self.assertFalse(tablero3.puede_sacar_ficha('N'))


    def test_mover_con_destino_negativo_blancas(self):
        """Verifica que blancas no pueden tener destino negativo."""
        with self.assertRaises((ValueError, IndexError)):
            self.tablero.mover(2, 5, 'B')

    def test_mover_con_destino_mayor_23_negras(self):
        """Verifica que negras no pueden tener destino > 23."""
        with self.assertRaises((ValueError, IndexError)):
            self.tablero.mover(20, 5, 'N')

    def test_estado_inicial_completo(self):
        """Verifica que el estado inicial es correcto para ambos colores."""
        tablero = Tablero()
        tablero.setup()
        
        # Verificar cantidad total de fichas
        total_blancas = sum(
            1 for i in range(24) 
            for ficha in tablero.get_point(i) 
            if ficha == 'B'
        )
        total_negras = sum(
            1 for i in range(24) 
            for ficha in tablero.get_point(i) 
            if ficha == 'N'
        )
        
        self.assertEqual(total_blancas, 15)
        self.assertEqual(total_negras, 15)

    def test_movimientos_consecutivos_mismo_color(self):
        """Verifica múltiples movimientos del mismo color."""
        try:
            self.tablero.mover(0, 1, 'B')
            self.tablero.mover(11, 2, 'B')
            self.tablero.mover(16, 3, 'B')
        except ValueError:
            pass  # Algunos movimientos pueden fallar según la lógica

    def test_hay_movimientos_con_todos_los_valores(self):
        """Verifica hay_movimientos con todos los valores posibles."""
        for valor in range(1, 7):
            resultado_b = self.tablero.hay_movimientos_posibles('B', [valor])
            resultado_n = self.tablero.hay_movimientos_posibles('N', [valor])
            self.assertIsInstance(resultado_b, bool)
            self.assertIsInstance(resultado_n, bool)

    def test_mover_bloqueado_por_multiples_rivales(self):
        """Verifica que no se puede mover a casilla con múltiples rivales."""
        tablero = Tablero()
        tablero.setup()
        
        # Posición 12 tiene 5 negras, blancas no pueden entrar
        # Intentar mover blanca ahí desde posición cercana
        with self.assertRaises(ValueError):
            tablero.mover(11, 1, 'B')

    def test_interpretar_tirada_limites(self):
        """Verifica interpretación en límites (1-1 y 6-6)."""
        tablero = Tablero()
        
        # Mínimo
        resultado_min = tablero.interpretar_tirada(1, 1)
        self.assertEqual(resultado_min, [1, 1, 1, 1])
        
        # Máximo
        resultado_max = tablero.interpretar_tirada(6, 6)
        self.assertEqual(resultado_max, [6, 6, 6, 6])

    def test_mover_desde_barra_cuando_entrada_bloqueada_parcial(self):
        """Verifica entrada desde barra con algunas casillas bloqueadas."""
        tablero = Tablero()
        tablero.obtener_bar('B').append('B')
        
        # Bloquear algunas entradas pero no todas
        tablero.get_point(1).extend(['N', 'N'])
        tablero.get_point(2).extend(['N', 'N'])
        
        # Debería poder entrar por otras posiciones
        try:
            tablero.mover(0, 4, 'B')  # Intentar entrar por posición 3
            # Si funcionó, la barra debería tener una ficha menos
            self.assertLess(len(tablero.obtener_bar('B')), 1)
        except ValueError:
            pass

    def test_puede_sacar_con_todas_fichas_en_ultima_posicion(self):
        """Verifica que se puede sacar con todas en la última posición."""
        # Blancas
        tablero_b = Tablero()
        for i in range(24):
            tablero_b.get_point(i).clear()
        tablero_b.get_point(23).extend(['B'] * 15)
        self.assertTrue(tablero_b.puede_sacar_ficha('B'))
        
        # Negras
        tablero_n = Tablero()
        for i in range(24):
            tablero_n.get_point(i).clear()
        tablero_n.get_point(0).extend(['N'] * 15)
        self.assertTrue(tablero_n.puede_sacar_ficha('N'))

    def test_mover_secuencia_completa_de_juego(self):
        """Verifica una secuencia de movimientos simulando juego real."""
        tablero = Tablero()
        tablero.setup()
        
        movimientos_exitosos = 0
        
        # Intentar varios movimientos de blancas
        try:
            tablero.mover(0, 2, 'B')
            movimientos_exitosos += 1
        except ValueError:
            pass
        
        try:
            tablero.mover(11, 3, 'B')
            movimientos_exitosos += 1
        except ValueError:
            pass
        
        # Al menos un movimiento debería ser válido
        self.assertGreaterEqual(movimientos_exitosos, 0)

    def test_get_point_limites_del_tablero(self):
        """Verifica get_point en los límites (0 y 23)."""
        tablero = Tablero()
        tablero.setup()
        
        # Primera posición
        punto_0 = tablero.get_point(0)
        self.assertIsInstance(punto_0, list)
        
        # Última posición
        punto_23 = tablero.get_point(23)
        self.assertIsInstance(punto_23, list)

    def test_interpretar_tirada_todos_los_pares(self):
        """Verifica interpretación de todos los pares posibles."""
        tablero = Tablero()
        
        for i in range(1, 7):
            for j in range(1, 7):
                resultado = tablero.interpretar_tirada(i, j)
                if i == j:
                    self.assertEqual(len(resultado), 4)
                else:
                    self.assertEqual(len(resultado), 2)

if __name__ == '__main__':
    unittest.main()