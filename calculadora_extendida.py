from calculadora_tests import Calculadora


class CalculadoraHP(Calculadora):
    def obter_entradas(self):
        valor = input('Digite o sinal da operação desejada: ')
        self.sinal = valor
        valor = input('Digite o primeiro número: ')
        self.entrada = int(valor)
        valor = input('Digite o segundo número: ')
        self.entrada2 = int(valor)