from idlelib.idle_test.test_searchengine import Mock
from unittest.case import TestCase


class Manada():
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def fazer_barulho(self, separador=None):
        barulhos = [a.barulho() for a in self.animais]
        if separador is not None:
            return separador.join(barulhos)
        return barulhos


class ManadaTests(TestCase):
    def test_barulhos(self):
        m = Mock()
        m.barulho = lambda: '1'
        m2 = Mock()
        m2.barulho = lambda: '2'

        manada = Manada()
        manada.adicionar_animal(m)
        manada.adicionar_animal(m2)

        self.assertListEqual(['1', '2'], manada.fazer_barulho())
        self.assertEqual('1,2', manada.fazer_barulho(','))
