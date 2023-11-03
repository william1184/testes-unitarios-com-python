import sys
from unittest import TestCase, mock
from unittest.mock import MagicMock


# CLASSE COM TESTE FUNCIONAIS COM NOMES MELHORES E TESTA COMPORTAMENTO MAS:
# POSSUI CODIGO DUPLICADO
class TestLambdaHandler(TestCase):
    # NESTES EXEMPLOS VAMOS VERIFICAR SE ESTAMOS REALMENTE TESTANDO COMPORTAMENTO

    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campos_obrigatorios_preenchidos_e_cliente_existe__entao_envia_email_e_retorna_200(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE

        # LIMPEZA DO MODULO EH IMPORTANTE, POIS SEM ELA FICA REUTILIZANDO OS MOCKS DO CLIENTE_SERVICE E EMAIL SERVICE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler
        mock_cliente_service().consultar.return_value = {'id_cliente': 1}
        mock_email_service().enviar.return_value = True  # enviado

        # ACT
        response = lambda_handler(event={
            'documento': '72705746000101',
            'email': 'cliente@email.com.br'
        }, context={})

        # ASSERT
        self.assertEqual(200, response['statusCode'])

        # Podemos verificar se os metodos foram invocados
        mock_cliente_service().consultar.assert_called_once()
        mock_email_service().enviar.assert_called_once()

    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campo_documento_vazio__entao_retorna_excecao_value_error(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            lambda_handler(event={
                'documento': ''
            }, context={})

        self.assertEqual('Documento Invalido: ', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        mock_cliente_service().consultar.assert_not_called()
        mock_email_service().enviar.assert_not_called()

    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campo_documento_nulo__entao_retorna_excecao_value_error(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            lambda_handler(event={
                'documento': None
            }, context={})

        self.assertEqual('Documento Invalido: None', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        mock_cliente_service().consultar.assert_not_called()
        mock_email_service().enviar.assert_not_called()

    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_sem_campo_documento__entao_retorna_excecao_value_error(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            lambda_handler(event={}, context={})

        # PODERIAMOS MELHORAR O ASSERT?
        self.assertEqual('Documento Invalido: nao-preenchido', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        mock_cliente_service().consultar.assert_not_called()
        mock_email_service().enviar.assert_not_called()

    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campo_email_vazio__entao_retorna_excecao_value_error(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            lambda_handler(event={
                'documento': '72705746000101',
                'email': ''
            }, context={})

        self.assertEqual('Email Invalido: ', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        mock_cliente_service().consultar.assert_not_called()
        mock_email_service().enviar.assert_not_called()

    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campo_email_nulo__entao_retorna_excecao_value_error(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            lambda_handler(event={
                'documento': '72705746000101',
                'email': None
            }, context={})

        # PODERIAMOS MELHORAR O ASSERT?
        self.assertEqual('Email Invalido: None', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        mock_cliente_service().consultar.assert_not_called()
        mock_email_service().enviar.assert_not_called()

    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_sem_campo_email__entao_retorna_excecao_value_error(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            lambda_handler(event={
                'documento': '72705746000101'
            }, context={})

        # PODERIAMOS MELHORAR O ASSERT?
        self.assertEqual('Email Invalido: nao-preenchido', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        mock_cliente_service().consultar.assert_not_called()
        mock_email_service().enviar.assert_not_called()
