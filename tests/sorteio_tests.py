from asyncio.test_utils import TestCase
from idlelib.idle_test.test_searchengine import Mock
from unittest.mock import patch, Mock
from reqgithub.aleatorio import sortear_e_multiplicar_por_10


class SortearTests(TestCase):
    @patch('reqgithub.aleatorio.choice')
    def test_sorteio(self, choice):
        choice.return_value = 1
        resultado = sortear_e_multiplicar_por_10([1, 2, 3, 4, 5, 6])
        self.assertEqual(10, resultado)
        choice.assert_called_once_with([1, 2, 3, 4, 5, 6])
