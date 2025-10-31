"""Tests finales para cubrir las últimas líneas faltantes en game.py"""
import unittest
from core.game import Juego
from core.board import Tablero
from core.checker import Checker
from exceptions import ColorInvalidoException


class TestJuegoLineasFinales(unittest.TestCase):
    """Tests para cubrir las últimas líneas sin cobertura."""

    
    def test_obtener_jugador_actual_negro(self):
        """Verifica que obtener_jugador_actual retorna jugador correcto para N."""
        game = Juego()
        game.turno_actual = 'N'
        
        jugador = game.obtener_jugador_actual()
        
        self.assertEqual(jugador.obtener_color(), 'N')
        self.assertIs(jugador, game.jugadores['N'])

    def test_gano_lanza_excepcion_con_color_invalido(self):
        """Verifica que gano() lanza ColorInvalidoException."""
        game = Juego()
        
        with self.assertRaises(ColorInvalidoException):
            game.gano('Z')

    def test_mover_con_pasos_no_en_valores(self):
        """Verifica ValueError cuando pasos no está en la tirada."""
        game = Juego()
        tablero = Tablero()
        
        tablero.get_point(5).clear()
        tablero.get_point(5).append(Checker('B'))
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([1, 2])
        
        with self.assertRaises(ValueError) as context:
            game.mover(5, 5)  # 5 no está en [1, 2]
        
        self.assertIn("no está en la tirada", str(context.exception))

    def test_mover_append_a_off_blancas(self):
        """Verifica que la ficha se agrega a off al sacarla."""
        game = Juego()
        tablero = Tablero()
        
        # Todas en casa
        for i in range(24):
            tablero.get_point(i).clear()
        
        tablero.get_point(23).append(Checker('B'))
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([1, 2])
        
        game.mover(23, 1)
        self.assertEqual(len(tablero.obtener_off('B')), 1)

    def test_mover_rollback_desde_tablero(self):
        """Verifica rollback cuando movimiento desde tablero falla."""
        game = Juego()
        tablero = Tablero()
        
        tablero.get_point(5).clear()
        tablero.get_point(5).append(Checker('B'))
        
        tablero.get_point(8).clear()
        tablero.get_point(8).extend([Checker('N') for _ in range(3)])
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([3, 4])
        
        fichas_antes = len(tablero.get_point(5))
        
        with self.assertRaises(ValueError):
            game.mover(5, 3)
        
        self.assertEqual(len(tablero.get_point(5)), fichas_antes)

    def test_obtener_direccion_negras(self):
        """Verifica que __obtener_direccion retorna -1 para negras."""
        game = Juego()
        game.turno_actual = 'N'
        tablero = Tablero()
        
        tablero.get_point(20).clear()
        tablero.get_point(20).append(Checker('N'))
        tablero.get_point(18).clear()
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([2, 3])
        
        game.mover(20, 2)
        
        self.assertEqual(len(tablero.get_point(18)), 1)

    def test_calcular_destino_desde_barra_negras(self):
        """Verifica cálculo de destino desde barra para negras."""
        game = Juego()
        game.turno_actual = 'N'
        tablero = Tablero()
        
        tablero.obtener_bar('N').append(Checker('N'))
        tablero.get_point(20).clear()  
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([4, 5])
        
        game.mover(-1, 4)
        
        self.assertEqual(len(tablero.get_point(20)), 1)
    
    def test_es_movimiento_valido_captura_una_ficha(self):
        """Verifica captura de una sola ficha rival."""
        game = Juego()
        tablero = Tablero()
        
        tablero.get_point(5).clear()
        tablero.get_point(5).append(Checker('B'))
        
        tablero.get_point(8).clear()
        tablero.get_point(8).append(Checker('N'))
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([3, 4])
        
        game.mover(5, 3)
        
        self.assertEqual(len(tablero.obtener_bar('N')), 1)

    def test_sacar_de_barra_vacia(self):
        """Verifica error al intentar sacar de barra vacía."""
        game = Juego()
        tablero = Tablero()
        
        tablero.obtener_bar('B').clear()
        tablero.get_point(2).clear()
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([3, 4])
        
        with self.assertRaises(ValueError) as context:
            game.mover(-1, 3)
        
        self.assertIn("No hay fichas", str(context.exception))


    def test_sacar_de_tablero_sin_fichas(self):
        """Verifica error al sacar de tablero sin fichas."""
        game = Juego()
        tablero = Tablero()
        
        tablero.get_point(10).clear()
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([3, 4])
        
        with self.assertRaises(ValueError):
            game.mover(10, 3)

    def test_sacar_de_tablero_ficha_color_incorrecto(self):
        """Verifica error al sacar ficha de color incorrecto."""
        game = Juego()
        tablero = Tablero()
        
        # Turno blanco pero ficha negra
        tablero.get_point(10).clear()
        tablero.get_point(10).append(Checker('N'))
        
        game.tablero = tablero
        game.dados.obtener_valores().clear()
        game.dados.obtener_valores().extend([3, 4])
        
        with self.assertRaises(ValueError):
            game.mover(10, 3)

    def test_no_puede_salir_de_barra(self):
        """Verifica que retorna False cuando no puede salir de barra."""
        game = Juego()
        tablero = Tablero()
        
        tablero.obtener_bar('B').append(Checker('B'))
        
        for i in range(6):
            tablero.get_point(i).clear()
            tablero.get_point(i).extend([Checker('N') for _ in range(2)])
        
        game.tablero = tablero
        
        resultado = game.hay_movimientos_posibles('B', [1])
        
        self.assertFalse(resultado)

    def test_no_puede_mover_ficha_en_tablero(self):
        """Verifica que retorna False cuando no puede mover en tablero."""
        game = Juego()
        tablero = Tablero()
        
        for i in range(24):
            tablero.get_point(i).clear()
        
        tablero.get_point(10).append(Checker('B'))
        
        for i in range(11, 17):
            tablero.get_point(i).extend([Checker('N') for _ in range(2)])
        
        game.tablero = tablero
        
        resultado = game.hay_movimientos_posibles('B', [1, 2, 3, 4, 5, 6])
        
        # Línea 213 ejecutada
        self.assertFalse(resultado)

    def test_obtener_estado_tablero_pygame_completo(self):
        """Verifica obtener_estado_tablero_pygame con diferentes casos."""
        game = Juego()
        tablero = Tablero()
        
        for i in range(24):
            tablero.get_point(i).clear()
        
        tablero.get_point(5).extend([Checker('B') for _ in range(3)])
        tablero.get_point(10).extend([Checker('N') for _ in range(2)])

        
        game.tablero = tablero
        
        estado = game.obtener_estado_tablero_pygame()
        
        self.assertEqual(len(estado), 24)
        self.assertEqual(estado[5], ('white', 3))
        self.assertEqual(estado[10], ('black', 2))
        self.assertIsNone(estado[15])

    def test_obtener_cantidad_barra(self):
        """Verifica obtener_cantidad_barra."""
        game = Juego()
        tablero = Tablero()
        
        tablero.obtener_bar('B').extend([Checker('B') for _ in range(3)])
        
        game.tablero = tablero
        
        cantidad = game.obtener_cantidad_barra('B')
        
        self.assertEqual(cantidad, 3)

    def test_obtener_cantidad_off(self):
        """Verifica obtener_cantidad_off."""
        game = Juego()
        tablero = Tablero()
        
        tablero.obtener_off('N').extend([Checker('N') for _ in range(5)])
        
        game.tablero = tablero
        
        cantidad = game.obtener_cantidad_off('N')
        
        self.assertEqual(cantidad, 5)


if __name__ == '__main__':
    unittest.main()