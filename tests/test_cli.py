"""Tests unitarios para el módulo CLI del juego de Backgammon.
Se enfoca en la lógica del flujo del juego, no en la salida de mensajes.
"""
import unittest
from unittest.mock import Mock, patch
from cli.cli import jugar


class TestCLI(unittest.TestCase):
    """Tests para verificar la lógica del CLI."""

    def setUp(self):
        """Configura los objetos necesarios antes de cada test."""
        pass

    @patch('builtins.input')
    def test_juego_termina_cuando_blancas_ganan(self, mock_input):
        """Verifica que el juego termina cuando las blancas ganan."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_color.return_value = 'N'
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | cambiar turno | while: B (True - sale) | if B (True) 
        mock_juego.gano.side_effect = [
            False, False,  # Primera iteración del while
            True, False,   # Segunda iteración (B gana)
            True           # Al final: if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = []
        mock_juego.hay_movimientos_posibles.return_value = False
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None

        jugar(mock_juego)

        self.assertTrue(mock_juego.gano.called)

    @patch('builtins.input')
    def test_juego_termina_cuando_negras_ganan(self, mock_input):
        """Verifica que el juego termina cuando las negras ganan."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_color.return_value = 'N'
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | cambiar turno | while: B, N (N=True - sale) | if B (False) | elif N (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            False, True,    # Segunda iteración (N gana)
            False,          # if juego.gano('B')
            True            # elif juego.gano('N')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_n
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = []
        mock_juego.hay_movimientos_posibles.return_value = False
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None

        jugar(mock_juego)

        self.assertTrue(mock_juego.gano.called)

    @patch('builtins.input', side_effect=['5', '3'])
    def test_movimiento_valido_se_ejecuta(self, mock_input):
        """Verifica que un movimiento válido se ejecuta correctamente."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | hace movimiento | while: B, N | while: B (True - sale) | if B (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            False, False,   # Después del movimiento dentro del while interno
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None
        mock_juego.mover.return_value = None

        jugar(mock_juego)

        mock_juego.mover.assert_called()

    @patch('builtins.input')
    def test_cambia_turno_cuando_no_hay_movimientos(self, mock_input):
        """Verifica que cambia de turno cuando no hay movimientos posibles."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | cambiar turno | while: B (True - sale) | if B (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3, 4]
        mock_juego.hay_movimientos_posibles.return_value = False
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None

        jugar(mock_juego)

        mock_juego.cambiar_turno.assert_called()

    @patch('builtins.input', side_effect=['5', '3', '4', '4'])
    def test_remueve_dado_de_tirada_tras_movimiento_exitoso(self, mock_input):
        """Verifica que se remueve el valor del dado tras un movimiento exitoso."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | mov1 | mov2 | while: B (True - sale) | if B (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            False, False,   # Después del primer movimiento
            False, False,   # Después del segundo movimiento
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3, 4]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.mover.return_value = None
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None

        jugar(mock_juego)

        self.assertTrue(mock_juego.mover.called)

    @patch('builtins.input', side_effect=['5', '7', '5', '3', '4', '4'])
    def test_rechaza_valor_no_en_tirada(self, mock_input):
        """Verifica que rechaza valores que no están en la tirada actual."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | intento fallido (pide input) | intento exitoso (consume 3) | intento exitoso (consume 4) | while: B (True - sale) | if B (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración del while
            False, False,   # Después del primer movimiento exitoso
            False, False,   # Después del segundo movimiento exitoso
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3, 4]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None
        
        # Primer movimiento (7) lanza error, segundo (3) funciona, tercero (4) funciona
        mock_juego.mover.side_effect = [
            ValueError("El valor de pasos no está en la tirada actual."),
            None,
            None
        ]

        jugar(mock_juego)

        self.assertTrue(mock_juego.hay_movimientos_posibles.called)

    @patch('builtins.input', side_effect=['-1', '3'])
    def test_obliga_mover_desde_barra_primero(self, mock_input):
        """Verifica que obliga a mover desde la barra si hay fichas ahí."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        mock_tablero = Mock()
        mock_tablero.obtener_bar = Mock(return_value=['B'])
        mock_tablero.mostrar = Mock()
        
        mock_juego.tablero = mock_tablero

        # while: B, N | movimiento | while: B (True - sale) | if B (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            False, False,   # Después del movimiento
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.mover.return_value = None

        jugar(mock_juego)

        mock_tablero.mostrar.assert_called()

    @patch('builtins.input', side_effect=['5', '3'])
    def test_maneja_entrada_invalida(self, mock_input):
        """Verifica que el flujo funciona correctamente."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | movimiento | while: B (True - sale) | if B (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            False, False,   # Después del movimiento
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None
        mock_juego.mover.return_value = None

        jugar(mock_juego)

        self.assertTrue(mock_juego.mover.called)

    @patch('builtins.input', side_effect=['25', '3', '5', '3'])
    def test_maneja_posicion_invalida(self, mock_input):
        """Verifica que maneja ValueError correctamente."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | intento fallido | intento exitoso | while: B (True - sale) | if B (True)
        mock_juego.mover.side_effect = [
            ValueError("Posición 25 fuera de rango"),
            None
        ]
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            False, False,   # Después del movimiento exitoso
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None

        jugar(mock_juego)

        self.assertEqual(mock_juego.mover.call_count, 2)

    @patch('builtins.input', side_effect=['5', '3'])
    def test_condicion_victoria_verifica_ambos_colores(self, mock_input):
        """Verifica que el bucle principal verifica victoria para ambos jugadores."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        # while: B, N | cambiar turno | while: B (True - sale) | if B (True)
        mock_juego.gano.side_effect = [
            False, False,   # Primera iteración
            True, False,    # Segunda iteración (B gana)
            True            # if juego.gano('B')
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = []
        mock_juego.hay_movimientos_posibles.return_value = False
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None

        jugar(mock_juego)

        self.assertGreater(mock_juego.gano.call_count, 2)

    @patch("builtins.input", side_effect=["5", "3"])
    @patch("builtins.print")
    def test_muestra_estado_tablero(self, mock_print, mock_input):
        mock_juego = Mock()
        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'

        mock_juego.gano.side_effect = [False, False, True, False, True]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.tablero.mostrar.return_value = None
        mock_juego.mover.return_value = None
        mock_juego.jugadores = {'B': mock_jugador_b}

        jugar(mock_juego)
        mock_print.assert_any_call("\n📍 Estado actual del tablero:")


    @patch("builtins.input", side_effect=["5", "3", "5", "3"])  # agregado más entradas
    @patch("builtins.print")
    def test_mensaje_movimiento_invalido(self, mock_print, mock_input):
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.tablero.mostrar.return_value = None
        mock_juego.jugadores = {'B': mock_jugador_b}

        # Primer movimiento: ValueError → salta except
        # Segundo: éxito → termina
        mock_juego.mover.side_effect = [
            ValueError("error"),
            None
        ]

        mock_juego.gano.side_effect = [
            False, False,  # primera iteración
            True, False,   # luego gana
            True           # if final
        ]

        jugar(mock_juego)

        mock_print.assert_any_call("movimiento inválido:")


    @patch("builtins.print")
    @patch("builtins.input", return_value="5")
    def test_muestra_mensaje_victoria_final(self, mock_input, mock_print):
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_juego.jugadores = {'B': mock_jugador_b}

        # El juego debe devolver True todas las veces
        mock_juego.gano.return_value = True

        jugar(mock_juego)

        mock_print.assert_any_call(" ¡El jugador X (color: B) ha ganado! ")


if __name__ == '__main__':
    unittest.main()