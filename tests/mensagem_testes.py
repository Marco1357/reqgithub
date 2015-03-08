import unittest
from unittest.mock import Mock


class Email():
    def enviar(self):
        print('Enviar email para todos usuário do sistema')


class EnviadorDeMensagem():
    def __init__(self):
        self.canal = Email()

    def enviar_mensagens(self):
        return self.canal.enviar()


class MensagemTests(unittest.TestCase):
    def test_enviar_mensagem(self):
        enviador_de_mensagem = EnviadorDeMensagem()
        canal_mock = Mock()
        enviador_de_mensagem.canal = canal_mock
        enviador_de_mensagem.enviar_mensagens()
        # Testes vão executar aqui abaixo
        canal_mock.enviar.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
