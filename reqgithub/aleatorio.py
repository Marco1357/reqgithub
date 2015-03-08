from random import choice


def sortear_e_multiplicar_por_10(lista):
    return choice(lista) * 10


if __name__ == '__main__':
    resultado = sortear_e_multiplicar_por_10(['Renzo', 'Edimar', 'Amauri'])
    print(resultado)

