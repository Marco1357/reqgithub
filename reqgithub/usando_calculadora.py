from calculadora_extendida import CalculadoraHP
from calculadora_tests import Adicao


calculadora = CalculadoraHP()
calculadora.obter_entradas()
calculadora.adicionar_operacao('+', Adicao())


class Multiplicacao():
    def calcular(self, e, e2):
        return e * e2


calculadora.adicionar_operacao('*', Multiplicacao())
print(calculadora.calcular())