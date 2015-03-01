import unittest


def soma(parcela, parcela2):
    if isinstance(parcela,(int, float)):
        return parcela + parcela2
    raise TypeError('Deve ser to tipo int ou float')



class SomaTests(unittest.TestCase):
    def test_numeros_inteiros(self):
        resultado = soma(1, 2)
        self.assertEqual(3, resultado)
        self.assertEqual(-2, soma(4, -6))

    def test_numeros_reais(self):
        self.assertAlmostEqual(0.3, soma(0.1, 0.2))

    def test_strings(self):
        self.assertRaises(TypeError, soma,'Renzo ','Nuccitelli')


print(__name__)
if __name__ == '__main__':
    unittest.main()