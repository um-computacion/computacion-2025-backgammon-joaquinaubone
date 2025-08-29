import unittest
from Dice.dice import Dice  

class TestDice(unittest.TestCase):

    def test_tirar_dado(self):
        dado = Dice()
        dado.tirar()
        valores = dado.obtener_valores() 
        self.assertEqual(len(valores), 2)
        self.assertTrue(all(1 <= val <= 6 for val in valores))

if __name__ == '__main__':
    unittest.main()