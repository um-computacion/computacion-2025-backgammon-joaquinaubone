import unittest
from dice.dice import Dice  

class TestDice(unittest.TestCase):

    def test_tirar_dado(self):
        dado = Dice()
        dado.tirar()
        valores = dado.obtener_valores() 
        self.assertEqual(len(valores), 2)
        self.assertTrue(all(1 <= val <= 6 for val in valores))
    
    def test_resetear_limpia_valores(self):
        dado = Dice()
        dado.tirar()
        self.assertGreater(len(dado.obtener_valores()), 0)  
        dado.resetear()
        self.assertEqual(dado.obtener_valores(), [])        

    def test_sin_valores_devuelve_true_si_vacio(self):
        dado = Dice()
        self.assertTrue(dado.sin_valores())                
        dado.tirar()
        self.assertFalse(dado.sin_valores())                
        dado.resetear()
        self.assertTrue(dado.sin_valores())                


if __name__ == '__main__':
    unittest.main()