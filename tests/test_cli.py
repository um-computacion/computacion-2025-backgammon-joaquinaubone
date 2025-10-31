"""Tests unitarios para el módulo CLI del juego de Backgammon.
Se enfoca en la lógica del flujo del juego, no en la salida de mensajes.
"""
import unittest
from unittest.mock import Mock, patch
from cli.cli import jugar


class TestCLI(unittest.TestCase):
    """Tests para verificar la lógica del CLI."""
    

    @patch('builtins.input', side_effect=['5', '7', '5', '3', '4', '4'])
    def test_rechaza_valor_no_en_tirada(self, _mock_input):
        """Verifica que rechaza valores que no están en la tirada actual."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_color.return_value = 'N'
        mock_jugador_n.obtener_simbolo.return_value = 'O'

       
        mock_juego.gano.side_effect = [
            False, False,
            False, False,   
            False, False,   
            True, False,  
            True            
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = [3, 4]
        mock_juego.hay_movimientos_posibles.return_value = True
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None
        
        
        mock_juego.mover.side_effect = [
            ValueError("El valor de pasos no está en la tirada actual."),
            None,
            None
        ]

        jugar(mock_juego)

        self.assertEqual(mock_juego.mover.call_count, 3)



    @patch('builtins.input', side_effect=['5', '3'])
    def test_condicion_victoria_verifica_ambos_colores(self, _mock_input):
        """Verifica que el bucle principal verifica victoria para ambos jugadores."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        
        mock_jugador_n = Mock()
        mock_jugador_n.obtener_color.return_value = 'N'
        mock_jugador_n.obtener_simbolo.return_value = 'O'

        
        mock_juego.gano.side_effect = [
            False, False,  
            True, False,   
            True            
        ]
        mock_juego.obtener_jugador_actual.return_value = mock_jugador_b
        mock_juego.dados.tirar.return_value = None
        mock_juego.interpretar_tirada.return_value = []
        mock_juego.hay_movimientos_posibles.return_value = False
        mock_juego.jugadores = {'B': mock_jugador_b, 'N': mock_jugador_n}
        mock_juego.tablero.mostrar.return_value = None

        jugar(mock_juego)

        self.assertGreater(mock_juego.gano.call_count, 2)

    
    @patch("builtins.print")
    @patch("builtins.input", return_value="5")
    def test_muestra_mensaje_victoria_final(self, _mock_input, mock_print):
        """Verifica que muestra mensaje de victoria al finalizar."""
        mock_juego = Mock()

        mock_jugador_b = Mock()
        mock_jugador_b.obtener_simbolo.return_value = 'X'
        mock_jugador_b.obtener_color.return_value = 'B'
        mock_juego.jugadores = {'B': mock_jugador_b}

        mock_juego.gano.return_value = True

        jugar(mock_juego)

        mock_print.assert_any_call(" ¡El jugador X (color: B) ha ganado! ")


if __name__ == '__main__':
    unittest.main()
