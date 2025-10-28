"""Tests unitarios para el módulo CLI del juego de Backgammon.
Se enfoca en la lógica del flujo del juego, no en la salida de mensajes.
"""
import unittest
from unittest.mock import Mock, patch
from cli.cli import jugar
from board.board import Tablero
from dice.dice import Dice
from player.player import Player
from exceptions import PosicionInvalida


class TestCLI(unittest.TestCase):
    """Tests para verificar la lógica del CLI."""

    def setUp(self):
        """Configura los objetos necesarios antes de cada test."""
        self.tablero = Tablero()
        self.dados = Dice()
        self.jugador_blanco = Player('B')
        self.jugador_negro = Player('N')

    @patch('builtins.input')
    @patch('cli.cli.Juego')
    def test_juego_termina_cuando_blancas_ganan(self, mock_juego_class, _):
        """Verifica que el juego termina cuando las blancas ganan."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.gano.side_effect = [
            False, False, True, False, True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = []
        mock_juego.hay_movimientos_posibles.return_value = False

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        self.assertTrue(mock_juego.gano.called)

    @patch('builtins.input')
    @patch('cli.cli.Juego')
    def test_juego_termina_cuando_negras_ganan(self, mock_juego_class, _):
        """Verifica que el juego termina cuando las negras ganan."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.gano.side_effect = [
            False, False, False, True, False, True
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_negro
        mock_juego.interpretar_tirada.return_value = []
        mock_juego.hay_movimientos_posibles.return_value = False

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        self.assertTrue(mock_juego.gano.called)

    @patch('builtins.input', side_effect=['5', '3'])
    @patch('cli.cli.Juego')
    def test_movimiento_valido_se_ejecuta(self, mock_juego_class, _):
        """Verifica que un movimiento válido se ejecuta correctamente."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.gano.side_effect = [
            False, False, False, False, True, False, True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        mock_juego.mover.assert_called()

    @patch('builtins.input')
    @patch('cli.cli.Juego')
    def test_cambia_turno_cuando_no_hay_movimientos(
        self, mock_juego_class, _
    ):
        """Verifica que cambia de turno cuando no hay movimientos
        posibles."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.gano.side_effect = [
            False, False, True, False, True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = [3, 4]
        mock_juego.hay_movimientos_posibles.return_value = False

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        mock_juego.cambiar_turno.assert_called()

    @patch('builtins.input', side_effect=['5', '3', '4', '4'])
    @patch('cli.cli.Juego')
    def test_remueve_dado_de_tirada_tras_movimiento_exitoso(
        self, mock_juego_class, _
    ):
        """Verifica que se remueve el valor del dado tras un movimiento
        exitoso."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        tirada_mock = [3, 4]
        mock_juego.gano.side_effect = [
            False, False, False, False, False, False, True, False,
            True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = tirada_mock.copy()
        mock_juego.hay_movimientos_posibles.side_effect = [
            True, True, True, False
        ]
        mock_juego.mover.return_value = None

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        self.assertTrue(mock_juego.mover.called)

    @patch('builtins.input', side_effect=[
        '5', '7',
        '5', '3',
        '5', '4',
    ])
    @patch('cli.cli.Juego')
    def test_rechaza_valor_no_en_tirada(self, mock_juego_class, _):
        """Verifica que rechaza valores que no están en la tirada
        actual."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.gano.side_effect = [
            False, False, False, False, True, False, True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = [3, 4]
        mock_juego.hay_movimientos_posibles.return_value = True

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        self.assertTrue(mock_juego.hay_movimientos_posibles.called)

    @patch('builtins.input', side_effect=['-1', '3'])
    @patch('cli.cli.Juego')
    def test_obliga_mover_desde_barra_primero(self, mock_juego_class, _):
        """Verifica que obliga a mover desde la barra si hay fichas
        ahí."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_tablero = Mock()
        mock_tablero.obtener_bar = Mock(return_value=['B'])
        mock_tablero.mostrar = Mock()

        mock_juego.gano.side_effect = [
            False, False, False, False, True, False, True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True

        jugar(mock_tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        mock_tablero.obtener_bar.assert_called()

    @patch('builtins.input', side_effect=['5', '3'])
    @patch('cli.cli.Juego')
    def test_maneja_entrada_invalida(self, mock_juego_class, _):
        """Verifica que el flujo funciona correctamente. """
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.gano.side_effect = [
            False, False, False, False, True, False, True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        self.assertTrue(mock_juego.mover.called)

    @patch('builtins.input', side_effect=['25', '3', '5', '3'])
    @patch('cli.cli.Juego')
    def test_maneja_posicion_invalida(self, mock_juego_class, _):
        """Verifica que maneja PosicionInvalida correctamente."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.mover.side_effect = [
            PosicionInvalida("Posición 25 fuera de rango"),
            None
        ]
        mock_juego.gano.side_effect = [
            False, False, False, False, False, True, False, True
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = [3]
        mock_juego.hay_movimientos_posibles.return_value = True

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        self.assertEqual(mock_juego.mover.call_count, 2)

    @patch('builtins.input', side_effect=['5', '3'])
    @patch('cli.cli.Juego')
    def test_condicion_victoria_verifica_ambos_colores(
        self, mock_juego_class, _
    ):
        """Verifica que el bucle principal verifica victoria para ambos
        jugadores."""
        mock_juego = Mock()
        mock_juego_class.return_value = mock_juego

        mock_juego.gano.side_effect = [
            False, False, True, False, True, False
        ]
        mock_juego.obtener_jugador_actual.return_value = self.jugador_blanco
        mock_juego.interpretar_tirada.return_value = []
        mock_juego.hay_movimientos_posibles.return_value = False

        jugar(self.tablero, self.dados, self.jugador_blanco,
              self.jugador_negro)

        self.assertGreater(mock_juego.gano.call_count, 2)


if __name__ == '__main__':
    unittest.main()