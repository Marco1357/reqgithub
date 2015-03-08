from unittest.mock import Mock

mock = Mock()

mock.enviar()
mock.enviar.assert_called_once_with()

mock.a(4, 5)
mock.a.assert_called_once_with(4, 6)