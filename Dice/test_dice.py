import unittest


class TestDice(unittest.TestCase):

    @patch('random.randint', side_effect=[5, 2])
    def test_tirar_devuelve_dos_valores(self, randint_patched):
        dice = Dice()
        dice.tirar()
        valores = dice.obtener_valores()
        self.assertEqual(len(valores), 2)
        self.assertEqual(valores[0], 5)
        self.assertEqual(valores[1], 2)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    
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