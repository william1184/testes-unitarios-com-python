import sys
from unittest import TestCase, mock
from unittest.mock import MagicMock

from src.exception.ClienteNaoExisteException import ClienteNaoExisteException


# CLASSE COM TESTE FUNCIONAIS COM NOMES MELHORES E TESTA COMPORTAMENTO e MENOS DUPLICACOES:
class TestLambdaHandler(TestCase):
    _lambda_handler = None
    _mock_email_service: MagicMock
    _mock_cliente_service: MagicMock

    # RODA ANTES DE CADA TESTE
    @mock.patch('src.service.email_service.EmailService')
    @mock.patch('src.service.cliente_service.ClienteService')
    def setUp(
            self,
            mock_client_service: MagicMock,
            mock_email_service: MagicMock
    ) -> None:
        from lambda_function import lambda_handler

        self._lambda_handler = lambda_handler
        self._mock_cliente_service = mock_client_service
        self._mock_email_service = mock_email_service

    # RODA DEPOIS DE CADA TESTE
    def tearDown(self) -> None:
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        del self._mock_cliente_service
        del self._mock_email_service

    # NESTES EXEMPLOS VAMOS VERIFICAR SE ESTAMOS REALMENTE TESTANDO COMPORTAMENTO

    def test_handler__caso_campos_obrigatorios_preenchidos_e_cliente_existe__entao_envia_email_e_retorna_200(
            self
    ):
        # ARRANGE
        self._mock_cliente_service().consultar.return_value = {'id_cliente': 1}
        self._mock_email_service().enviar.return_value = True  # enviado

        event_valido = {
            'documento': '72705746000101',
            'email': 'cliente@email.com.br'
        }

        # ACT
        response = self._lambda_handler(event=event_valido, context={})

        # ASSERT
        self.assertEqual(200, response['statusCode'])

        # Podemos verificar se os metodos foram invocados
        self._mock_cliente_service().consultar.assert_called_once()
        self._mock_email_service().enviar.assert_called_once()

    def test_handler__caso_campos_obrigatorios_preenchidos_e_cliente_nao_existe__entao_retornar_excecao_cliente_nao_existe(
            self
    ):
        # ARRANGE
        self._mock_cliente_service().consultar.return_value = None

        event_valido = {
            'documento': '72705746000101',
            'email': 'cliente@email.com.br'
        }

        # ACT e ASSERT
        with self.assertRaises(ClienteNaoExisteException) as context:
            self._lambda_handler(event=event_valido, context={})

        self.assertEqual('Cliente nao existe: 72705746000101', context.exception.args[0])

        # Podemos verificar se os metodos foram invocados
        self._mock_cliente_service().consultar.assert_called_once()
        self._mock_email_service().enviar.assert_not_called()

    def test_handler__caso_campo_documento_vazio__entao_retorna_excecao_value_error(
            self,
    ):
        # ARRANGE
        event_invalido_documento_vazio = {
            'documento': ''
        }

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            self._lambda_handler(event=event_invalido_documento_vazio, context={})

        self.assertEqual('Documento Invalido: ', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        self._mock_cliente_service().consultar.assert_not_called()
        self._mock_email_service().enviar.assert_not_called()

    def test_handler__caso_campo_documento_nulo__entao_retorna_excecao_value_error(
            self,
    ):
        # ARRANGE
        event_invalido_documento_nulo = {
            'documento': None
        }

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            self._lambda_handler(event=event_invalido_documento_nulo, context={})

        self.assertEqual('Documento Invalido: None', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        self._mock_cliente_service().consultar.assert_not_called()
        self._mock_email_service().enviar.assert_not_called()

    def test_handler__caso_sem_campo_documento__entao_retorna_excecao_value_error(
            self,
    ):
        # ARRANGE
        event_invalido_sem_campo_documento = {'email': 'cliente@email.com'}

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            self._lambda_handler(event=event_invalido_sem_campo_documento, context={})

        # PODERIAMOS MELHORAR O ASSERT?
        self.assertEqual('Documento Invalido: nao-preenchido', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        self._mock_cliente_service().consultar.assert_not_called()
        self._mock_email_service().enviar.assert_not_called()

    def test_handler__caso_campo_email_vazio__entao_retorna_excecao_value_error(
            self,
    ):
        # ARRANGE
        event_invalido_email_vazio = {
            'documento': '72705746000101',
            'email': ''
        }

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            self._lambda_handler(event=event_invalido_email_vazio, context={})

        self.assertEqual('Email Invalido: ', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        self._mock_cliente_service().consultar.assert_not_called()
        self._mock_email_service().enviar.assert_not_called()

    def test_handler__caso_campo_email_nulo__entao_retorna_excecao_value_error(
            self,
    ):
        # ARRANGE
        event_invalido_email_nulo = {
            'documento': '72705746000101',
            'email': None
        }

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            self._lambda_handler(event=event_invalido_email_nulo, context={})

        # PODERIAMOS MELHORAR O ASSERT?
        self.assertEqual('Email Invalido: None', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        self._mock_cliente_service().consultar.assert_not_called()
        self._mock_email_service().enviar.assert_not_called()

    def test_handler__caso_sem_campo_email__entao_retorna_excecao_value_error(
            self,
    ):
        # ARRANGE
        event_invalido_sem_campo_email = {
            'documento': '72705746000101'
        }

        # ACT and ASSERT
        with self.assertRaises(ValueError) as context:
            self._lambda_handler(event={
                'documento': '72705746000101'
            }, context={})

        # PODERIAMOS MELHORAR O ASSERT?
        self.assertEqual('Email Invalido: nao-preenchido', context.exception.args[0])

        # podemos verificar se os itens nao foram chamados
        self._mock_cliente_service().consultar.assert_not_called()
        self._mock_email_service().enviar.assert_not_called()
