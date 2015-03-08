import unittest
from unittest.mock import Mock


class Calculadora():
    def __init__(self, entrada=None, entrada2=None, sinal=None):
        self.sinal = sinal
        self.entrada2 = entrada2
        self.entrada = entrada
        self.operacoes_disponiveis = {}

    def adicionar_operacao(self, sinal, operacao):
        self.operacoes_disponiveis[sinal] = operacao

    def calcular(self):
        operacao = self.operacoes_disponiveis[self.sinal]
        resultado = operacao.calcular(self.entrada, self.entrada2)
        return resultado

    def obter_entradas(self):
        valor = input('Digite o primeiro número: ')
        self.entrada = int(valor)
        valor = input('Digite o sinal da operação desejada: ')
        self.sinal = valor
        valor = input('Digite o segundo número: ')
        self.entrada2 = int(valor)


def calcular(sinal, entrada, entrada2):
    if sinal == '+':
        return entrada + entrada2


class Subtracao():
    def calcular(self, entrada, entrada2):
        return entrada - entrada2


class CalculadoraTests(unittest.TestCase):
    def test_adicionar_operacao(self):
        calculadora = Calculadora()
        adicao = Adicao()
        calculadora.adicionar_operacao('+', adicao)
        self.assertDictEqual({'+': adicao}, calculadora.operacoes_disponiveis)
        subtracao = Subtracao()
        calculadora.adicionar_operacao('-', subtracao)
        self.assertDictEqual({'+': adicao, '-': subtracao}, calculadora.operacoes_disponiveis)

    def test_calcular_integracao(self):
        calculadora = Calculadora()
        adicao = Adicao()
        calculadora.adicionar_operacao('+', adicao)
        calculadora.entrada = 1
        calculadora.entrada2 = 2
        calculadora.sinal = '+'
        resultado = calculadora.calcular()
        self.assertEqual(3, resultado)

    def test_calcular(self):
        calculadora = Calculadora()
        operacao_mock = Mock()
        operacao_mock.calcular = Mock(return_value='Resultado de execucao do metodo calcular')
        calculadora.adicionar_operacao('+', operacao_mock)
        calculadora.entrada = 1
        calculadora.entrada2 = 2
        calculadora.sinal = '+'

        resultado = calculadora.calcular()
        operacao_mock.calcular.assert_called_once_with(1, 2)
        self.assertEqual('Resultado de execucao do metodo calcular', resultado)

    def test_subtracao_operacao(self):
        calculadora = Calculadora()
        subtracao = Subtracao()
        calculadora.adicionar_operacao('-', subtracao)
        calculadora.entrada = 1
        calculadora.entrada2 = 2
        calculadora.sinal = '-'
        resultado = calculadora.calcular()
        self.assertEqual(-1, resultado)


class Adicao():
    def calcular(self, entrada, entrada2):
        return entrada - entrada2


class OperacaoTests(unittest.TestCase):
    def test_adicao(self):
        adicao = Adicao()
        resultado = adicao.calcular(1, 2)
        self.assertEqual(3, resultado)
