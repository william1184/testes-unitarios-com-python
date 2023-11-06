import sys
from unittest import TestCase, mock
from unittest.mock import MagicMock


# CLASSE COM TESTES FUNCIONAIS:
# NOME PARA TESTE PODE SER MELHOR
# MAS NAO TESTA COMPORTAMENTO
# DUPLICA CODIGO
class TestLambdaHandler(TestCase):

    # O TESTE FUNCIONA....
    # O NOME DO TESTE FALA REALMENTE O COMPORTAMENTO ESPERADO EM CASO DE SUCESSO? PS. ELE ENVIA EMAIL EM CASO DE SUCESSO
    # MAS ELE ESTÁ TESTANDO DE VERDADE?
    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campos_obrigatorios_preenchidos__entao_retorna_200(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        import lambda_function
        mock_cliente_service().consultar.return_value = {'id_cliente': 1}
        mock_email_service().enviar.return_value = True  # enviado

        # COMENTARIO PARA VERIFICAR A INSTANCIA
        # print(lambda_function.cliente_service)

        # ACT
        response = lambda_function.lambda_handler(event={
            'documento': '72705746000101',
            'email': 'cliente@email.com.br'
        }, context={})

        # ASSERT
        self.assertEqual(200, response['statusCode'])

    # O DOCUMENTO ESTA SOMENTE NAO PREENCHIDO ?
    # ESSE CENARIO CONTEMPLA TODAS AS FORMAS DE NAO-PREENCHIDO? VAZIO, NULO E CHAVE INEXISTENTE?
    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campo_documento_nao_preenchido__entao_retorna_excecao(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # NAO PRECISO MOCKAR RETORNO, A EXECUCAO NUNCA CHEGA NESSA ETAPA
        # mock_cliente_service().consultar.return_value = {'id_cliente': 1}
        # mock_email_service().enviar.return_value = True  # enviado

        # ESSE CODIGO ESTA REALMENTE DANDO ERRO POR CAUSA DA FALTA DE DOCUMENTO?
        # ACT and ASSERT
        with self.assertRaises(Exception) as context:
            lambda_handler(event={
                'documento': ''
            }, context={})

    # O EMAIL ESTA SOMENTE NAO PREENCHIDO ?
    # ESSE CENARIO CONTEMPLA TODAS AS FORMAS DE NAO-PREENCHIDO? VAZIO, NULO E CHAVE INEXISTENTE?
    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campo_email_nao_preenchido__entao_retorna_excecao(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        if 'lambda_function' in sys.modules:
            del sys.modules['lambda_function']

        from lambda_function import lambda_handler

        # NAO PRECISO MOCKAR RETORNO, A EXECUCAO NUNCA CHEGA NESSA ETAPA
        # mock_cliente_service().consultar.return_value = {'id_cliente': 1}
        # mock_email_service().enviar.return_value = True  # enviado

        # ESSE CODIGO ESTA REALMENTE DANDO ERRO POR CAUSA DA FALTA DE EMAIL?
        # ACT and ASSERT
        with self.assertRaises(Exception) as context:
            lambda_handler(event={
                'documento': '72705746000101',
                'email': ''
            }, context={})
