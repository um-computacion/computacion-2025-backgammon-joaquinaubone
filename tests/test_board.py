
""" Módulo de pruebas unitarias para la clase Tablero del juego de backgammon."""
import unittest
from core.board import Tablero
from core.checker import Checker
from exceptions import ColorInvalidoException, PosNoExistenteException

class TestTablero(unittest.TestCase):
    """Clase de pruebas para Tablero."""
    
    def test_setup_inicial(self):
        """Verifica que se coloque cada pieza en su posición inicial."""
        tablero = Tablero()
        tablero.setup()

        punto_0 = tablero.get_point(0)
        self.assertEqual(len(punto_0), 2)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_0))

        punto_11 = tablero.get_point(11)
        self.assertEqual(len(punto_11), 5)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_11))

        punto_16 = tablero.get_point(16)
        self.assertEqual(len(punto_16), 3)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_16))

        punto_18 = tablero.get_point(18)
        self.assertEqual(len(punto_18), 5)
        self.assertTrue(all(f.obtener_color() == 'B' for f in punto_18))

        punto_23 = tablero.get_point(23)
        self.assertEqual(len(punto_23), 2)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_23))

        punto_12 = tablero.get_point(12)
        self.assertEqual(len(punto_12), 5)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_12))

        punto_7 = tablero.get_point(7)
        self.assertEqual(len(punto_7), 3)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_7))

        punto_5 = tablero.get_point(5)
        self.assertEqual(len(punto_5), 5)
        self.assertTrue(all(f.obtener_color() == 'N' for f in punto_5))

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
        with self.assertRaises(ColorInvalidoException):
            tablero.obtener_bar('X')
    
    def test_obtener_off_color_invalido(self):
        """Verifica excepción al pedir off con color inválido."""
        tablero = Tablero()
        with self.assertRaises(ColorInvalidoException):
            tablero.obtener_off('X')

    def test_obtener_off_blanca(self): 
        """Verifica que el off blanca esté vacío al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('B'), [])

    def test_obtener_off_negra(self): 
        """Verifica que el off negra esté vacío al inicio."""
        tablero = Tablero()
        self.assertEqual(tablero.obtener_off('N'), [])
    
    def test_mostrar_con_fichas_en_barra_blanca(self):
        """Verifica que mostrar() funciona con fichas en barra blanca."""
        tablero = Tablero()
        tablero.obtener_bar('B').append(Checker('B')) 
        tablero.mostrar()  


    def test_mostrar_con_fichas_en_barra_negra(self):
        """Verifica que mostrar() funciona con fichas en barra negra."""
        tablero = Tablero()
        tablero.obtener_bar('N').append(Checker('N')) 
        tablero.mostrar() 

    def test_get_point_posicion_limite_superior(self):
        """Verifica excepción cuando posición es >= 24."""
        tablero = Tablero()
        
        with self.assertRaises(PosNoExistenteException) as context:
            tablero.get_point(24)
        
        self.assertIn("El punto no existe en el tablero", str(context.exception))

    def test_get_point_posicion_negativa(self):
        """Verifica excepción cuando posición es negativa."""
        tablero = Tablero()
        
        with self.assertRaises(PosNoExistenteException) as context:
            tablero.get_point(-1)
        
        self.assertIn("El punto no existe en el tablero", str(context.exception))

    def test_obtener_bar_color_negro(self):
        """Verifica que obtener_bar('N') retorna la barra negra."""
        tablero = Tablero()
        
        tablero.obtener_bar('N').append(Checker('N'))
        
        barra_negra = tablero.obtener_bar('N')
        self.assertEqual(len(barra_negra), 1)
        self.assertEqual(barra_negra[0].obtener_color(), 'N')

    def test_obtener_bar_color_invalido_mayusculas(self):
        """Verifica excepción con color inválido en obtener_bar."""
        tablero = Tablero()
        
        with self.assertRaises(ColorInvalidoException) as context:
            tablero.obtener_bar('BLANCO')
        
        self.assertIn("Color no válido", str(context.exception))

    
    def test_obtener_off_color_negro(self):
        """Verifica que obtener_off('N') retorna el off negro."""
        tablero = Tablero()
        
        # Agregar ficha a off negro
        tablero.obtener_off('N').append(Checker('N'))
        
        off = tablero.obtener_off('N')
        self.assertEqual(len(off), 1)
        self.assertEqual(off[0].obtener_color(), 'N')

    def test_obtener_off_color_invalido_minusculas(self):
        """Verifica excepción con color inválido en obtener_off."""
        tablero = Tablero()
        
        with self.assertRaises(ColorInvalidoException) as context:
            tablero.obtener_off('b')  
        
        self.assertIn("Color no válido", str(context.exception))

    def test_mostrar_con_tablero_vacio(self):
        """Verifica que mostrar() funciona con tablero completamente vacío."""
        tablero = Tablero()
        # NO llamar setup() - tablero vacío
        
        try:
            tablero.mostrar()
        except (ValueError, IndexError) as e:
            self.fail(f"mostrar() falló con tablero vacío: {e}")

    def test_mostrar_con_fichas_en_todas_las_estructuras(self):
        """Verifica mostrar() con fichas en tablero, barras y off."""
        tablero = Tablero()
        tablero.setup()
        
        tablero.obtener_bar('B').append(Checker('B'))
        tablero.obtener_bar('N').append(Checker('N'))
        tablero.obtener_off('B').append(Checker('B'))
        tablero.obtener_off('N').append(Checker('N'))
        try:
            tablero.mostrar()
        except (ValueError, IndexError) as e:
            self.fail(f"mostrar() falló: {e}")

    def test_get_point_retorna_lista_mutable(self):
        """Verifica que get_point retorna lista que se puede modificar."""
        tablero = Tablero()
        
        punto = tablero.get_point(0)
        punto.append(Checker('B'))
        self.assertEqual(len(tablero.get_point(0)), 3)

    


    

    


if __name__ == '__main__':
    unittest.main()