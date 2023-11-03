from unittest import TestCase, mock
from unittest.mock import MagicMock

import lambda_function


# CLASSE DE TESTE QUE NAO FUNCIONA O TESTE:
# NAO ESTA SENDO MOCKADO AS CLASSES ANTES DA INSTANCIACAO DAS MESMAS
class TestLambdaHandler(TestCase):

    # EXEMPLO TESTE UNITÁRIO QUE UTILIZA O MOCK.PATCH PRA MOCKAR AS INSTANCIAS DENTRO DO HANDLER,
    # MAS MESMO ASSIM AINDA NAO ESTA SENDO MOCKADO CORRETAMENTE
    # O TESTE FALHA POIS O IMPORT DO MODÚLO OCORRE ANTES DO MOCK DAS CLASSES
    @mock.patch('src.service.cliente_service.ClienteService')
    @mock.patch('src.service.email_service.EmailService')
    def test_handler__caso_campos_obrigatorios_preenchidos_e_cliente_existe__retorna_200(
            self,
            mock_email_service: MagicMock,
            mock_cliente_service: MagicMock
    ):
        # ARRANGE
        mock_cliente_service.consultar.return_value = {'id_cliente': 1}
        mock_email_service.enviar.return_value = True  # enviado

        # COMENTARIO PARA VERIFICAR A INSTANCIA
        # print(lambda_function.cliente_service)

        # ACT
        response = lambda_function.lambda_handler(event={
            'documento': '72705746000101',
            'email': 'cliente@email.com.br'
        }, context={})

        # ASSERT
        self.assertEqual(200, response['statusCode'])
