import unittest


class Email():
    def enviar(self):
        print('Enviar email para todos usuário do sistema')


class EnviadorDeMensagem():
    def __init__(self):
        self.canal = Email()

    def enviar_mensagens(self):
        return self.canal.enviar()

class CanalMock():
    def __init__(self):
        self.enviar_executado = False

    def enviar(self):
        self.enviar_executado = True


class MensagemTests(unittest.TestCase):
    def test_enviar_mensagem(self):
        enviador_de_mensagem = EnviadorDeMensagem()
        canal_mock = CanalMock()
        enviador_de_mensagem.canal = canal_mock
        enviador_de_mensagem.enviar_mensagens()
        # Testes vão executar aqui abaixo
        self.assertTrue(canal_mock.enviar_executado)

if __name__=='__main__':
    unittest.main()
