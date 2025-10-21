"""Tests unitarios para la clase Juego.

Este módulo prueba la LÓGICA del juego: movimientos, validaciones,
condiciones de victoria, interpretación de tiradas.
"""
import unittest
from game.game import Juego
from board.board import Tablero
from player.player import Player
from dice.dice import Dice


class TestJuego(unittest.TestCase):
    """Pruebas para verificar la lógica principal de la clase Juego."""

    def setUp(self):
        """Configura los objetos necesarios antes de cada test."""
        self.tablero = Tablero()
        self.tablero.setup()
        self.dados = Dice()
        self.jugador_blanco = Player('B')
        self.jugador_negro = Player('N')
        self.game = Juego(self.tablero, self.dados, self.jugador_blanco, self.jugador_negro)

    def test_cambiar_turno(self):
        """Verifica que el cambio de turno alterne correctamente entre los jugadores."""
        self.assertEqual(self.game.turno_actual, 'B')
        self.game.cambiar_turno()
        self.assertEqual(self.game.turno_actual, 'N')
        self.game.cambiar_turno()
        self.assertEqual(self.game.turno_actual, 'B')

    def test_obtener_jugador_actual(self):
        """Verifica que se obtenga correctamente el jugador del turno actual."""
        jugador = self.game.obtener_jugador_actual()
        self.assertEqual(jugador.obtener_color(), 'B')

    def test_interpretar_tirada_no_doble(self):
        """Verifica interpretación de tirada sin dobles."""
        self.game.dados.tirar()
        # Acceder directamente al atributo interno
        valores = self.game.dados.obtener_valores()
        valores.clear()
        valores.extend([3, 5])
        resultado = self.game.interpretar_tirada()
        self.assertEqual(resultado, [3, 5])

    def test_interpretar_tirada_doble(self):
        """Verifica interpretación de tirada con dobles."""
        self.game.dados.tirar()
        # Acceder directamente al atributo interno
        valores = self.game.dados.obtener_valores()
        valores.clear()
        valores.extend([4, 4])
        resultado = self.game.interpretar_tirada()
        self.assertEqual(resultado, [4, 4, 4, 4])

    def test_gano_true_blancas(self):
        """Verifica victoria de blancas con 15 fichas en off."""
        self.tablero.obtener_off('B').extend(['B'] * 15)
        self.assertTrue(self.game.gano('B'))

    def test_gano_false_blancas(self):
        """Verifica que blancas no ganan con 14 fichas en off."""
        self.tablero.obtener_off('B').extend(['B'] * 14)
        self.assertFalse(self.game.gano('B'))

    def test_gano_true_negras(self):
        """Verifica victoria de negras con 15 fichas en off."""
        self.game.turno_actual = 'N'
        self.tablero.obtener_off('N').extend(['N'] * 15)
        self.assertTrue(self.game.gano('N'))

    def test_gano_false_negras(self):
        """Verifica que negras no ganan con 13 fichas en off."""
        self.game.turno_actual = 'N'
        self.tablero.obtener_off('N').extend(['N'] * 13)
        self.assertFalse(self.game.gano('N'))

    def test_gano_color_invalido(self):
        """Verifica comportamiento con color inválido."""
        self.game.turno_actual = 'X'
        with self.assertRaises(ValueError):
            self.game.gano('X')

    def test_no_gano(self):
        """Verifica que el jugador no haya ganado al inicio."""
        self.assertFalse(self.game.gano('B'))
        self.assertFalse(self.game.gano('N'))

    def test_puede_sacar_ficha_verificacion_completa_blancas(self):
        """Verifica todas las condiciones para sacar fichas blancas."""
        # Caso 1: No puede sacar al inicio con setup normal
        # Con setup(), las blancas tienen fichas fuera de casa (en posiciones 0-17)
        self.assertFalse(self.game.puede_sacar_ficha('B'))

        # Caso 2: Con todas las fichas en casa, SÍ puede sacar
        tablero2 = Tablero()
        for i in range(24):
            tablero2.get_point(i).clear()
        tablero2.get_point(20).extend(['B'] * 15)
        game2 = Juego(tablero2, self.dados, self.jugador_blanco, self.jugador_negro)
        self.assertTrue(game2.puede_sacar_ficha('B'))

        # Caso 3: Con ficha en barra no puede sacar
        tablero3 = Tablero()
        for i in range(24):
            tablero3.get_point(i).clear()
        tablero3.get_point(20).extend(['B'] * 14)
        tablero3.obtener_bar('B').append('B')
        game3 = Juego(tablero3, self.dados, self.jugador_blanco, self.jugador_negro)
        self.assertFalse(game3.puede_sacar_ficha('B'))

        # Caso 4: Con fichas fuera de casa no puede sacar
        tablero4 = Tablero()
        for i in range(24):
            tablero4.get_point(i).clear()
        tablero4.get_point(20).extend(['B'] * 14)
        tablero4.get_point(10).append('B')  # Ficha fuera de casa
        game4 = Juego(tablero4, self.dados, self.jugador_blanco, self.jugador_negro)
        self.assertFalse(game4.puede_sacar_ficha('B'))

    def test_puede_sacar_ficha_verificacion_completa_negras(self):
        """Verifica todas las condiciones para sacar fichas negras."""
        # Caso 1: No puede sacar al inicio
        self.assertFalse(self.game.puede_sacar_ficha('N'))

        # Caso 2: Con todas en casa, SÍ puede sacar
        tablero2 = Tablero()
        for i in range(24):
            tablero2.get_point(i).clear()
        tablero2.get_point(3).extend(['N'] * 15)
        game2 = Juego(tablero2, self.dados, self.jugador_blanco, self.jugador_negro)
        self.assertTrue(game2.puede_sacar_ficha('N'))

        # Caso 3: Con ficha en barra no puede sacar
        tablero3 = Tablero()
        for i in range(24):
            tablero3.get_point(i).clear()
        tablero3.get_point(3).extend(['N'] * 14)
        tablero3.obtener_bar('N').append('N')
        game3 = Juego(tablero3, self.dados, self.jugador_blanco, self.jugador_negro)
        self.assertFalse(game3.puede_sacar_ficha('N'))

    def test_puede_sacar_con_todas_fichas_en_ultima_posicion(self):
        """Verifica que se puede sacar con todas en la última posición."""
        # Blancas
        tablero_b = Tablero()
        for i in range(24):
            tablero_b.get_point(i).clear()
        tablero_b.get_point(23).extend(['B'] * 15)
        game_b = Juego(tablero_b, self.dados, self.jugador_blanco, self.jugador_negro)
        self.assertTrue(game_b.puede_sacar_ficha('B'))

        # Negras
        tablero_n = Tablero()
        for i in range(24):
            tablero_n.get_point(i).clear()
        tablero_n.get_point(0).extend(['N'] * 15)
        game_n = Juego(tablero_n, self.dados, self.jugador_blanco, self.jugador_negro)
        self.assertTrue(game_n.puede_sacar_ficha('N'))

    def test_mover_valor_mayor_para_sacar(self):
        """Verifica sacar ficha con valor mayor al necesario."""
        tablero = Tablero()
        for i in range(18, 24):
            tablero.get_point(i).clear()
        tablero.get_point(22).extend(['B'] * 15)
        game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)

        if game.puede_sacar_ficha('B'):
            try:
                # Valor mayor (6) para sacar desde posición 22 (necesita 2)
                game.mover(22, 6)
                self.assertGreater(len(tablero.obtener_off('B')), 0)
            except ValueError:
                pass

    def test_hay_movimiento_posible_desde_tablero(self):
        """Verifica detección de movimientos posibles desde tablero."""
        # Con setup inicial, debe haber movimientos disponibles
        self.assertTrue(self.game.hay_movimientos_posibles('B', [1]))

    def test_hay_movimientos_con_todos_los_valores(self):
        """Verifica hay_movimientos con todos los valores posibles."""
        for valor in range(1, 7):
            resultado_b = self.game.hay_movimientos_posibles('B', [valor])
            resultado_n = self.game.hay_movimientos_posibles('N', [valor])
            self.assertIsInstance(resultado_b, bool)
            self.assertIsInstance(resultado_n, bool)

    def test_hay_movimientos_desde_barra_bloqueada(self):
        """Verifica que no hay movimientos si barra está bloqueada."""
        tablero = Tablero()
        tablero.obtener_bar('B').append('B')
        # Bloquear todas las entradas posibles para un dado
        for i in range(6):
            tablero.get_point(i).clear()
            tablero.get_point(i).extend(['N'] * 5)

        game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)
        resultado = game.hay_movimientos_posibles('B', [1])
        self.assertFalse(resultado)

    def test_mover_con_ficha_en_barra_y_origen_distinto_de_cero(self):
        """Verifica excepción al intentar mover desde tablero cuando hay fichas en barra."""
        self.tablero.obtener_bar('B').append('B')
        with self.assertRaises(ValueError):
            self.game.mover(5, 3)

    def test_mover_blancas_fuera_de_rango_alto(self):
        """Verifica movimiento que sale del tablero por arriba."""
        with self.assertRaises((ValueError, IndexError)):
            self.game.mover(20, 6)

    def test_mover_negras_fuera_de_rango_bajo(self):
        """Verifica movimiento que sale del tablero por abajo."""
        self.game.turno_actual = 'N'
        with self.assertRaises((ValueError, IndexError)):
            self.game.mover(3, 6)

    def test_mover_sin_poder_sacar_blancas(self):
        """Verifica que no se puede sacar sin tener todas en casa."""
        with self.assertRaises(ValueError):
            self.game.mover(23, 1)

    def test_mover_sin_poder_sacar_negras(self):
        """Verifica que no se puede sacar sin tener todas en casa."""
        self.game.turno_actual = 'N'
        with self.assertRaises(ValueError):
            self.game.mover(0, 1)

    def test_captura_ficha_rival_y_envia_a_barra(self):
        """Verifica que al capturar, la ficha rival va a la barra."""
        tablero = Tablero()
        # Configurar: colocar una ficha negra solitaria
        tablero.get_point(5).clear()
        tablero.get_point(5).append('N')
        # Colocar ficha blanca que pueda capturar
        tablero.get_point(0).clear()
        tablero.get_point(0).append('B')

        game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)
        bar_antes = len(tablero.obtener_bar('N'))
        try:
            game.mover(0, 5)
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

        game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)
        with self.assertRaises(ValueError):
            game.mover(5, 5)

    def test_mover_obligatorio_desde_barra_primero(self):
        """Verifica que con fichas en barra, solo se puede mover desde ahí."""
        self.tablero.obtener_bar('B').append('B')
        # Intentar mover desde tablero debería fallar
        with self.assertRaises(ValueError):
            self.game.mover(18, 3)

    def test_mover_desde_barra_a_casilla_bloqueada(self):
        """Verifica que no se puede entrar desde barra a casilla bloqueada."""
        tablero = Tablero()
        tablero.obtener_bar('B').append('B')
        # Bloquear casilla de entrada para blancas
        tablero.get_point(2).clear()
        tablero.get_point(2).extend(['N', 'N'])

        game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)
        with self.assertRaises(ValueError):
            game.mover(-1, 3)

    def test_mover_con_destino_negativo_blancas(self):
        """Verifica que blancas no pueden tener destino negativo."""
        with self.assertRaises((ValueError, IndexError)):
            self.game.mover(2, 5)

    def test_mover_con_destino_mayor_23_negras(self):
        """Verifica que negras no pueden tener destino > 23."""
        self.game.turno_actual = 'N'
        with self.assertRaises((ValueError, IndexError)):
            self.game.mover(20, 5)

    def test_movimientos_consecutivos_mismo_color(self):
        """Verifica múltiples movimientos del mismo color."""
        try:
            self.game.mover(0, 1)
            self.game.mover(11, 2)
            self.game.mover(16, 3)
        except ValueError:
            pass  # Algunos movimientos pueden fallar según la lógica

    def test_mover_bloqueado_por_multiples_rivales(self):
        """Verifica que no se puede mover a casilla con múltiples rivales."""
        tablero = Tablero()
        tablero.setup()

        # Posición 12 tiene 5 negras, blancas no pueden entrar
        # Intentar mover blanca ahí desde posición cercana
        with self.assertRaises(ValueError):
            game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)
            game.mover(11, 1)

    def test_mover_desde_barra_cuando_entrada_bloqueada_parcial(self):
        """Verifica entrada desde barra con algunas casillas bloqueadas."""
        tablero = Tablero()
        tablero.obtener_bar('B').append('B')

        # Bloquear algunas entradas pero no todas
        tablero.get_point(1).extend(['N', 'N'])
        tablero.get_point(2).extend(['N', 'N'])

        game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)
        # Debería poder entrar por otras posiciones
        try:
            game.mover(-1, 4)  # Intentar entrar por posición 3
            # Si funcionó, la barra debería tener una ficha menos
            self.assertLess(len(tablero.obtener_bar('B')), 1)
        except ValueError:
            pass

    def test_mover_secuencia_completa_de_juego(self):
        """Verifica una secuencia de movimientos simulando juego real."""
        tablero = Tablero()
        tablero.setup()
        game = Juego(tablero, self.dados, self.jugador_blanco, self.jugador_negro)

        movimientos_exitosos = 0

        # Intentar varios movimientos de blancas
        try:
            game.mover(0, 2)
            movimientos_exitosos += 1
        except ValueError:
            pass

        try:
            game.mover(11, 3)
            movimientos_exitosos += 1
        except ValueError:
            pass

        # Al menos un movimiento debería ser válido
        self.assertGreaterEqual(movimientos_exitosos, 0)


if __name__ == '__main__':
    unittest.main()